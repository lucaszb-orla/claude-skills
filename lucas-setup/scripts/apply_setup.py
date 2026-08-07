#!/usr/bin/env python3
"""Apply Lucas project setup assets without overwriting different files."""

from __future__ import annotations

import argparse
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CopyItem:
    source: Path
    destination: Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Apply Lucas setup templates to a new project."
    )
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument(
        "--platform",
        required=True,
        choices=("web", "apple", "both"),
    )
    parser.add_argument(
        "--conductor",
        action="store_true",
        help="Add a starter .conductor/settings.toml for a single platform.",
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def build_copy_plan(skill_dir: Path, target: Path, platform: str, conductor: bool) -> list[CopyItem]:
    assets = skill_dir / "assets"
    plan = [
        CopyItem(assets / "base" / "AGENTS.md", target / "AGENTS.md"),
        CopyItem(assets / "base" / "CLAUDE.md", target / "CLAUDE.md"),
        CopyItem(
            assets / "base" / "PROJECT_CONTEXT.md",
            target / "PROJECT_CONTEXT.md",
        ),
    ]

    selected_platforms = ("web", "apple") if platform == "both" else (platform,)
    for selected in selected_platforms:
        filename = "WEB.md" if selected == "web" else "APPLE.md"
        plan.append(
            CopyItem(
                assets / "platforms" / filename,
                target / "platforms" / filename,
            )
        )

    if conductor:
        if platform == "both":
            raise ValueError("--conductor requires --platform web or --platform apple")
        plan.append(
            CopyItem(
                assets / "conductor" / f"{platform}.toml",
                target / ".conductor" / "settings.toml",
            )
        )

    return plan


def classify(plan: list[CopyItem]) -> tuple[list[CopyItem], list[CopyItem], list[CopyItem]]:
    pending: list[CopyItem] = []
    unchanged: list[CopyItem] = []
    conflicts: list[CopyItem] = []

    for item in plan:
        if not item.destination.exists():
            pending.append(item)
        elif item.destination.is_file() and item.source.read_bytes() == item.destination.read_bytes():
            unchanged.append(item)
        else:
            conflicts.append(item)

    return pending, unchanged, conflicts


def main() -> int:
    args = parse_args()
    skill_dir = Path(__file__).resolve().parent.parent
    target = args.target.expanduser().resolve()

    if target in (Path("/"), Path.home().resolve(), skill_dir):
        print(f"error: refusing broad or internal target: {target}", file=sys.stderr)
        return 2
    if target.exists() and not target.is_dir():
        print(f"error: target is not a directory: {target}", file=sys.stderr)
        return 2

    try:
        plan = build_copy_plan(skill_dir, target, args.platform, args.conductor)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    missing_sources = [item.source for item in plan if not item.source.is_file()]
    if missing_sources:
        for source in missing_sources:
            print(f"missing asset: {source}", file=sys.stderr)
        return 2

    pending, unchanged, conflicts = classify(plan)
    for item in unchanged:
        print(f"unchanged: {item.destination}")
    for item in conflicts:
        print(f"conflict: {item.destination}", file=sys.stderr)

    if conflicts:
        print("No files were copied. Merge conflicting files manually.", file=sys.stderr)
        return 1

    for item in pending:
        action = "would create" if args.dry_run else "created"
        print(f"{action}: {item.destination}")
        if not args.dry_run:
            item.destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(item.source, item.destination)

    if not pending:
        print("Setup already applied.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

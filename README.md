# Skills

Todas as skills que uso com o Claude Code, num repo só pra clonar em outra
máquina/projeto sem precisar reconfigurar tudo do zero.

## O que tem aqui

- **Minhas de verdade**: `slop-cleaner`, `claude-code-playbook`, `lucas-setup`,
  `apple-hig`, `design-principles`, `book-to-obsidian`, `yt-to-obsidian`,
  `vault-setup`. Escritas/ajustadas por mim, não vêm de nenhum pacote externo.
- **Instaladas via [`npx skills`](https://www.npmjs.com/package/skills)**: o
  resto (a maioria de [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable)).
  `.skill-lock.json` registra a origem, versão e hash de cada uma — é o que o
  instalador usa pra saber o que já está instalado e de onde atualizar.
- **Instaladas na mão**: `diagram-design` (de
  [`cathrynlavery/diagram-design`](https://github.com/cathrynlavery/diagram-design),
  clonado em `~/code` e symlinkado) e `security-audit` (de
  [`bybren-llc/wtfb-safe-agentic-workflow`](https://github.com/bybren-llc/wtfb-safe-agentic-workflow),
  copiada direto). Nenhuma das duas está no `.skill-lock.json`, então `npx
  skills` não sabe atualizá-las — pra pegar versão nova, buscar na fonte.
  `security-audit` é template: tem tokens `{{PLACEHOLDER}}` pra trocar pelos
  valores do projeto antes de usar.

Duas ressalvas sobre as minhas:

- `lucas-setup` também tem repo próprio em
  [`lucaszb-orla/lucas-setup`](https://github.com/lucaszb-orla/lucas-setup). A
  cópia aqui existe pra clonagem funcionar de uma vez só; a fonte canônica é o
  repo dela.
- `apple-hig` e `design-principles` também vivem em
  [`lucaszb-orla/hig-skills`](https://github.com/lucaszb-orla/hig-skills), no
  formato instalável via `npx skills add lucaszb-orla/hig-skills`.

As pastas ficam todas soltas na raiz (é o que o passo 2 de clonagem abaixo
espera: `~/.agents/skills/<nome>`), mas por função elas se agrupam assim:

**Design visual (ajuste/polimento de UI existente)**
`animate` · `arrange` · `bolder` · `clarify` · `colorize` · `delight` ·
`distill` · `extract` · `harden` · `make-interfaces-feel-better` ·
`normalize` · `onboard` · `optimize` · `overdrive` · `polish` · `quieter` ·
`transitions-dev` · `typeset`

**Design/build (criar UI e sistemas de design do zero)**
`api-and-interface-design` · `frontend-design` · `frontend-ui-engineering` ·
`hallmark`

**Revisão de design (avaliar, não corrigir)**
`audit` · `critique` · `slop-cleaner`

**Princípios de design (o que construir e por quê, não como)**
`apple-hig` · `design-principles` · `hig-project-context`

**Segundo cérebro (Obsidian)**
`book-to-obsidian` · `vault-setup` · `yt-to-obsidian`

**Processo de engenharia**
`ci-cd-and-automation` · `code-review-and-quality` · `code-simplification` ·
`debugging-and-error-recovery` · `deprecation-and-migration` ·
`documentation-and-adrs` · `doubt-driven-development` ·
`git-workflow-and-versioning` · `incremental-implementation` ·
`karpathy-guidelines` · `observability-and-instrumentation` ·
`performance-optimization` · `planning-and-task-breakdown` ·
`security-and-hardening` · `security-audit` · `shipping-and-launch` ·
`source-driven-development` · `spec-driven-development` ·
`test-driven-development`

**Diagramas técnicos**
`diagram-design`

**Descoberta de requisitos**
`idea-refine` · `interview-me`

**Setup de projeto**
`lucas-setup`

**Marketing**
`seo-audit`

**Meta (sobre o próprio Claude Code / sistema de skills)**
`claude-code-playbook` · `context-engineering` · `find-skills` ·
`teach-impeccable` · `using-agent-skills`

**Testes em navegador**
`browser-testing-with-devtools`

## Sobre as skills de design da Apple

Este repo tinha 14 skills `hig-*` vindas de
[`raintree-technology/hig-doctor`](https://github.com/raintree-technology/hig-doctor).
Foram removidas em 2026-08-06 e substituídas por `apple-hig` e
`design-principles`.

Motivo: os arquivos de referência delas eram índices (só os títulos das boas
práticas, sem o texto que explica o porquê) e vinham de um snapshot de
fevereiro de 2025. Desde então a Apple revisou o HIG duas vezes, incluindo a
reintrodução da página de princípios de design em junho de 2026.

As duas skills que ficaram foram escritas a partir do texto completo do HIG,
capturado dos endpoints DocC de `developer.apple.com` em agosto de 2026 (171
páginas, 227 mil palavras). `apple-hig` cobre o que é específico das
plataformas Apple; `design-principles` cobre o que vale em qualquer lugar,
inclusive web, e tem uma seção explícita do que **não** transportar da Apple.

`hig-project-context` ficou porque não é conteúdo HIG: é utilitário que lê
`Package.swift`, `Info.plist` e imports pra descobrir as plataformas alvo do
projeto e gravar em `.claude/apple-design-context.md`.

O guia HIG completo, em formato de vault Obsidian, vive no segundo cérebro
(`megabrain2.0`), não aqui.

## O que não está neste repo

**Plugins.** Vários plugins instalados via `claude plugin` ficam registrados em
`~/.claude/plugins`, não em `~/.agents/skills`, então não têm cópia aqui. Numa
máquina nova:

```sh
# skills de product management (4 dos 9 do marketplace)
claude plugin marketplace add phuryn/pm-skills
for p in pm-product-discovery pm-execution pm-product-strategy pm-data-analytics; do
  claude plugin install "$p@pm-skills"
done

# ponytail: modo "dev sênior preguiçoso" (hook de sessão + slash commands)
claude plugin marketplace add DietrichGebert/ponytail
claude plugin install ponytail@ponytail

# do marketplace oficial da Anthropic
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin install vercel@claude-plugins-official     # deploy, AI SDK, Next.js
claude plugin install swift-lsp@claude-plugins-official  # LSP de Swift
```

(Existe também um `frontend-design@claude-plugins-official` instalado com
escopo de projeto num repo antigo. É redundante com a skill `frontend-design`
que já está neste repo — não vale reinstalar.)

Dos 9 plugins do `pm-skills`, os outros 5 foram avaliados e descartados:
`pm-ai-shipping` colide com as skills de engenharia já listadas acima,
`pm-toolkit` tem escopo alheio e as partes jurídicas assumem GDPR/CCPA sem
mencionar LGPD, e `pm-market-research`, `pm-go-to-market` e
`pm-marketing-growth` são redundantes entre si até o produto entrar em fase de
crescimento.

## Como usar numa máquina nova

1. Clone este repo em `~/.agents/skills` (ou o caminho equivalente na máquina
   nova):
   ```sh
   git clone <url-deste-repo> ~/.agents/skills
   ```
2. Symlink cada skill em `~/.claude/skills/`, igual já é feito aqui:
   ```sh
   for d in ~/.agents/skills/*/; do
     name=$(basename "$d")
     ln -s "../../.agents/skills/$name" ~/.claude/skills/"$name"
   done
   ```
3. Se preferir reinstalar as de terceiros direto da fonte (em vez da cópia
   congelada aqui) pra pegar atualizações, use `npx skills add <fonte>` com
   base no `.skill-lock.json`.
4. Instale os plugins de PM com o bloco da seção anterior.

Atenção: `book-to-obsidian`, `yt-to-obsidian`, `apple-hig` e
`design-principles` têm o caminho do vault `megabrain2.0` embutido. Numa
máquina onde o vault esteja em outro lugar, ajuste o caminho no topo de cada
uma ou rode `vault-setup` de novo.

## Atualizando

Depois de instalar/editar uma skill em `~/.agents/skills`, só commitar e dar
push normalmente — é um repo git de verdade, não um espelho read-only.

# Skills

Todas as skills que uso com o Claude Code, num repo só pra clonar em outra
máquina/projeto sem precisar reconfigurar tudo do zero.

## O que tem aqui

- **Minhas de verdade**: `slop-cleaner`, `claude-code-playbook`. Escritas/
  ajustadas por mim, não vêm de nenhum pacote externo.
- **Instaladas via [`npx skills`](https://www.npmjs.com/package/skills)**: o
  resto (a maioria de [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable)).
  `.skill-lock.json` registra a origem, versão e hash de cada uma — é o que o
  instalador usa pra saber o que já está instalado e de onde atualizar.

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

## Atualizando

Depois de instalar/editar uma skill em `~/.agents/skills`, só commitar e dar
push normalmente — é um repo git de verdade, não um espelho read-only.

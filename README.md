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

As pastas ficam todas soltas na raiz (é o que o passo 2 de clonagem abaixo
espera: `~/.agents/skills/<nome>`), mas por função elas se agrupam assim:

**Design visual (ajuste/polimento de UI existente)**
`animate` · `arrange` · `bolder` · `clarify` · `colorize` · `delight` ·
`distill` · `extract` · `harden` · `normalize` · `onboard` · `optimize` ·
`overdrive` · `polish` · `quieter` · `transitions-dev` · `typeset`

**Design/build (criar UI e sistemas de design do zero)**
`api-and-interface-design` · `frontend-design` · `frontend-ui-engineering` ·
`hallmark`

**Revisão de design (avaliar, não corrigir)**
`audit` · `critique` · `slop-cleaner`

**Apple HIG (guias de plataforma da Apple)**
`hig-components-content` · `hig-components-controls` ·
`hig-components-dialogs` · `hig-components-layout` · `hig-components-menus` ·
`hig-components-search` · `hig-components-status` · `hig-components-system` ·
`hig-foundations` · `hig-inputs` · `hig-patterns` · `hig-platforms` ·
`hig-project-context` · `hig-technologies`

**Processo de engenharia**
`ci-cd-and-automation` · `code-review-and-quality` · `code-simplification` ·
`debugging-and-error-recovery` · `deprecation-and-migration` ·
`documentation-and-adrs` · `doubt-driven-development` ·
`git-workflow-and-versioning` · `incremental-implementation` ·
`karpathy-guidelines` · `observability-and-instrumentation` ·
`performance-optimization` · `planning-and-task-breakdown` ·
`security-and-hardening` · `shipping-and-launch` ·
`source-driven-development` · `spec-driven-development` ·
`test-driven-development`

**Descoberta de requisitos**
`idea-refine` · `interview-me`

**Meta (sobre o próprio Claude Code / sistema de skills)**
`claude-code-playbook` · `context-engineering` · `find-skills` ·
`teach-impeccable` · `using-agent-skills`

**Testes em navegador**
`browser-testing-with-devtools`

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

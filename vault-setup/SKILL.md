---
name: vault-setup
description: "Onboarding interativo para configurar o Obsidian como cérebro do Claude. Faz perguntas ao usuário, detecta e instala dependências (parseleaf), cria estrutura de pastas do vault, gera CLAUDE.md de instrucoes e produz skills customizadas (book-to-obsidian e yt-to-obsidian) com os caminhos corretos do usuario. Use quando o usuario mencionar 'configurar obsidian', 'setup vault', 'vault-setup', 'instalar skills obsidian', ou quiser comecar a usar o Obsidian como base de conhecimento para o Claude."
---

# Vault Setup — Obsidian como Cérebro do Claude

Skill de onboarding interativo. Configura tudo do zero para que o Claude passe a usar o vault Obsidian do usuario como fonte de verdade.

## O que esta skill faz

1. Coleta configuracoes do usuario via perguntas
2. Detecta e instala dependencias (parseleaf)
3. Cria estrutura de pastas do vault
4. Gera `CLAUDE.md` no vault com instrucoes de uso
5. Gera skills customizadas `book-to-obsidian` e `yt-to-obsidian` com caminhos corretos
6. Executa teste de sanidade opcional com um EPUB

---

## Fluxo de Execucao

### FASE 1 — Coleta de Informacoes

Fazer as seguintes perguntas ao usuario, uma a uma (nao tudo de uma vez):

**Pergunta 1 — Caminho do vault:**
```
Onde você quer criar (ou já tem) seu vault Obsidian?

Exemplos comuns:
  macOS iCloud:  ~/Library/Mobile Documents/iCloud~md~obsidian/Documents/MeuVault
  macOS local:   ~/Documents/MeuVault
  Windows:       C:\Users\SeuNome\Documents\MeuVault

Digite o caminho completo ou pressione Enter para usar ~/Documents/ObsidianVault
```

**Pergunta 2 — Nome do vault:**
```
Qual o nome do seu vault? (será a pasta raiz dentro do caminho informado)
Exemplo: Alpinist, MeuCerebro, KnowledgeBase
```

**Pergunta 3 — Idioma principal:**
```
Em qual idioma você vai usar o vault?
1. Português brasileiro (recomendado)
2. Inglês
3. Outro (especifique)
```

**Pergunta 4 — Estrutura de pastas:**
```
Qual estrutura de pastas você prefere?

1. Padrão Zettelkasten (recomendado):
   1-material-bruto/ → 2-materia-prima/ → 3-marcadores/ → 4-anotacoes/ → 5-modelo/ → 6-artigos/

2. Simples:
   raw/ → livros/ → videos/ → notas/

3. Personalizada (descreva)
```

**Pergunta 5 — EPUB de teste (opcional):**
```
Você tem um arquivo .epub para testar o processamento agora?
Informe o caminho completo ou deixe em branco para pular.
```

Confirmar as respostas antes de continuar:
```
Vou configurar com essas informações:
- Vault: [caminho]/[nome]
- Idioma: [idioma]
- Estrutura: [estrutura escolhida]
- Teste com EPUB: [caminho ou "não"]

Confirma? (s/n)
```

---

### FASE 2 — Verificar e Instalar Dependencias

#### 2.1 Verificar Node.js

```bash
node --version
```

Se falhar:
```
Node.js não encontrado. Por favor instale em: https://nodejs.org
Após instalar, rode /vault-setup novamente.
```

#### 2.2 Verificar parseleaf

Checar nos caminhos comuns:
```bash
which parseleaf || ls /opt/homebrew/bin/parseleaf 2>/dev/null || ls ~/.npm-global/bin/parseleaf 2>/dev/null
```

Se não encontrado, instalar:
```bash
npm install -g parseleaf
```

Se falhar com permissão:
```bash
sudo npm install -g parseleaf
```

Verificar instalacao:
```bash
parseleaf --version
```

Salvar o caminho do parseleaf encontrado/instalado para usar nas skills geradas.

#### 2.3 Verificar yt-dlp (para skill YT)

```bash
which yt-dlp
```

Se não encontrado, instalar via pip ou brew:
```bash
# macOS/Linux com brew
brew install yt-dlp 2>/dev/null || pip3 install yt-dlp
```

---

### FASE 3 — Criar Estrutura do Vault

#### Se estrutura Zettelkasten (opcao 1):

```
[vault-path]/
├── .obsidian/                    ← config do Obsidian (criado pelo Obsidian)
├── 0-sem-curadoria/              ← inbox: capturas rapidas
├── 1-material-bruto/             ← notas incompletas, rascunhos
│   └── notas-diarias/
├── 2-materia-prima/              ← material processado
│   ├── Livros/
│   ├── Videos/
│   ├── Podcasts/
│   └── Artigos/
├── 3-marcadores/                 ← tags e indices
├── 4-anotacoes/                  ← notas finalizadas
├── 5-modelo/                     ← templates
├── 6-artigos/                    ← publicacoes
└── clientes/                     ← (opcional) projetos por cliente
```

#### Se estrutura simples (opcao 2):

```
[vault-path]/
├── raw/
├── livros/
├── videos/
└── notas/
```

Criar as pastas com:
```bash
mkdir -p "[vault-path]/[pasta1]"
mkdir -p "[vault-path]/[pasta2]"
# etc.
```

---

### FASE 4 — Gerar CLAUDE.md no Vault

Criar o arquivo `[vault-path]/CLAUDE.md` com o seguinte conteudo (adaptado com os dados coletados):

```markdown
# Instruções do Vault para o Claude

Este vault Obsidian é a base de conhecimento usada pelo Claude Code.
Quando receber tarefas de análise, estratégia, escrita ou pesquisa, consulte este vault.

## Configuração

- **Vault:** [vault-path]/[vault-name]
- **Idioma:** [idioma escolhido]
- **parseleaf:** [caminho do parseleaf]
- **Estrutura:** [estrutura escolhida]

## Onde Encontrar o Conhecimento

- **Livros processados:** `2-materia-prima/Livros/`
- **Videos do YouTube:** `2-materia-prima/Videos/`
- **Podcasts:** `2-materia-prima/Podcasts/`
- **Notas finalizadas:** `4-anotacoes/`
- **Artigos:** `6-artigos/`

## Como Usar Este Vault

### Referenciar frameworks ao criar conteudo:
"Use os frameworks do vault em 2-materia-prima/Livros/ para criar esta estrategia."

### Consultar autor especifico:
"Leia o contexto de [Autor] em 2-materia-prima/Livros/[Livro - Autor]/ e aplique na tarefa."

### Processar novo livro:
/book-to-obsidian

### Processar video do YouTube:
/yt-to-obsidian

## Skills Disponiveis

- `/book-to-obsidian` — transforma EPUB em notas organizadas no vault
- `/yt-to-obsidian` — processa video do YouTube e salva como nota no vault
```

---

### FASE 5 — Gerar Skills Customizadas

#### 5.1 Criar skill `book-to-obsidian` customizada

Criar o arquivo `~/.claude/skills/book-to-obsidian/SKILL.md` com:
- `VAULT_PATH` substituido pelo caminho real do vault
- `PARSELEAF_PATH` substituido pelo caminho real do parseleaf
- `BOOKS_PATH` substituido pela pasta de livros dentro do vault
- `LANGUAGE` substituido pelo idioma escolhido

Usar o template em `vault-setup/templates/book-to-obsidian.md` como base.

#### 5.2 Criar skill `yt-to-obsidian` customizada

Criar o arquivo `~/.claude/skills/yt-to-obsidian/SKILL.md` com:
- `VAULT_PATH` substituido pelo caminho real do vault
- `VIDEOS_PATH` substituido pela pasta de videos dentro do vault
- `LANGUAGE` substituido pelo idioma escolhido

Usar o template em `vault-setup/templates/yt-to-obsidian.md` como base.

---

### FASE 6 — Teste de Sanidade (se EPUB informado)

Se o usuario informou um EPUB na Fase 1:

1. Rodar parseleaf:
```bash
parseleaf convert "[epub-path]" --out "/tmp/vault-setup-test"
```

2. Verificar se gerou markdown:
```bash
ls /tmp/vault-setup-test/*.md
```

3. Informar resultado ao usuario e perguntar se quer processar o livro completo agora via `/book-to-obsidian`.

---

### FASE 7 — Resumo Final

Exibir resumo completo do que foi configurado:

```
✓ Vault criado em: [caminho completo]
✓ Estrutura de pastas: [estrutura]
✓ CLAUDE.md gerado no vault
✓ parseleaf instalado em: [caminho]
✓ Skill book-to-obsidian instalada
✓ Skill yt-to-obsidian instalada

Próximos passos:
1. Abra o Obsidian e aponte para a pasta: [vault-path]
2. Para processar seu primeiro livro: /book-to-obsidian
3. Para processar um video do YouTube: /yt-to-obsidian
4. Use o Claude em qualquer projeto referenciando o vault pelo caminho acima
```

---

## Regras de Comportamento

- Fazer perguntas uma a uma, esperar resposta antes de continuar
- Nunca assumir caminhos sem confirmar com o usuario
- Se algum passo falhar, explicar o erro com clareza e sugerir solucao
- Nao prosseguir para a proxima fase se a atual tiver erros criticos
- Confirmar antes de sobrescrever arquivos existentes

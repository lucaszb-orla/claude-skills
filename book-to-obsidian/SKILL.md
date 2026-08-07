---
name: book-to-obsidian
description: "Processa livros (epub ou markdown bruto) em notas organizadas no vault Obsidian megabrain2.0, seguindo o método de chunks com contexto: nota hub, contexto, capítulos resumidos e fonte limpa. Use quando o usuário mencionar 'processar livro', 'epub para obsidian', 'book to obsidian', 'resumir livro', ou quando houver um epub/markdown de livro para processar."
---

# Book to Obsidian — megabrain2.0

Transforma livros (epub ou markdown bruto de epub) em um sistema completo de notas no Obsidian, seguindo o metodo Karpathy: processar em chunks com contexto, nunca jogar o arquivo inteiro de uma vez.

## Configuracao (hardcoded para este vault)

- `VAULT_PATH`: `/Users/lucasbaggiotto/Documents/Documents/Projetos/megabrain2.0`
- `BOOKS_PATH`: `2-materia-prima/Livros/`
- `PARSELEAF_PATH`: `/opt/homebrew/bin/parseleaf`
- `LANGUAGE`: portugues brasileiro

Se `VAULT_PATH` nao existir, ler `CLAUDE.md` do vault ou perguntar ao usuario.

---

## FASE 1 — Receber Input

Pedir ao usuario o arquivo de entrada:

```
Qual o caminho do arquivo EPUB (ou markdown bruto) do livro?
Exemplo: ~/Downloads/100-million-offers.epub
```

Verificar se o arquivo existe antes de continuar.

---

## FASE 2 — Converter

### 2.1 Se input e .epub

```bash
parseleaf convert "[epub-path]" --out "/tmp/parseleaf-[nome-do-livro]"
```

Onde `[nome-do-livro]` e o nome do arquivo sem extensao, com espacos trocados por hifens.

Converter em `/tmp`, nao dentro do vault. So o resultado final entra no vault.

### 2.2 O que o parseleaf produz

Verificado na versao 0.1.1. O output **nao** e um markdown unico: e **um arquivo por secao** mais um manifesto.

```
/tmp/parseleaf-[nome]/
├── manifest.json                          ← indice completo do livro
├── 01-[slug-da-secao].md
├── 02-[slug-da-secao].md
└── ...
```

Cada `.md` de secao ja vem com frontmatter proprio:

```yaml
---
book_title: Pride and Prejudice
book_author: Jane Austen
section_type: chapter
section_title: CHAPTER XIII
order: 14
source_hrefs: [...]
source_anchor: pgepubid00106
nav_label: CHAPTER XIII
---
```

### 2.3 Ler o manifest.json primeiro

O `manifest.json` e a fonte de verdade da estrutura. Ler ele antes de qualquer coisa:

```json
{
  "book": { "title": "...", "author": "...", "language": "en", "slug": "...", "inputFile": "..." },
  "generatedAt": "...",
  "sections": [
    { "order": 1, "file": "01-....md", "title": "...", "navLabel": "...",
      "sectionType": "chapter", "sourceAnchor": "...", "assets": [] }
  ],
  "assets": [...]
}
```

Usar `book.title` e `book.author` para nomear a pasta do livro. Usar `sections[]` para saber a ordem e o titulo de cada capitulo, sem precisar varrer headings.

### 2.4 Limpar cada arquivo de secao

Artefatos reais que o parseleaf deixa:

1. **Anchors HTML soltos:** linhas com apenas `<a id="..."></a>` — remover
2. **Anchors dentro de headings:** `## <a id="X"></a><a id="X"></a>` seguido do titulo em linha separada — colapsar para `## Titulo`
3. **Anchors colados no inicio de paragrafo:** `<a id="X"></a>Texto do paragrafo` vira `Texto do paragrafo`
4. **Anchors de imagem:** `<a id="img_images_i_107_a.jpg"></a>` — remover
5. **Qualquer outra tag HTML residual:** `<div>`, `<span>`, `<svg>`
6. **Colapsar linhas em branco excessivas** (max 2 consecutivas)

O italico `_texto_` e markdown valido. **Nao** mexer.

Aplicar a limpeza com um script Python de uso unico (regex sobre os arquivos), nao arquivo por arquivo na mao.

### 2.5 Descartar secoes que nao sao conteudo

O manifesto costuma trazer secoes de sumario, licenca, colofao, creditos da editora. Filtrar pelo `title` / `navLabel` antes de resumir. Nao gastar processamento em pagina de copyright.

---

## FASE 3 — Montar o Indice

Ja vem pronto do `manifest.json`. Montar a lista de capitulos a processar:

- Numero (`order`)
- Titulo (`title` / `navLabel`)
- Caminho do arquivo (`file`)

Se o livro tiver agrupamento em partes ou secoes, inferir pelos titulos e agrupar na tabela da nota hub.

Se o `manifest.json` nao existir (input foi markdown bruto, nao epub), cair no fallback: mapear headings `# ` e `## ` do arquivo e delimitar cada capitulo por linha inicial e final.

---

## FASE 4 — Criar Estrutura de Pastas

```
[VAULT_PATH]/2-materia-prima/Livros/[Titulo do Livro - Autor]/
├── [Titulo do Livro - Autor].md    ← nota hub (resumo consolidado)
├── contexto.md                      ← contexto do livro
├── capitulos/
│   ├── 00 - Primeiro Capitulo.md
│   ├── 01 - Segundo Capitulo.md
│   └── ...
└── fonte/
    ├── manifest.json                  ← indice original do parseleaf
    ├── secoes/                        ← um .md por secao, ja limpo
    │   ├── 01-....md
    │   └── ...
    ├── cover.jpeg
    └── *.jpeg                         ← imagens extraidas
```

Mover para `fonte/`:
- O `manifest.json`
- Todos os arquivos de secao ja limpos, dentro de `fonte/secoes/`
- Todas as imagens extraidas

Apagar `/tmp/parseleaf-[nome-do-livro]` no final.

---

## FASE 5 — Buscar Contexto do Livro

Usar WebSearch para buscar informacoes sobre o livro:
- Resumo geral (Wikipedia, Goodreads, blogs)
- Quem e o autor e por que e relevante
- Conceitos-chave reconhecidos

Combinar com a descricao do frontmatter e a introducao do proprio livro.

---

## FASE 6 — Escrever contexto.md

```yaml
---
title: "Contexto - [Titulo do Livro]"
author: Nome do Autor
type: contexto-livro
tags:
  - livro
  - [tags relevantes ao tema]
---
```

Secoes obrigatorias:
1. **Sobre o autor**: quem e, o que fez, por que e relevante
2. **Tese central**: o argumento principal do livro em 2-3 paragrafos
3. **Conceitos-chave**: lista com [[wikilinks]] para cada conceito importante
4. **Estrutura do livro**: secoes e como se conectam
5. **Para quem e**: publico-alvo do livro

---

## FASE 7 — Resumir Capitulos

Para cada capitulo listado no manifesto, ler o arquivo de secao limpo em `fonte/secoes/` e gerar um resumo.

**IMPORTANTE:** Usar o `contexto.md` como ancora. Cada resumo e feito com consciencia do livro inteiro.

### Template de capitulo:

```yaml
---
title: "Cap. XX - [Titulo]"
book: "[Titulo do Livro]"
author: Nome do Autor
type: capitulo-livro
chapter: XX
tags:
  - livro
  - [tags especificas do capitulo]
---
```

Secoes de cada capitulo:
1. **Ideia central**: 1-2 paragrafos com o argumento principal
2. **Conceitos e Frameworks**: modelos, formulas, frameworks (com [[wikilinks]])
3. **Exemplos memoraveis**: historias e casos citados
4. **Action items**: 3-5 itens acionaveis derivados do capitulo

Meta: 300-600 palavras por capitulo. Denso e util, sem enrolacao.

Usar Agent tool para processar multiplos capitulos em paralelo quando possivel.

---

## FASE 8 — Nota Hub (nota principal)

A nota `[Titulo do Livro - Autor].md` e o hub central:

```yaml
---
title: "[Titulo Completo do Livro]"
author: Nome do Autor
publisher: Editora
date: YYYY-MM-DD
type: resumo-livro
tags:
  - livro
  - [todas as tags relevantes]
cover: "[[fonte/cover.jpeg]]"
---
```

### Estrutura da nota hub:

1. Capa e citacao-chave do livro
2. Link para contexto: `[[contexto|Contexto completo do livro]]`
3. Info do autor (2-3 linhas com [[wikilinks]])
4. Tese em 1 paragrafo
5. Tabela de capitulos por secao:

```markdown
| # | Capitulo | Ideia Central |
|---|---------|--------------|
| 0 | [[00 - Nome]] | Frase curta |
```

6. Framework completo (se o livro apresenta um processo step-by-step)
7. Equacoes e modelos-chave
8. Citacoes memoraveis (5-8 quotes marcantes)
9. Conexoes: links para outros livros, autores e conceitos do vault
10. Link para fonte: `[[fonte/Nome do Livro|texto completo]]`

---

## Regras de Escrita

<HARD-RULES>
- Escrever em portugues brasileiro
- NUNCA usar travessao (em-dash). Substituir por ponto final, virgula, dois-pontos
- Adicionar [[wikilinks]] para conceitos-chave que podem se conectar a outras notas
- Antes de criar um wikilink novo, buscar no vault se ja existe nota com esse nome
- Adicionar tags relevantes no frontmatter YAML
- Resumos densos e acionaveis, sem enrolacao
- Imagens referenciadas como `./fonte/filename.ext`
</HARD-RULES>

---

## Checklist Final

- [ ] Secoes limpas, sem anchors `<a id="...">` sobrando
- [ ] Secoes de licenca, sumario e colofao descartadas
- [ ] `manifest.json` e secoes em `fonte/`
- [ ] Todas as imagens em `fonte/`
- [ ] `contexto.md` com tese e conceitos-chave
- [ ] Todos os capitulos resumidos em `capitulos/`
- [ ] Nota hub com tabela, framework, citacoes e conexoes
- [ ] [[Wikilinks]] em todos os conceitos importantes
- [ ] Tags no frontmatter de todos os arquivos
- [ ] Nenhum travessao em nenhum arquivo
- [ ] `/tmp/parseleaf-*` removida
- [ ] Nomes de arquivo limpos e amigaveis para Obsidian

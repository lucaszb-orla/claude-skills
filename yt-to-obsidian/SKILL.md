---
name: yt-to-obsidian
description: "Processa videos do YouTube em notas organizadas no vault Obsidian megabrain2.0. Extrai transcricao, gera resumo, insights, conceitos-chave, action items e wikilinks. Use quando o usuario mencionar 'processar video', 'youtube para obsidian', 'yt-to-obsidian', 'salvar video no vault', ou fornecer uma URL do YouTube."
---

# YT to Obsidian — megabrain2.0

Transforma videos do YouTube em notas estruturadas no vault, seguindo o mesmo padrao do processamento de livros: contexto, insights, conceitos-chave e action items.

## Configuracao (hardcoded para este vault)

- `VAULT_PATH`: `/Users/lucasbaggiotto/Documents/Documents/Projetos/megabrain2.0`
- `VIDEOS_PATH`: `2-materia-prima/Videos/`
- `YTDLP_PATH`: `/opt/homebrew/bin/yt-dlp`
- `LANGUAGE`: portugues brasileiro

Se `VAULT_PATH` nao existir, ler `CLAUDE.md` do vault ou perguntar ao usuario.

---

## FASE 1 — Receber URL

Se nao foi passada como argumento, pedir:
```
Informe a URL do vídeo do YouTube:
```

Validar que e uma URL do YouTube (youtube.com ou youtu.be).

---

## FASE 2 — Extrair Metadados e Transcricao

### 2.1 Buscar metadados via yt-dlp

```bash
yt-dlp --dump-json --no-download "[URL]"
```

Extrair do JSON:
- `title` — titulo do video
- `uploader` / `channel` — nome do canal
- `upload_date` — data de upload (formato YYYYMMDD)
- `duration` — duracao em segundos
- `description` — descricao do video
- `webpage_url` — URL canonica
- `thumbnails` — URL da thumbnail

### 2.2 Extrair transcricao

Tentar extrair legenda automatica em PT-BR primeiro, depois EN:

```bash
yt-dlp --write-auto-subs --sub-lang "pt-BR,pt,en" --sub-format vtt --skip-download --output "/tmp/yt-obsidian-[id]" "[URL]"
```

Se nao tiver legenda automatica, tentar legenda manual:
```bash
yt-dlp --write-subs --sub-lang "pt-BR,pt,en" --sub-format vtt --skip-download --output "/tmp/yt-obsidian-[id]" "[URL]"
```

Converter VTT para texto limpo: remover timestamps, tags HTML e linhas duplicadas.

Se nao conseguir transcricao:
```
Não foi possível extrair transcrição automática. Vou processar com base nos metadados e descrição do vídeo.
Quer fornecer a transcrição manualmente? (cole o texto ou pressione Enter para continuar sem ela)
```

### 2.3 Baixar thumbnail (opcional)

```bash
yt-dlp --write-thumbnail --skip-download --output "[VAULT_PATH]/[VIDEOS_PATH]/[YYYY-MM]/thumbnail" "[URL]"
```

---

## FASE 3 — Processar com Claude

Com base nos metadados e transcricao, gerar a nota com as seguintes secoes:

### Resumo executivo (3-5 paragrafos)
O que o video ensina, qual o argumento central, por que importa.

### Insights principais (5-10 bullets)
As ideias mais importantes, formulas, frameworks, numeros citados.
Cada insight como bullet com [[wikilinks]] para conceitos que se conectam ao vault.

### Conceitos-chave
Lista de conceitos com definicoes breves. Cada conceito como [[wikilink]].

### Citacoes memoraveis
3-5 frases marcantes do video, com contexto.

### Action items
3-7 acoes concretas que o espectador pode tomar com base no conteudo.

### Conexoes
Links para outros videos, livros ou notas do vault que abordam temas relacionados.
Buscar por [[wikilinks]] que ja existam no vault antes de criar novos.

---

## FASE 4 — Criar Nota no Vault

### 4.1 Nome do arquivo

Formato: `[YYYY-MM-DD] [Canal] - [Titulo Limpo].md`

Regras para o titulo:
- Remover caracteres especiais (exceto hifens e underscores)
- Manter maximo 80 caracteres

### 4.2 Estrutura do arquivo

```yaml
---
title: "[Titulo do Video]"
channel: "[Nome do Canal]"
url: "[URL do Video]"
date: YYYY-MM-DD
duration: "[X min]"
type: video-yt
tags:
  - video
  - [tags tematicas relevantes]
---
```

```markdown
![[thumbnail.jpg]]

# [Titulo do Video]

**Canal:** [Nome do Canal]
**Data:** [Data de Upload]
**Duracao:** [X min]
**Link:** [URL]

---

## Resumo

[resumo executivo aqui]

---

## Insights Principais

- [[conceito-1]]: insight detalhado
- [[conceito-2]]: insight detalhado
- insight sem wikilink quando nao for um conceito autonomo

---

## Conceitos-chave

- **[[Conceito 1]]**: definicao breve
- **[[Conceito 2]]**: definicao breve

---

## Citacoes Memoraveis

> "Citacao marcante aqui." — [Nome do Autor/Speaker]

---

## Action Items

- [ ] Acao concreta 1
- [ ] Acao concreta 2

---

## Conexoes

- [[Outro Video ou Livro]] — motivo da conexao
- [[Conceito Relacionado]] — como se conecta

---

## Transcricao Completa

[transcricao aqui, se disponivel]
```

### 4.3 Destino no vault

Salvar em:
```
[VAULT_PATH]/2-materia-prima/Videos/[YYYY-MM]/[nome-do-arquivo].md
```

Organizar por mes de publicacao. Criar pasta do mes se nao existir.

---

## Regras de Escrita

<HARD-RULES>
- Escrever em portugues brasileiro
- NUNCA usar travessao (em-dash) no corpo do texto. Substituir por ponto final, virgula, dois-pontos
- Adicionar [[wikilinks]] para conceitos-chave que podem se conectar a outras notas
- Antes de criar um wikilink novo, buscar no vault se ja existe nota com esse nome
- Adicionar tags relevantes no frontmatter YAML
- Insights concisos e acionaveis, sem enrolacao
- Transcricao: traduzir para portugues se o video for em outro idioma
</HARD-RULES>

---

## Checklist Final

- [ ] Metadados completos no frontmatter
- [ ] Resumo executivo em 3-5 paragrafos
- [ ] Pelo menos 5 insights com [[wikilinks]]
- [ ] Conceitos-chave listados
- [ ] Citacoes memoraveis (se houver)
- [ ] Action items acionaveis
- [ ] Conexoes com outras notas do vault
- [ ] Transcricao incluida (quando disponivel)
- [ ] Nota salva na pasta correta com nome formatado
- [ ] Nenhum travessao no corpo do texto

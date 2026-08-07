---
name: lucas-setup
description: Preparar projetos novos ou recém-iniciados com as preferências de desenvolvimento do Lucas, instruções para Codex e Claude Code, contexto preenchível, orientação para web, iOS ou macOS e configuração opcional do Conductor. Usar quando o usuário pedir para criar um projeto, iniciar um repositório, aplicar seu setup pessoal, adicionar AGENTS.md ou CLAUDE.md, preparar um workspace do zero ou padronizar um projeto novo.
---

# Lucas Setup

Preparar a fundação de um projeto sem escolher silenciosamente produto, stack ou arquitetura.
Aplicar os templates incluídos e adaptar somente o que o contexto real sustentar.

## Fluxo

1. Inspecionar o diretório alvo, arquivos de instrução, manifestos e estado do Git.
2. Determinar se o projeto é web, Apple ou multiplataforma pelo pedido e pelos arquivos existentes.
3. Se a escolha de plataforma ou stack mudar materialmente o resultado e não puder ser descoberta,
   fazer uma pergunta curta antes de criar código.
4. Aplicar os arquivos base:
   - Em diretório novo ou sem arquivos conflitantes, executar
     `python3 <skill-dir>/scripts/apply_setup.py --target <diretório> --platform <web|apple|both>`.
   - Em projeto com `AGENTS.md`, `CLAUDE.md` ou `PROJECT_CONTEXT.md`, não sobrescrever. Ler ambos,
     consolidar regras compatíveis e apontar conflitos reais.
5. Preencher `PROJECT_CONTEXT.md` com fatos observados. Não deixar exemplos que pareçam decisões.
6. Criar ou adaptar o projeto somente se o pedido incluir scaffolding ou implementação.
7. Configurar o Conductor somente quando pedido ou quando o projeto estiver sendo preparado para ele.
8. Validar arquivos, comandos, Git e ausência de segredos.

## Aplicar os assets

Usar `scripts/apply_setup.py` para uma cópia determinística e sem sobrescrita. O script:

- cria o diretório alvo quando necessário;
- copia `AGENTS.md`, `CLAUDE.md` e `PROJECT_CONTEXT.md`;
- copia apenas as orientações das plataformas escolhidas;
- recusa qualquer arquivo existente com conteúdo diferente;
- aceita `--dry-run`;
- aceita `--conductor` para uma plataforma única.

Para um projeto Apple:

```sh
python3 <skill-dir>/scripts/apply_setup.py \
  --target /caminho/do/projeto \
  --platform apple \
  --conductor
```

Para um projeto web:

```sh
python3 <skill-dir>/scripts/apply_setup.py \
  --target /caminho/do/projeto \
  --platform web \
  --conductor
```

Depois da cópia, editar `PROJECT_CONTEXT.md` com `apply_patch`.

## Decisões de projeto

- Não escolher framework, banco, arquitetura, bundle ID, deployment target ou provedor sem evidência
  no pedido ou no repositório.
- Preferir a stack e o gerenciador já adotados.
- Em projeto realmente vazio, oferecer uma recomendação curta baseada no produto, mas separar
  recomendação de decisão confirmada.
- Não adicionar dependências ou serviços apenas para completar um template.
- Não alterar arquivos gerados quando houver fonte declarativa.

## Preferências obrigatórias

- Não usar travessão longo em interface, documentação, comentários ou conteúdo exportado.
- Não adicionar borda decorativa ao onboarding.
- Quando houver arte principal no onboarding, mantê-la como único destaque material.
- Preservar mudanças do usuário e manter o escopo cirúrgico.
- Fazer commits pequenos e atômicos depois de validar incrementos relevantes.
- Atualizar a memória do projeto quando surgir decisão ou gotcha duradouro.

## Conductor

Antes de criar configuração, investigar os comandos reais de setup, execução e teste.

- Usar `.conductor/settings.toml` para configuração compartilhada.
- Usar `.conductor/settings.local.toml` para preferências locais do repositório.
- Usar `CONDUCTOR_PORT` em servidores configuráveis.
- Marcar execução como não concorrente quando banco, porta ou serviço local não puder ser isolado.
- Não criar worktree aninhada dentro de um workspace do Conductor.
- Tratar os TOMLs em `assets/conductor/` como pontos de partida, nunca como fatos do projeto.

## Git e GitHub

- Inicializar Git e criar repositório remoto somente quando o pedido autorizar essas ações.
- Antes do primeiro commit, validar o diff e procurar segredos.
- Usar branch padrão `main`, salvo convenção existente.
- Não renomear branch ativa sem pedido explícito.
- Não publicar projeto como público quando a visibilidade não estiver clara.

## Verificação

Confirmar:

- `AGENTS.md`, `CLAUDE.md` e `PROJECT_CONTEXT.md` existem e são coerentes;
- somente as orientações de plataforma aplicáveis foram adicionadas;
- o contexto não contém exemplos tratados como decisões;
- configurações do Conductor usam comandos reais;
- testes ou comandos estreitos relevantes passam;
- o Git não contém segredos, artefatos ou mudanças fora do escopo.

Informar no final o que foi criado, o que precisa ser preenchido e qualquer validação não executada.

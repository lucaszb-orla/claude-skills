# Guia de trabalho do projeto

Leia `PROJECT_CONTEXT.md` e a orientação da plataforma aplicável antes de trabalhar.

## Prioridades

1. Atender ao pedido atual.
2. Preservar comportamento, dados e mudanças existentes.
3. Seguir o contexto e as convenções do projeto.
4. Implementar a menor solução completa e verificável.
5. Deixar código e documentação coerentes para a próxima sessão.

Não escolha silenciosamente entre instruções conflitantes quando a decisão mudar o resultado.

## Antes de alterar

- Leia os arquivos relacionados, a documentação e o estado do Git.
- Descubra stack, gerenciador, fonte de verdade, comandos e padrões existentes.
- Diferencie fatos de hipóteses e declare hipóteses materiais.
- Consulte documentação oficial para APIs e ferramentas que possam ter mudado.
- Não altere arquivos gerados quando existir uma fonte declarativa.

## Escopo e arquitetura

- Faça mudanças cirúrgicas e preserve alterações não relacionadas.
- Reutilize padrões do projeto antes de adicionar bibliotecas ou camadas.
- Prefira código direto. Uma abstração deve reduzir duplicação real ou proteger uma fronteira estável.
- Trate entrada externa e dados persistidos como não confiáveis.
- Nunca registre, versione ou exiba segredos.

## Git

- Verifique `git status` antes e depois.
- Use worktree separada quando houver tarefas concorrentes.
- No Conductor, o workspace já é uma worktree. Não crie outra dentro dele.
- Faça commits atômicos depois de validar cada incremento relevante.
- Não renomeie a branch atual sem pedido explícito.
- Não force push em branch compartilhada sem autorização.
- Resolva conflitos de artefatos gerados na fonte declarativa e regenere.
- Descrição de pull request nunca leva assinatura de ferramenta ("Generated with Claude Code", link
  ou emoji de robô). Esta regra vence o padrão da ferramenta. A autoria fica no autor do commit e no
  `Co-Authored-By`.

## Verificação

- Rode testes relacionados, build, lint e verificação de tipos quando existirem.
- Exercite manualmente o fluxo de maior risco quando possível.
- Para web, valide em navegador real e confira console e rede.
- Para Apple, valide a plataforma e configuração realmente afetadas.
- Confira o diff, arquivos inesperados e possíveis segredos.
- Diga claramente o que não pôde ser validado.

## Interface e conteúdo

- Prefira padrões nativos, legibilidade e hierarquia antes de decoração.
- Não adicione borda decorativa ao onboarding.
- Quando houver arte principal, ela deve ser o único destaque material.
- Não use travessão longo em interface, documentação, comentários ou conteúdo exportado.
- Inclua estados de vazio, carregamento, erro e sucesso quando aplicáveis.
- Respeite acessibilidade, contraste, foco, teclado, texto dinâmico e redução de movimento.
- Localize todo texto visível e separe texto de interface de prompts internos.
- Limite o conteúdo interno, não o fundo completo da tela ou janela.

## Ferramentas

- Use o gerenciador e o lockfile existentes.
- Adicione dependências somente quando o benefício justificar manutenção e risco.
- Faça scripts funcionarem em shell não interativo.
- Não assuma que apps GUI herdam o `PATH` do shell.
- Consuma ou redirecione stdout e stderr de processos.
- Prefira portas e recursos isolados para workspaces concorrentes.

## Memória do projeto

Atualize `PROJECT_CONTEXT.md` quando mudar arquitetura, comandos, estado relevante ou quando surgir
um gotcha duradouro. Edite fatos obsoletos em vez de duplicá-los.

## Plataforma

- Web: leia `platforms/WEB.md`.
- iOS ou macOS: leia `platforms/APPLE.md`.
- Multiplataforma: leia ambos e documente qual regra vale em cada camada.

## Conductor

- Use `CONDUCTOR_PORT` quando o servidor aceitar porta configurável.
- Use execução concorrente somente com portas, bancos e serviços isoláveis.
- Use `.worktreeinclude` para arquivos locais estáticos e gitignored.
- Use `.conductor/settings.toml` para configuração compartilhada.
- Use `.conductor/settings.local.toml` para preferências locais do repositório.

## Conclusão

Confirme que o pedido foi atendido, o comportamento foi verificado, o diff não contém segredos ou
artefatos e a memória registra qualquer aprendizado duradouro.

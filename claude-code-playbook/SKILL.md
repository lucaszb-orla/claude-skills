---
name: claude-code-playbook
description: >
  Práticas de como usar o Claude Code de forma mais eficiente, baseadas no
  relatório oficial da Anthropic "How Anthropic teams use Claude Code"
  (entrevistas com 10 times internos) e no vídeo/discussão de Boris Cherny e
  Cat Wu sobre CLAUDE.md e loops de agente. Use ao configurar um CLAUDE.md
  novo, decidir entre modo autônomo e supervisionado, montar um loop de
  trabalho, ou quando o usuário pedir dicas de como tirar mais proveito do
  Claude Code.
---

# Como usar o Claude Code melhor

Origem: [How Anthropic teams use Claude Code](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)
(relatório oficial da Anthropic, entrevistas com os times de Data
Infrastructure, Product Development, Security Engineering, Inference, Data
Science, API, Growth Marketing, Product Design, RL Engineering e Legal), mais
o vídeo em que Boris Cherny e Cat Wu (criadores do Claude Code) explicam os
mesmos princípios em detalhe.

Uso: não é um checklist de correção, é um conjunto de hábitos que separam quem
usa o Claude Code superficialmente de quem tira o máximo dele. Aplique o que
fizer sentido pro contexto, não force os 12 pontos em toda tarefa pequena.

## 1. CLAUDE.md é a memória persistente, trate como tal

Quanto melhor documentado o workflow, as ferramentas e as expectativas no
CLAUDE.md, melhor o Claude Code performa. Não é só arquitetura: inclua
convenções específicas ("rode `pytest`, não `npm run test`", "não dê `cd`
desnecessário, use o caminho certo direto") sempre que perceber o mesmo erro
de tool-calling se repetindo. Sessões que terminam bem valem um resumo/ajuste
de volta no CLAUDE.md antes de encerrar. Isso cria um loop de melhoria
contínua: cada sessão deixa a próxima mais eficiente. Prefira editar seções
existentes a duplicar informação.

## 2. Classifique a tarefa antes de escolher o nível de supervisão

- **Autônomo (auto-accept, `shift+tab`)**: tarefas periféricas, prototipagem,
  problemas abstratos/fora da área de expertise de quem está pedindo. Deixe
  rodar, revise a solução ~80% pronta, refine o resto.
- **Síncrono, supervisionado**: lógica de negócio central, fixes críticos.
  Prompt detalhado, acompanhamento em tempo real, revisão de arquitetura e
  estilo enquanto anda.

Regra prática: se o nome/função é ambíguo ou parecido com outra coisa no
código, seja bem mais específico no prompt antes de confiar no autônomo.

## 3. Tente de primeira, só depois colabore

Dê um prompt rápido e deixe tentar a implementação inteira primeiro. Quando
funciona de primeira (não é sempre, um time reportou ~1/3 das vezes), já
economizou tempo. Quando não funciona, aí sim mude pro modo colaborativo e
guiado passo a passo.

## 4. Trate como caça-níquel, não como alguém pra convencer

Salve o estado (commit), deixe rodar um tempo (ex.: 30 min), e então aceite ou
recomece do zero. Recomeçar do zero costuma ter taxa de sucesso maior que
tentar consertar/discutir com o Claude em cima do que já saiu errado.
Consequência direta: **sempre comece de um git state limpo e commite
checkpoints com frequência**, assim reverter é trivial se ele sair dos
trilhos.

## 5. Interrompa pedindo simplicidade quando perceber complexidade

O modelo tende a soluções mais complexas por padrão. Não hesite em parar e
perguntar "por que você tá fazendo isso assim? tenta uma versão mais simples"
no meio do processo — ele responde bem a esse pedido.

## 6. Loops auto-suficientes: deixe o Claude checar o próprio trabalho

Configure pra ele rodar build/lint/teste sozinho depois de mudar algo, em vez
de só entregar e esperar revisão manual. Pedir pra escrever os testes antes
(ou logo depois) do código de verdade é o que mais rende nesse quesito: ele
passa a pegar os próprios erros e trabalhar autônomo por mais tempo sem
travar esperando confirmação a cada passo.

## 7. Use o Claude Code como primeiro passo, não como oráculo

Antes de sair editando: peça pra ele mapear quais arquivos examinar, explicar
dependências, ou descrever o comportamento que você tá vendo ("acha que
consegue arrumar esse bug? é esse o comportamento que eu tô vendo"). Trate
como parceiro iterativo, não solução de um tiro só — comece com o mínimo de
contexto e deixe ele guiar, em vez de escrever um relatório inteiro antes de
perguntar.

## 8. Imagem vale mais que descrição em texto

Cole screenshots de dashboard, mockup, tela de erro, ou design direto no
Claude Code (`Cmd+V`) em vez de descrever em texto. Funciona bem tanto pra
debugar (ex.: seguir um erro de infra passo a passo por print de tela) quanto
pra prototipar UI (mockup vira protótipo funcional que dá pra iterar).

## 9. Planeje/discuta antes de sair codando

Pra tarefas grandes ou pouco definidas: primeiro converse a ideia inteira
(modo texto, sem tocar em código), peça um resumo em passo a passo, só então
peça pra implementar — de preferência incremental, um passo por vez, não tudo
de uma vez. Isso evita tanto você quanto o Claude ficarem sobrecarregados no
meio da tarefa.

## 10. Quebre workflows complexos em sub-agentes especializados

Em vez de um prompt/agente só tentando fazer tudo, separe por responsabilidade
(ex.: um agente só pra título, outro só pra descrição; um só pra achar bug,
outro só pra revisar a correção). Fica mais fácil de debugar e a qualidade da
saída melhora quando cada agente tem um escopo estreito.

## 11. MCP em vez de CLI cru quando o dado é sensível

Prefira um servidor MCP a uma CLI genérica (ex. BigQuery CLI) quando o
Claude Code vai acessar dados sensíveis: dá controle mais fino sobre o que
ele pode acessar, com log e limite de escopo, em vez de acesso total a uma
ferramenta de linha de comando.

## 12. Contexto persiste entre sessões, use isso a seu favor

Múltiplas instâncias/worktrees em paralelo (uma por projeto/tarefa) mantêm
contexto completo cada uma: ao voltar depois de horas ou dias, o Claude
lembra exatamente onde parou. Isso já é prática natural neste projeto (ver
`CLAUDE.md` do Transcribe: uma worktree por tarefa).

## Bônus: não esconda o protótipo tosco

Compartilhar um protótipo "feio" ou incompleto de algo que o Claude Code fez
inspira outras pessoas a ver possibilidades que não tinham considerado —
mais valioso do que esperar ficar perfeito pra mostrar.

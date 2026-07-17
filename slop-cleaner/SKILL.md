---
name: slop-cleaner
description: >
  Checklist para identificar e remover "AI slop" visual e estrutural (cara de
  interface gerada por IA sem curadoria). Use ao revisar/auditar qualquer
  tela ou componente novo antes de considerá-lo terminado, ou quando o
  usuário disser que algo "parece feito por IA" / "tem cara de AI slop".
  Baseado nos vídeos "How to Avoid AI Slop in Vibe-Coded Landing Pages"
  (DesignCode) e "10 Ways to Prevent AI Slop in Your Frontend UIs" (Tom Is
  Loading), mais observações de campo do usuário. Aplica-se a qualquer
  projeto de frontend, independente de stack.
---

# Slop cleaner

Origem: transcript de dois vídeos, mais itens observados na prática (não citados em nenhum vídeo, mas confirmados como sinal real de "AI slop").
1. [How to Avoid AI Slop in Vibe-Coded Landing Pages](https://www.youtube.com/watch?v=M4DNgmI7MIM) (DesignCode) — foco em decoração visual (glow, gradiente, ícone, fonte).
2. [10 Ways to Prevent AI Slop in Your Frontend UIs](https://www.youtube.com/watch?v=zKBUBVtoM0g) (Tom Is Loading) — foco em estrutura/densidade de UI (cards, bordas, hierarquia, navegação).

Uso: checklist de revisão, não gerador de design — aplique **depois** que a tela já segue o design system do projeto (tokens de cor, componentes de tipografia, etc., se existirem). Slop é sobre curadoria e intenção, não sobre regra de token.

## Parte 1 — decoração visual (vídeo 1, do pior pro mais leve)

1. **Glow blob decorativo** — `radial-gradient` "de luz" solto num canto de card/hero sem nenhuma fonte de luz real por trás. É o sinal que mais entrega "gerado sem pensar".
2. **Gradiente roxo/azul-ciano genérico** — a paleta-padrão de toda ferramenta de IA em 2024/2025. Se a tela não tem motivo de marca pra usar roxo, é sinal de slop.
3. **Eyebrow em CAPS espremido** — texto pequeno em letter-spacing alto mas comprimido no layout (sem padding suficiente ao redor). Diferença entre elegante e slop aqui é só respiro.
4. **Badge/status gratuito** — pill ou selo decorativo sem função real ("NEW", contador, indicador), colocado só porque "parece produto".
5. **Estado selecionado/ativo desalinhado** — border ou highlight com espaçamento assimétrico (ex.: padding-top ≠ padding-left). Sintoma de estilo copiado sem revisão visual.
6. **Ícone de biblioteca genérica sem curadoria** — lucide (ou similar) usado porque "é o que a IA sempre sugere", sem pensar se aquele ícone específico comunica algo. A biblioteca em si raramente é o problema; o problema é ícone decorativo aleatório só pra "preencher" um heading.
7. **Ilustração de IA no lugar de foto real** — quando o conteúdo pedia uma foto (pessoa, produto, ambiente) e apareceu uma ilustração genérica de IA.
8. **Fotos "banco de imagem"** — stock photo genérica, sem relação com a marca.
9. **Linguagem de forma inconsistente entre seções** — uma seção com cantos quadrados, a próxima com cantos muito arredondados, sem critério.
10. **Texto de botão quebrando em duas linhas** — sinal de que ninguém revisou em viewport real.
11. **Gradiente decorativo sem significado** — principalmente gradiente **no texto** de métricas/headings só pra "parecer premium".
12. **Borda cinza/branca lisa em vez de borda com intenção** — borda genérica de 1px cinza em card, quando um destaque de marca (sombra, cor de fundo) comunicaria melhor.
13. **Logo rasterizado cheio** em vez de um logomark SVG limpo.
14. **Fonte genérica de IA** — Inter, Roboto, Arial, system default sem escolha deliberada.
25. **Fundo pontilhado (dot-grid) decorativo** — textura de `radial-gradient(circle, cor 1px, transparent 1px)` repetida em `background-size` pequeno (~16-24px), atrás de heroes/cards escuros. É um dos padrões mais repetidos por ferramentas de IA: some vez sozinho, mas o mais comum é vir colado num glow blob (sinal 1). Sinal de slop tão forte quanto o glow: é decoração copiada em toda superfície escura sem nenhuma variação ou motivo. **Fix:** abolir, não tornar mais sutil — fundo liso (cor sólida do tema) resolve e não perde nada de hierarquia real (a informação já vem de tipografia/espaçamento). Se o dot-grid está pareado com card `$featured`/hero de destaque, aproveite pra conferir se o gradiente ou cor de fundo sozinhos já bastam.

## Parte 2 — estrutura e densidade de UI (vídeo 2)

15. **Card em tudo** — usar card (fundo elevado + borda) pra criar hierarquia visual quando espaçamento, tamanho e peso de fonte já bastariam. Se toda seção da tela virou uma caixa separada, é sinal de slop. Referência dada no vídeo: landing pages "de gosto" (Work OS) apoiam a separação em padding/margin e tipografia, não em contorno.
16. **Toda ação empurrada pro nível mais alto** — ícones de ação ao lado de cada linha (ver, copiar, editar), colunas extras "porque dá pra mostrar" (contador de uso, métricas). Em vez disso: agrupar em menu de contexto, badge clicável, ou aba/página separada. Regra prática: se a página tem uma aba de analytics, não repita o número de uso na tabela principal.
17. **Excesso de bordas** — borda entre cada seção, embaixo de cada heading, ao redor de cada card. Ferramentas de referência (Linear, Notion, Stripe) usam borda raramente e só quando o espaçamento/tipografia não bastam sozinhos.
18. **Sem hierarquia de "o que eu quero que o usuário faça aqui"** — cor em tudo (logo, aba ativa, badges, avisos) competindo entre si, sem prioridade. Sintoma: olhar a tela por 5 segundos e não saber onde focar.
19. **Tabs "inset" (padrão shadcn) como navegação de topo do site inteiro** — esse estilo de aba é bom pra alternância local/contextual (ex.: "Preview" vs "Code" dentro de uma mesma tela), não pra trocar de página inteira do produto. Pra navegação de alto nível, preferir sidebar, aba sublinhada, ou um context switcher.
20. **Subheading redundante** — texto explicando o óbvio logo abaixo do heading ("Gerencie suas chaves de API" embaixo de "Chaves de API"). Se o usuário já navegou até a página, o heading sozinho basta.

## Como pensar (nível mais alto, vídeo 2)

21. **Desenhe antes de implementar** — faça o mockup/wireframe (mesmo cru, tudo num arquivo só, sem preocupação com qualidade de código) antes de plugar em schema/banco/endpoint. Começar pela implementação prende a direção cedo demais e dificulta mudar de ideia depois.
22. **Divirja antes de convergir** — gere a mesma tela/ideia em modelos ou ferramentas diferentes, pegue o melhor de cada (uma animação daqui, uma contagem dali) e sintetize a sua própria versão, em vez de aceitar a primeira saída de uma ferramenta só.
23. **Não aceite o default da biblioteca de componentes** — Shadcn/Material/etc. "cru" fica idêntico ao de todo mundo que usa a mesma lib. Ajustar padding, cor, raio de borda, dark/light antes de usar como base é o que diferencia.
24. **Vale investir um pouco em fundamentos de design** — não precisa virar designer, mas entender o "porquê" por trás de "isso ficou ruim" vs "isso ficou melhor" rende muito. Referência citada no vídeo: livro *Refactoring UI* (Adam Wathan).

## Como aplicar (qualquer projeto)

- Antes de mexer em cor/token: identifique a fonte única de cor do projeto (ex.: `colors.ts`, tema do design system, variáveis CSS). Se o "glow"/dot-grid/gradiente decorativo que você quer remover usa um token compartilhado, **não delete o token** se outras telas ainda o usam — confirme com grep antes.
- Revisão de eyebrow/CAPS: olhar padding real no browser, não só o código — é fácil errar por pouco.
- Ícones: não trocar a lib inteira de ícones só por "achar mais original" — troca de biblioteca é custo alto pra ganho estético baixo. Curar o uso pontual (ícone certo pro contexto) resolve o sinal 6, não a lib.
- Fonte: se o projeto já foge da fonte-padrão-de-IA (Inter/Roboto/system), isso é um ativo a **proteger** — não deixar entrar de volta em código novo ou em componentes de terceiros.
- Dot-grid (sinal 25): antes de remover, `grep -rn "background-size" src` pra achar todas as ocorrências de uma vez — costuma estar duplicado em vários arquivos com nomes parecidos (`HeroDots`, `CoverDots`, `XxxDots`). Remova o styled-component inteiro e a linha `<S.XxxDots />` no JSX, não só zere a opacidade.
- Antes de adicionar um card/borda nova (sinais 15 e 17): pergunte se espaçamento + tipografia já resolvem a separação. Card e borda são a última ferramenta, não a primeira.
- Ao desenhar uma tabela/lista com ações por item (sinal 16): comece contando quantas colunas/ícones tem por linha. Mais de 3-4 elementos de ação por linha é sinal de que algo devia estar num menu de contexto.
- Tabs de navegação (sinal 19): pergunte se a aba troca de "página" (rota) ou só alterna conteúdo local. Só o segundo caso justifica o estilo inset.
- Qualquer remoção de decoração ou reestruturação de hierarquia: confirmar visualmente (screenshot via browser real ou Cypress/Playwright temporário) antes de reportar como concluído — slop é visual, não dá pra confirmar só lendo o código.

## Auto-checagem antes de dar como terminado

Percorra os itens 1-20 e 25 na tela que você acabou de tocar. Se bater 2+ itens, não está terminado — corrija ou peça decisão do usuário quando envolver corte de escopo (ex.: trocar lib de ícone, remover token usado em outro lugar, redesenhar navegação, escolher o que substitui uma decoração removida). Os itens 21-24 são hábito de processo, não checklist de tela — revise a cada feature nova, não a cada componente.

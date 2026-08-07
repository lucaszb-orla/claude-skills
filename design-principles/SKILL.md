---
name: design-principles
description: "Princípios de design de interface e padrões de comportamento que valem em qualquer plataforma: web, Android, desktop, CLI, produto. Destilado do Apple HIG (snapshot 2026-08-05) e traduzido para o que é universal, com equivalências concretas para web. Cobre os oito princípios (Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight), feedback, loading, onboarding, modalidade, undo, entrada de dados, mensagens de erro, escrita de UX e acessibilidade. Use ao desenhar ou revisar qualquer interface, ao decidir comportamento de fluxo, ao escrever microcopy, ao avaliar se um design está bom, ou quando o usuário pedir crítica de UX, princípios de design ou orientação que não seja específica de plataforma Apple. Para detalhe de plataforma Apple, usar apple-hig."
---

# Princípios de design de interface

Destilado do Apple Human Interface Guidelines, snapshot de 2026-08-05, separando o que é universal do que é idiossincrático da Apple. A Apple é a fonte porque documenta comportamento com rigor incomum, mas quase tudo abaixo vale igual em web, Android e desktop.

Fonte completa no vault em `~/Documents/Documents/Projetos/megabrain2.0/2-materia-prima/Guias/Apple Human Interface Guidelines/`. Para detalhe específico de plataforma Apple, usar a skill `apple-hig`.

## A premissa

Boas interfaces se apoiam em como as pessoas realmente pensam, sentem e agem, não em como seria elegante que pensassem.

Os princípios abaixo **não resolvem trade-off, eles nomeiam o trade-off**. Não existe um jeito certo de aplicá-los; são ferramentas para pesar prioridades que competem. Quando dois se contradizem num caso concreto, esse conflito é a decisão de design, e é aí que você deve pensar em vez de seguir regra.

## Os oito princípios

A Apple reintroduziu esta página em 2026-06-08. É a espinha dorsal de todo o resto.

### Purpose
- **Crie valor.** Em cada etapa, pergunte para que o produto serve e se o design serve a esse propósito.
- **Mantenha foco.** Priorize as funções mais importantes e faça essas realmente bem.
- **Ache um jeito novo de resolver.** Investigue o que existe e evite recriar. Defina o que te diferencia.

### Agency
- **Saia da frente.** As pessoas usam o produto para fazer algo. Leve direto à tarefa. Os melhores designs são discretos e presentes quando necessário.
- **Deixe explorar.** Sem trancar em fluxos ou modos. Se um fluxo guiado é necessário, deixe pular ou escapar fácil.
- **Ajude a recuperar de erros.** Saber que pode desfazer é o que torna a interface convidativa. Recuperar do inesperado não deve custar tempo nem trabalho.

### Responsibility
- **Seja transparente sobre o que o produto faz e por quê.** Justifique ao pedir permissão. Seja claro sobre que dados coleta e como usa.
- **Proteja a informação das pessoas.** Colete só o necessário. Antecipe como poderia ser mal usada e previna.

### Familiarity
- **Use conceitos que a pessoa já conhece.** Ela traz conhecimento do mundo real e de outros softwares.
- **Mantenha visual e interação consistentes.** Definiu um comportamento, aplique em tudo. Consistência acelera aprendizado e dá confiança.
- **Dê feedback claro.** Sinalize o que está acontecendo, quando controles estão disponíveis e quando conteúdo muda.

### Flexibility
- **Desenhe para todo mundo.** Trate acessibilidade como prioridade desde o início, não como camada final.
- **Preserve o contexto da pessoa.** Conteúdo e controles em posições consistentes e previsíveis. Transições que se explicam.
- **Considere vários métodos de entrada.** Voz, toque, teclado, ponteiro. Mais inputs, mais gente conseguindo usar.

### Simplicity
- **Inclua só o necessário.** Simplicidade não é minimalismo. É foco: o importante por perto, o resto sai de cena.
- **Seja conciso.** O jeito mais simples de dizer costuma ser o mais universal e o mais útil.
- **Estabeleça hierarquia.** Quando forma e função são evidentes, a pessoa sabe como chegar ao resultado.

### Craft
- **Qualidade define o tom.** Cada elemento mostra quanto você se importa.
- **Experimente e itere.** Prototipe cedo, descarte o que não funciona. Teste em condição real.
- **Sustente o acabamento.** Enviar não é a linha de chegada. Design é compromisso contínuo.

### Delight
- **Saiba que emoção quer provocar.** Um app de fitness energiza, um de meditação acalma. Deixe isso guiar o design.
- **Crie momentos definidores.** De um toque de botão a uma mensagem de erro, cada momento pode carregar caráter.
- **Não confunda delight com decoração.** A pessoa está tentando fazer algo. Encanto pelo encanto atravessa o propósito.
- **Considere o todo.** Delight é a soma do cuidado, não um efeito colado no fim.

## Padrões de comportamento universais

Regras destiladas do HIG, todas aplicáveis fora do ecossistema Apple.

### Feedback
- Alerta só para o que é crítico e, de preferência, acionável. Alerta banal treina a pessoa a ignorar alerta.
- Avise **antes** de uma ação causar perda de dados inesperada e irreversível.
- Confirme conclusão quando a ação foi significativa.
- Quando um comando não pode ser executado, mostre isso **e explique por quê**. "Falhou" sozinho é inútil.
- Prefira integrar status na própria interface a interromper com diálogo.
- Todo feedback precisa ser acessível, não só visual.

### Carregamento e espera
- Mostre algo o quanto antes. Tela vazia por segundos é a pior opção.
- Deixe a pessoa fazer outra coisa enquanto espera.
- Comunique que está carregando **e quanto pode demorar**.
- Se a espera é inevitavelmente longa, dê algo interessante para ver.
- Baixe ativos grandes em background.

### Onboarding
- **Ensine por interatividade**, não por carrossel de texto.
- Prefira dicas contextuais a um fluxo único no começo.
- Se houver tutorial separado, faça opcional.
- Adie setup e customização não essenciais.
- Não coloque licenciamento nem termos no meio do onboarding.
- Deixe a pessoa experimentar antes de pedir avaliação ou compra.
- Peça permissão com justificativa clara, no contexto de uso. Se o produto não funciona sem, integre ao onboarding.

### Modalidade e interrupção
- Modal só quando há benefício claro.
- Tarefa modal deve ser simples, curta e direta.
- Nunca um app dentro do app: se o modal tem navegação própria e profundidade, virou outra coisa.
- **Sempre** uma saída óbvia.
- Confirme antes de fechar se houver risco de perder trabalho.
- Deixe fechar um modal antes de abrir outro. Modal em cima de modal é sinal de fluxo mal desenhado.

### Desfazer
- Deixe a pessoa prever o resultado do undo. Nomeie a operação: "Desfazer excluir 3 itens", não "Desfazer".
- Mostre o resultado do undo.
- Permita desfazer várias vezes.
- Não redefina gestos e atalhos padrão de undo da plataforma.

### Entrada de dados
- **Pegue do sistema o que puder** em vez de pedir.
- Seja claro sobre que dado você precisa e por quê.
- Ofereça escolha em vez de digitação quando possível.
- Aceite colar e arrastar.
- **Valide dinamicamente**, não só no submit.
- Deixe evidente o que é obrigatório antes da pessoa tentar avançar.
- Nunca pré-preencha campo de senha.

### Busca
- Se busca é importante, dê a ela posição primária.
- Um único lugar para buscar todo o conteúdo.
- Deixe claro o escopo atual da busca.
- Ofereça sugestões.
- Pense em privacidade antes de exibir histórico de busca.

## Escrita de interface

- **Defina a voz do produto** e ajuste o tom ao contexto. Erro grave não é lugar de piada.
- **Seja orientado a ação.** Botão diz o que faz, não "OK".
- **Construa padrões de linguagem** e reaplique. A mesma coisa com o mesmo nome, sempre.
- **Escreva mensagens de erro claras**: o que aconteceu, por quê, e o que fazer agora.
- **Toda tela vazia precisa de próximo passo claro.** Estado vazio é oportunidade, não acidente.
- **Considere o propósito de cada tela** antes de escrever o texto dela.
- Labels de configuração claros e simples.
- Dicas dentro de campos de texto, quando ajudam.
- Use pronomes possessivos com parcimônia.
- Adote regras de capitalização e aplique consistentemente.

Inclusão na escrita:
- Considere o tom sob perspectivas diferentes da sua.
- Preste atenção em como você se refere a pessoas.
- Não use termo técnico sem definir.
- Troque expressão coloquial por linguagem simples. Coloquialismo é o que pior sobrevive a tradução.
- Pense duas vezes antes de humor.
- Ao falar de pessoas com deficiência, abordagem people-first.
- Evite imagens e linguagem que excluem pessoas com deficiência.

## Acessibilidade, o mínimo universal

- **Contraste:** 4.5:1 para texto corrido. 3:1 para texto grande ou bold. Este é o número do WCAG AA, vale em qualquer lugar.
- **Nunca só cor** para transmitir informação, indicar interatividade ou diferenciar objetos.
- **Alvos grandes o suficiente, e espaçados.** Espaçamento entre controles importa tanto quanto o tamanho deles.
- **Texto maior deve funcionar.** Nada de container de altura fixa que corta texto ampliado.
- **Teclado sozinho** deve navegar e operar tudo.
- **Descreva interface e conteúdo** para leitor de tela.
- **Alternativa para todo gesto.** Gesto complexo nunca é o único caminho.
- **Legenda e transcrição** para áudio e vídeo.
- **Cuidado com animação rápida ou piscante.** Deixe optar por não ver flashes.
- **Minimize elemento com tempo limitado.** Se há timeout, deixe estender.
- **Pistas redundantes:** som mais visual, háptico mais som.
- Deixe controlar playback de áudio e vídeo.

## Traduzindo para web

Os conceitos do HIG têm equivalente direto em web. Use o equivalente, não a imitação:

| Conceito Apple | Equivalente web |
|---|---|
| Dynamic Type | `rem` em vez de `px`, e nada de `max-height` fixo em bloco de texto |
| Reduce Motion | `@media (prefers-reduced-motion: reduce)` |
| Increase Contrast | `@media (prefers-contrast: more)` |
| Dark Mode | `@media (prefers-color-scheme: dark)` |
| Cores semânticas do sistema | Design tokens em CSS custom properties, nunca hex espalhado |
| VoiceOver | HTML semântico primeiro, ARIA só onde o HTML não alcança |
| Alvo de 44 pt | 44 px CSS de área clicável, WCAG 2.5.5 |
| Restaurar estado | URL como estado. Toda view relevante deve ser linkável |
| SF Symbols | Um único set de ícones, com peso e alinhamento óptico coerentes |
| Spotlight | Busca no site mais dados estruturados para busca externa |
| Views de sistema para abrir e salvar | `<input type="file">` e as APIs nativas, não uploader custom |
| Controles nativos | Elementos nativos (`<select>`, `<dialog>`, `<details>`) antes de recriar em div |

Duas coisas que web tem e Apple não precisa documentar, mas que valem o mesmo rigor: **URL é estado** (se não dá para linkar, você quebrou Agency) e **o back do navegador é o undo mais usado da web** (se ele destrói trabalho, você quebrou Agency de novo).

## O que NÃO transportar da Apple

Não trate como universal:

- **Liquid Glass, translucidez e blur.** Estética de plataforma. Em web custa performance e costuma sair mal.
- **Números de tamanho de controle por plataforma.** O 44 pt tem análogo no WCAG; os de tvOS e watchOS não têm.
- **Posição de navegação.** Tab bar embaixo é convenção de iOS, não regra de interface. Web tem outra.
- **Gestos específicos.** Swipe de volta, Digital Crown, force touch: existem porque o hardware existe.
- **Menu bar, Dock, Control Center** e outros pontos de integração de sistema.
- **Regras de App Store.** Não são design, são contrato de distribuição.
- **A preferência por "o sistema resolve".** Excelente na Apple, onde há um sistema. Em web o "sistema" é o navegador e o que ele oferece é bem menor. Não conclua que existe API nativa só porque na Apple existe.

## Como aplicar numa crítica de design

Ordem que costuma achar os problemas maiores primeiro:

1. **Purpose.** Para que serve esta tela? Se não dá para responder em uma frase, o resto não importa.
2. **Hierarquia.** O que é mais importante parece mais importante?
3. **Agency.** A pessoa consegue sair, pular, desfazer? Onde ela fica presa?
4. **Familiarity.** Algo aqui se comporta diferente do que aparenta?
5. **Feedback.** Toda ação tem resposta? Todo erro explica o que fazer?
6. **Flexibility.** Funciona com texto grande, teclado, leitor de tela, sem cor?
7. **Simplicity.** O que dá para tirar sem perder função?
8. **Craft e Delight.** Só depois dos anteriores. Acabamento em cima de fluxo quebrado é maquiagem.

Ao criticar, diga qual princípio está sendo violado e qual é o custo concreto para a pessoa que usa. "Viola Agency" sozinho não ajuda; "não tem como cancelar depois de começar, então quem errar precisa recomeçar do zero" ajuda.

## Regras de trabalho

- Ao afirmar uma regra vinda do HIG, é honesto dizer de onde vem. As notas estão no vault em `2-materia-prima/Guias/Apple Human Interface Guidelines/`.
- O snapshot é de 2026-08-05 e a revisão mais recente da fonte é 2026-06-08. Princípios envelhecem devagar, mas confira a fonte para detalhe.
- Princípio não substitui teste com pessoa de verdade. Quando a decisão é caríssima ou controversa, o certo é dizer que precisa de pesquisa, não escolher o princípio que confirma a preferência de quem pergunta.

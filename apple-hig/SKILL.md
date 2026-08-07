---
name: apple-hig
description: "Orientação de design para plataformas Apple (iOS, iPadOS, macOS, tvOS, visionOS, watchOS), destilada do Human Interface Guidelines em snapshot de 2026-08-05. Cobre Liquid Glass, o que muda entre plataformas, tamanhos mínimos de controle, contraste, Dynamic Type, SF Symbols e escolha de componente de navegação. Use ao desenhar, revisar ou implementar interface para qualquer plataforma Apple, ao decidir entre tab bar e sidebar, ao aplicar materiais e translucidez, ao portar um app entre plataformas Apple, ou quando o usuário mencionar HIG, Apple design, SwiftUI/UIKit de UI, iOS design ou Liquid Glass. Para princípios universais que valem também em web e Android, usar design-principles."
---

# Apple HIG

Destilado do Human Interface Guidelines, snapshot de 2026-08-05. O guia completo (173 notas, 250 mil palavras, texto original da Apple) está no vault em `~/Documents/Documents/Projetos/megabrain2.0/2-materia-prima/Guias/Apple Human Interface Guidelines/`, com índice em `3-marcadores/MOC - Apple HIG.md`. **Leia a nota específica no vault antes de decidir qualquer detalhe.** Esta skill é o mapa, não o território.

Para os oito princípios de design e os padrões de comportamento que valem em qualquer plataforma, usar a skill `design-principles`. Esta aqui cobre só o que é idiossincrático da Apple.

## Antes de qualquer coisa: qual plataforma

O erro mais comum é desenhar "para Apple". Não existe. Cada plataforma tem ergonomia, input e expectativa diferentes. Estabeleça a plataforma alvo antes de opinar sobre layout ou componente. Se o usuário não disse, pergunte.

| Plataforma | Distância e postura | Input primário | Consequência de design |
|---|---|---|---|
| iOS | Uma mão, polegar, em movimento | Toque | Ações importantes na metade de baixo. Sessões curtas e interrompíveis. |
| iPadOS | Duas mãos, apoiado, sessão longa | Toque, Pencil, teclado, trackpad | Layouts multi-coluna, sidebar, multitarefa real. |
| macOS | Sentado, foco longo, múltiplas janelas | Ponteiro e teclado | Densidade maior, menu bar, atalhos, janelas redimensionáveis. |
| tvOS | Sala, 3 metros, em grupo | Foco direcional no remote | Nada de toque. Tudo por foco. Texto e alvos grandes. |
| visionOS | Espaço 3D, passthrough | Olhos e mãos | Conforto acima de tudo. Profundidade real, sem movimento na periferia. |
| watchOS | Pulso, olhada de 2 segundos | Toque, Digital Crown | Uma tarefa por tela. Sem indicador de progresso indeterminado. |

Cada plataforma tem sua nota `HIG - Designing For X` no vault, com as seções Display, Ergonomics, Inputs, App interactions e System features.

## Liquid Glass

Material introduzido em 2025 e revisado em 2026, que unificou a linguagem visual entre as plataformas. É o que mais data um design feito antes de meados de 2025. Regras, verbatim da Apple:

- **Não use Liquid Glass na camada de conteúdo.** Ele existe para separar controles e navegação do conteúdo. Usar no conteúdo produz hierarquia confusa. Exceção: controles com elemento interativo transitório, como sliders e toggles.
- **Use com parcimônia.** Efeito demais anula a hierarquia que ele deveria criar.
- **Liquid Glass "clear" só sobre fundos visualmente ricos.**
- **Escolha material por significado semântico**, não por aparência.
- **Garanta legibilidade com cores vibrantes sobre o material.**
- **Prefira translucidez a cor opaca em janelas.**
- Para elementos da camada de conteúdo, use **materiais padrão**, não Liquid Glass.

Detalhe completo em `HIG - Materials`. Se o trabalho envolve aparência de barra, sidebar ou controle flutuante, leia essa nota inteira.

## Números que não se negocia

Tamanho de controle, direto da tabela do HIG:

| Plataforma | Padrão | Mínimo |
|---|---|---|
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

Contraste mínimo (WCAG AA, o que o Accessibility Inspector usa):

| Tamanho do texto | Peso | Mínimo |
|---|---|---|
| Até 17 pt | Qualquer | 4.5:1 |
| 18 pt | Qualquer | 3:1 |
| Qualquer | Bold | 3:1 |

Espaçamento entre controles conta tanto quanto o tamanho: cerca de **12 pt** de padding em elementos com bezel, cerca de **24 pt** sem bezel.

tvOS tem margens próprias: conteúdo primário a **60 pt** do topo e base, **80 pt** das laterais, e centros de botão a pelo menos 60 pt entre si.

## O que a plataforma já resolve, e você não deve reimplementar

Isto é onde a maioria do esforço se desperdiça. Em todos os casos, o caminho é usar o sistema:

- **Cor.** Nunca hardcode valores de cor de sistema. Nunca redefina o significado semântico de uma cor dinâmica. Cores semânticas já se adaptam a claro, escuro e alto contraste.
- **Tipografia.** Use os estilos de texto do sistema e suporte Dynamic Type. Peso da fonte afeta legibilidade tanto quanto tamanho.
- **Ícones.** SF Symbols acompanha peso, alinhamento óptico e Dynamic Type do texto ao lado. Ícone custom só quando não existe símbolo equivalente.
- **Controles de cor.** Se o app deixa a pessoa escolher cor, prefira o controle do sistema.
- **Abrir e salvar arquivo.** Use as views do sistema.
- **Undo e redo.** Comandos no menu Edit e atalhos padrão. Não redefina os gestos padrão.
- **Busca.** Torne o conteúdo pesquisável no Spotlight, não só dentro do app.

Se você está escrevendo código para replicar um desses, pare e verifique a API do sistema primeiro.

## Escolha de navegação

**Não trate tab bar e sidebar como escolha binária.** O HIG é explícito: para muitos apps você não precisa escolher, existe um estilo de tab bar que oferece os dois. Se você está debatendo "tab bar ou sidebar", provavelmente está resolvendo o problema errado. Leia `HIG - Sidebars` e `HIG - Tab Bars` antes de decidir.

O que a fonte estabelece:

- **Tab bar serve navegação, não ação.** Alternar entre seções do app, preservando o estado de navegação de cada uma. Se você precisa de controles que agem sobre o conteúdo atual, tab bar é o lugar errado.
- **Sidebar exige muito espaço** vertical e horizontal. Onde o espaço é limitado, ou onde você quer dar a tela ao conteúdo, um controle mais compacto costuma servir melhor.
- **Split view** quando lista e detalhe convivem. Base do iPadOS e macOS.
- Ao portar entre plataformas, a estrutura de navegação é a primeira coisa que muda. Não transporte tab bar de iPhone para Mac.

Grupos de componentes no vault, dentro de `4 - Components/`: Layout and organization, Content, Menus and actions, Navigation and search, Presentation, Selection and input, Status, System experiences.

## Padrões que a Apple trata como obrigatórios

- **Launch.** Tela de lançamento quase idêntica à primeira tela real, **sem texto**. Restaure o estado anterior. Não transforme o launch em espetáculo.
- **Onboarding.** Ensine por interatividade, não por tela de texto. Prefira dicas contextuais a um fluxo único. Se houver tutorial separado, torne opcional. Adie setup não essencial. Não coloque licenciamento no onboarding.
- **Permissões.** Peça no contexto, com justificativa clara. Se o app não funciona sem, integre ao onboarding.
- **Modalidade.** Só quando há benefício claro. Sempre com saída óbvia. Confirme antes de fechar se houver risco de perda de dados. Nunca um app dentro do app.
- **Feedback.** Alertas só para o que é crítico e acionável. Avise antes de perda de dados irreversível e inesperada. Quando um comando falha, explique por quê.
- **Loading.** Mostre algo o quanto antes. Deixe a pessoa fazer outra coisa enquanto espera. Em watchOS, evite indicador indeterminado.

## Revisão: o que checar

1. Plataforma alvo declarada, e o layout respeita a ergonomia dela
2. Nenhum uso de Liquid Glass na camada de conteúdo
3. Alvos de toque no mínimo da plataforma, com espaçamento adequado
4. Contraste ≥ 4.5:1 para texto até 17 pt
5. Dynamic Type suportado, nada de tamanho fixo em ponto
6. Cores semânticas do sistema, nada de hex hardcoded para cor de sistema
7. Testado em claro, escuro e alto contraste
8. Informação nunca transmitida só por cor
9. Movimento respeita Reduce Motion e é cancelável
10. Navegação apropriada à plataforma, não portada de outra
11. VoiceOver descreve interface e conteúdo
12. Navegação completa só por teclado (relevante em macOS e iPadOS)

## Regras de trabalho

- **Cite a nota do vault** quando afirmar uma regra do HIG, por exemplo `HIG - Materials`. Se a afirmação não está no vault nem na fonte, diga que é sua opinião, não HIG.
- **Confira a data.** Cada nota tem `apple_atualizado` no frontmatter. A revisão mais recente do guia é 2026-06-08. A Apple revisa em junho, junto com a WWDC. Se hoje for muito depois disso, avise que o snapshot pode estar velho e a fonte canônica é `developer.apple.com/design/human-interface-guidelines`.
- **HIG não é App Review.** O HIG não tem força contratual. Rejeição na App Store vem das App Review Guidelines, que são outro documento. Não confunda os dois ao dizer que algo "é proibido".
- **O HIG defende a plataforma, não o produto do usuário.** Quando ele quiser contrariar o guia por diferenciação, diga o custo com clareza e siga. Não trate o HIG como lei moral.

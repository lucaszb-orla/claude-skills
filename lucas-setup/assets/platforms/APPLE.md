# Orientação para iOS e macOS

- Prefira Swift, SwiftUI e APIs nativas quando atenderem ao requisito.
- Registre deployment target, versões de Xcode e Swift e destinos no contexto.
- Altere a fonte declarativa e regenere o projeto quando usar XcodeGen ou Tuist.
- Descubra `BUILT_PRODUCTS_DIR` com `xcodebuild -showBuildSettings`.
- Mantenha assinatura estável em fluxos com permissões do sistema.
- Não fixe IDs de time, bundle IDs ou entitlements na configuração genérica.
- Siga os padrões específicos de iOS ou macOS.
- Suporte VoiceOver, teclado, foco, texto dinâmico e Reduzir Movimento.
- Prefira String Catalogs em projetos modernos.
- Não fixe `Locale` na árvore da interface.
- Confirme emissão e sincronização dos dados de localização em projetos gerados.
- Não trate cancelamento cooperativo como interrupção imediata.
- Não use task group como timeout quando um filho puder nunca retornar.
- Drene ou redirecione os streams de `Process`.
- Solicite permissões no contexto de uma ação compreensível.
- Separe permissões essenciais de integrações opcionais.
- Documente onde os dados ficam e se saem do dispositivo.
- Valide build, testes, assinatura, entitlements, localização e acessibilidade.

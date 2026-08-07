# Orientação para projetos web

- Detecte framework, runtime e gerenciador pelo manifesto e lockfile.
- Mantenha o servidor configurável por variável ou argumento.
- Não compartilhe porta, banco, cache ou Docker entre workspaces sem isolamento.
- Nunca envie segredos ao bundle do cliente.
- Use HTML semântico e controles nativos antes de simular comportamento.
- Garanta teclado, foco visível, nomes acessíveis e contraste adequado.
- Modele carregamento, vazio, erro, retry e dados parciais.
- Valide entrada no servidor, mesmo quando o cliente já valida.
- Implemente responsividade para conteúdo real.
- Evite páginas genéricas compostas apenas de cartões iguais.
- Valide o fluxo em navegador real, console, rede e viewports pequeno e grande.

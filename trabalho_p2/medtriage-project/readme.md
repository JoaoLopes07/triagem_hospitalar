Funcionalidade: Classificação de Risco de Pacientes

  Cenário: Paciente com saturação de oxigênio crítica
    Dado que o paciente possui uma saturação de oxigênio de 80%
    E uma frequência cardíaca de 130 bpm
    Quando a triagem for executada utilizando o Protocolo de Manchester
    Então o sistema deve definir a cor do risco como "VERMELHO"
    E alterar o status do atendimento para "CLASSIFICADO"

Evidências de Clean Code: Código altamente legível, com nomenclatura autoexplicativa para funções e variáveis, eliminação de estruturas redundantes e ausência total de comentários poluidores.

Aplicação dos Princípios SOLID:

SRP: Cada classe possui uma única função dentro do ecossistema.

OCP: O comportamento das classificações pode ser estendido com novas estratégias sem alterar o código existente.

LSP: O repositório em memória pode ser facilmente substituído por um banco real através da interface.

ISP: Clientes da interface não são forçados a depender de métodos que não utilizam.

DIP: A lógica de aplicação depende puramente de interfaces abstratas, isolando o núcleo de dependências de infraestrutura externa.

Design Patterns Implementados: Strategy (regras de Manchester), Repository (abstração de dados), Injeção de Dependência (via construtores) e Data Transfer Object (estruturação de payloads JSON).

Link de Acesso ao Sistema: https://medtriage-tcc.render.com (Substitua pela sua URL após realizar o upload do repositório no Render, Railway ou plataforma de sua preferência)
# MedTriage System - Sistema de Triagem Hospitalar

O MedTriage é uma solução de software projetada para automatizar o fluxo de classificação de risco em prontos-socorros com base no Protocolo de Manchester. O sistema foi desenvolvido dividindo as responsabilidades em microsserviços independentes, aplicando conceitos de Arquitetura Limpa, princípios SOLID, Design Patterns, TDD e BDD.

## Links do Sistema Publicado (Render)

* **Microsserviço de Triagem (Triage-Service):** https://triagem-hospitalar-k0li.onrender.com
* **Microsserviço de Pacientes (Patient-Service):** https://triagem-hospitalar-ts8q.onrender.com

---

## 1. Estrutura do Projeto (Arquitetura Limpa)

A solução adota os pilares da Clean Architecture para isolar as regras de negócio de detalhes de infraestrutura e frameworks web.

```text
medtriage-project/
├── docker-compose.yml
├── patient-service/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
└── triage-service/
    ├── Dockerfile
    ├── requirements.txt
    ├── app.py
    ├── test_triage.py
    └── src/
        ├── core/
        │   ├── domain/
        │   │   └── entities.py
        │   └── usecases/
        │       ├── interfaces.py
        │       └── perform_triage.py
        └── infrastructure/
            └── database/
                └── repository.py

2. Divisão em Microsserviços
O ecossistema foi descentralizado em duas APIs independentes que operam isoladas:

Patient-Service (Porta 8001): Responsável pela ingestão, armazenamento demográfico e busca de dados dos pacientes.

Triage-Service (Porta 8002): Core do sistema que processa os sinais vitais, executa o motor de regras clínicas e gera a ordem de prioridade.

3. Princípios SOLID Aplicados
SRP (Single Responsibility Principle): Cada classe possui escopo único. A entidade Triage gerencia o estado clínico do atendimento, enquanto as classes de estratégia decidem os limites de pontuação de risco.

OCP (Open/Closed Principle): O motor de triagem usa polimorfismo. Se houver mudanças nas regras de negócio ou adoção de novos protocolos (como a classificação da OMS), basta estender a classe base sem alterar os casos de uso existentes.

LSP (Liskov Substitution Principle): O adaptador de persistência em memória MemoryTriageRepository herda e respeita integralmente o contrato estabelecido pela interface abstrata de domínio.

ISP (Interface Segregation Principle): As interfaces contêm apenas os métodos estritamente necessários para a execução daquele contexto técnico.

DIP (Dependency Inversion Principle): A lógica de aplicação nos Casos de Uso depende de abstrações e interfaces, nunca de implementações diretas de infraestrutura ou do framework Flask.

4. Design Patterns Utilizados
Strategy Pattern: Centraliza as regras de negócio variáveis do Protocolo de Manchester, isolando as condicionais de avaliação de sinais vitais.

Repository Pattern: Cria uma camada de abstração para o acesso a dados, desacoplando o núcleo da aplicação do mecanismo físico de persistência.

Injeção de Dependência: Utilizada via construtores para fornecer instâncias de infraestrutura para a camada de regras de aplicação sem acoplamento rígido.

Data Transfer Object (DTO): Empregado na recepção de payloads JSON nas rotas HTTP do Flask para tipificar e organizar os dados de entrada.

5. Cenários de Comportamento (BDD)
Gherkin


Funcionalidade: Classificação de Risco de Pacientes

  Cenário: Paciente com saturação de oxigênio crítica
    Dado que o paciente possui uma saturação de oxigênio de 80%
    E uma frequência cardíaca de 130 bpm
    Quando a triagem for executada utilizando o Protocolo de Manchester
    Então o sistema deve definir a cor do risco como "VERMELHO"
    E alterar o status do atendimento para "CLASSIFICADO"
6. Testes Automatizados (TDD)
Os testes foram escritos guiados por comportamento e podem ser executados nativamente com o módulo unittest do Python.

Como executar os testes locais:
Bash


cd trabalho_p2/medtriage-project/triage-service
python -m unittest test_triage.py
7. Configuração do Ambiente (Docker Compose)
O ambiente produtivo é orquestrado de forma automatizada por containers. Para inicializar a aplicação localmente com Docker, execute o comando na raiz do projeto:

Bash


docker compose up --build
8. Justificativa Técnica
A separação em microsserviços garante que instabilidades causadas por alta demanda de cadastros na recepção do hospital (patient-service) não afetem o motor crítico de triagem de pacientes em atendimento de emergência (triage-service). A escolha da Arquitetura Limpa garante manutenibilidade a longo prazo, permitindo que a camada de persistência em memória utilizada nesta versão seja substituída por bancos relacionais como PostgreSQL sem a necessidade de reescrever ou alterar as regras de negócio clínicas da aplicação.

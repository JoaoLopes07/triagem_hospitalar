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

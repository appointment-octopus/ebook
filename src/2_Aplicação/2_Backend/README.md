# Resumão Backend

Nesse capítulo você terá um resumo sobre a ideia do backend, estruturado como microsserviços, e vamos explicar também cada microsserviço contido dentro do projeto.

- [Resumão Backend]()
  - [Microsserviços](#Microsserviços)
    - [Appointments](#Appointments)
    - [Licença](#Licença)
    - [Use Cases](#Use-Cases)

## Microsserviços

Diferentemente de uma arquitetura moldada em um software monolítico (uma aplicação onde todos os processos estão acoplados em um único lugar), optamos por uma organização de desenvolvimento estruturada em microsserviços, onde cada pequeno serviço tem sua responsabilidade independente e se comunicam utilizando de APIs que são bem definidas. Dessa forma facilita designar a responsabilidade de cada serviço a pequenas equipes que conseguem se autogerir.

> "As arquiteturas de microsserviços facilitam a escalabilidade e agilizam o desenvolvimento de aplicativos, habilitando a inovação e acelerando o tempo de introdução de novos recursos no mercado." <br /> fonte: https://aws.amazon.com/pt/microservices/

Entretanto, não seguimos 100% a risca: utilizamos um unico banco de dados para todos os serviços.

### Appointments

https://github.com/appointment-octopus/appointments

É o nosso microsserviço responsável por todo o CRUD (*Create*, *Read*, *Update* e *Delete* ) das consultas. É possível ver as consultas de um usuário (tanto as que passaram, como as que ainda acontecerão) e, também, listar horários disponíveis para agendar.

Stack: Javascript + Express.js + Sequelize + Jest

### Auth

Microsserviço responsável pela autenticação do usuário. Cria usuário, faz login (e gera um token jwt), logout etc.

Stack: Go + mux + Gorm + redigo (cache do usuário)

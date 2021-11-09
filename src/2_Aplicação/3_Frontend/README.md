# Resumão Frontend

Nesse capítulo você terá um resumo sobre a ideia do Frontend, que se encontra como um microsserviço no nosso projeto.

- [Resumão Frontend]()
  - [Front](#Front)
    - [UserApp](#UserApp)

## Front

Nosso Frontend no início tinha o objetivo de ser composto por um aplicativo de usuário, e por um de adminitrador.

O de usuário (UserApp), consistia em:

 - login;
 - navegação;
 - escolha do tipo de consulta;
 - adicionar métodos de pagamento;
 - agendamento da consulta propriamente dito.

Quanto ao de administrador, iria "liberar" dias possíveis juntamente com seus horários para as consultas poderem ser realizadas.

Devido ao escopo que propomos e até onde conseguimos produzir, o único que foi 'planejado e construído', ao menos de forma visual foi o app de Usuário.

### UserApp

Microsserviço responsável pela parte visual, logo o nosso Frontend. Como nos propomos a desenvolver uma aplicação mobile utilizamos *React Native*, como *framework*, e com o auxílio do *StoryBook* que é uma ferramenta *open source* para construção de componentes de interface, e o desenvolvimento de páginas.


# Backend

Para interagir com o backend, em geral, é mais indicado utilizar [Postman](https://www.postman.com/) ou [Insomnia](https://insomnia.rest/)

Ambas as ferramentas são utilizadas para fazer requisições http; dessa forma, para testar alguma rota especifica do backend, não será necessário, por exemplo, navegar nas telas do frontend até chegar no botão X que faz uma requisição especifica em alguma rota do backend.
Não é necessário, também, ir ao mais "baixo nível" que seria utilizando o comando `curl` e afins.

Exemplificando:

1. Crie um novo **request** no Postman
![postman_new_request](../../Imagens/postman_new_request.png)

2. Preencha as informações:
```
url = https://localhost:3000/api/users/
tipo = POST
body = raw, json
```
```json
{
    "user": {
        "email": "john@jacob.com",
        "password": "johnnyjacob",
        "username": "johnjacob"
    }
}
```

![postman_post_users](../../Imagens/postman_post_users.png)

Para entender melhor esse request, vamos verificar como está especificada a criação de usuários no backend.

Abra `backend/routes/api/users.js(L63-73)`:
![backend_users](../../Imagens/backend_users.png)

Perceba que `user` é uma instância da model `User`:
Em `backend/routes/api/users.js(L4)`
![backend_user_model_users_route](../../Imagens/backend_user_model_users_route.png)

Para entendermos o que é essa model,

Abra `backend/models/Users.js`:

Não precisamos nos aprofundar muito, mas, de acordo com o código visto acima, há 3 trechos relevantes:

Schema:
![user_schema](../../Imagens/user_schema.png)

Set Password:
![user_schema_set_password](../../Imagens/user_schema_set_password.png)
> é recomendada a pesquisa sobre `pbkdf2`, `bcrypt`, `sha512`, `salt`, `pepper` no contexto de criptografia :)
> mas, basicamente trata-se de uma segurança a mais para armazenar as senhas dos usuários
> dificultando que *hackers* consigam "adivinhar" a senha dos usuários (seja através de *bruteforce* ou de *"ataques rainbow table"*)

To Auth Json:
![user_schema_to_auth_json](../../Imagens/user_schema_to_auth_json.png)

Com isso tudo, podemos inferir bastante sobre o funcionamento do request que fizemos:
A api recebe nosso request (incluindo o corpo de texto [em formato json] com informações de cadastro do usuário), valida se o `username`, `email` e `password` atendem as especificações do `Schema` (por ex: não podemos cadastrar "abc" como email), a senha é criptografada e, então, o usuário é salvo no banco de dados Mongo;
Caso tudo tenha ocorrido corretamente, o servidor responde o request do usuário mostrando informações básicas de como o usuário foi cadastrado no banco de dados.
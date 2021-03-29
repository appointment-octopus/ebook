# Projeto completo em Javascript

Este tutorial têm como objetivo:

- Elucidar melhor como funciona a arquitetura Cliente-Servidor
- Demonstrar como preparar o ambiente da sua máquina
- Demonstrar como funciona a estrutura de um projeto Javascript
- Conseguir fazer uma interação completa entre o front, back e banco

Se trata de uma aplicação de mundo real, baseada no [Medium](http://medium.com/): [https://demo.realworld.io/#/](https://demo.realworld.io/#/)
Pode encontrar mais informações sobre esse projeto [aqui](https://github.com/gothinkster/realworld).

| Projeto | Stack | Url do projeto |
| ------- | ----- | -------------- |
| [Backend](#backend) | Node.js, Express, MongoDB | [https://github.com/gothinkster/node-express-realworld-example-app](https://github.com/gothinkster/node-express-realworld-example-app) |
| [Frontend](#frontend) | React, Redux | [https://github.com/gothinkster/react-redux-realworld-example-app](https://github.com/gothinkster/react-redux-realworld-example-app) |


## Instalação

### Clonar repositórios

```bash
$ mkdir conduit
```

```bash
$ cd conduit
```

```bash
$ git clone https://github.com/gothinkster/node-express-realworld-example-app backend
```

```bash
$ git clone https://github.com/gothinkster/react-redux-realworld-example-app frontend
```

### Instalar MongoDB

MongoDB é um SGBD (Sistema Gerenciador de Banco de Dados) orientado a Documentos, sendo categorizado como `NoSql`. 

```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
```

```bash
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
```

```bash
$ sudo apt update
```

```bash
$ sudo apt-get install -y mongodb-org
```

```bash
$ sudo systemctl start mongod
```

```bash
$ sudo systemctl status mongod
```

```bash
$ sudo mkdir -p /data/db
```

```bash
$ sudo chown -R `id -u` /data/db
```

```bash
$ mongod
```

### Istalar NPM e Yarn

São gerenciadores de pacotes Javascript, portanto, utilizados para instalar bibliotecas externas. 

- `npm` = gerenciador padrão
- `yarn` = surgiu com algumas otimizações em relação ao `npm`, sendo normalmente mais rápido

> *hoje em dia há quem argumente que ambos estão em pé de igualdade* 

```bash
$ sudo apt install nodejs npm
```

```bash
$ npm install --global yarn
```

## Entendendo estrutura dos projetos

Felizmente, é bem simples de se abstrair o funcionamento de qualquer projeto JS: caso o `README.md` não providencie todas as informações necessárias, basta começar a ler pelo `package.json` :D

*A partir da pasta "conduit":*

```bash
$ tree -L 2
.
├── backend
│   ├── app.js
│   ├── config
│   ├── models
│   ├── package.json
│   ├── project-logo.png
│   ├── public
│   ├── README.md
│   ├── routes
│   ├── tests
│   └── yarn.lock
└── frontend
    ├── package.json
    ├── project-logo.png
    ├── public
    ├── README.md
    ├── src
    └── yarn.lock

9 directories, 9 files
```


### Package.json

Antes de começarmos a ler de fato ambos os `package.json`, vamos ver a similaridade destes:

`backend/package.json`:

```json
{
  "name": "conduit-node",
  "version": "1.0.0",
  "description": "conduit on node",
  "main": "app.js",
  "scripts": {
    "mongo:start": "docker run --name realworld-mongo -p 27017:27017 mongo & sleep 5",
    "start": "node ./app.js",
    "dev": "nodemon ./app.js",
    "test": "newman run ./tests/api-tests.postman.json -e ./tests/env-api-tests.postman.json",
    "stop": "lsof -ti :3000 | xargs kill",
    "mongo:stop": "docker stop realworld-mongo && docker rm realworld-mongo"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/gothinkster/productionready-node-api.git"
  },
  "license": "ISC",
  "dependencies": {
    "body-parser": "1.15.0",
    "cors": "2.7.1",
    "ejs": "2.4.1",
    "errorhandler": "1.4.3",
    "express": "4.13.4",
    "express-jwt": "3.3.0",
    "express-session": "1.13.0",
    "jsonwebtoken": "7.1.9",
    "method-override": "2.3.5",
    "methods": "1.1.2",
    "mongoose": "4.4.10",
    "mongoose-unique-validator": "1.0.2",
    "morgan": "1.7.0",
    "passport": "0.3.2",
    "passport-local": "1.0.0",
    "request": "2.69.0",
    "slug": "0.9.1",
    "underscore": "1.8.3"
  },
  "devDependencies": {
    "newman": "^3.8.2",
    "nodemon": "^1.11.0"
  }
}
```


`frontend/package.json`:
```json
{
  "name": "react-redux-realworld-example-app",
  "version": "0.1.0",
  "private": true,
  "devDependencies": {
    "cross-env": "^5.1.4",
    "react-scripts": "1.1.1"
  },
  "dependencies": {
    "history": "^4.6.3",
    "marked": "^0.3.6",
    "prop-types": "^15.5.10",
    "react": "^16.3.0",
    "react-dom": "^16.3.0",
    "react-redux": "^5.0.7",
    "react-router": "^4.1.2",
    "react-router-dom": "^4.1.2",
    "react-router-redux": "^5.0.0-alpha.6",
    "redux": "^3.6.0",
    "redux-devtools-extension": "^2.13.2",
    "redux-logger": "^3.0.1",
    "superagent": "^3.8.2",
    "superagent-promise": "^1.1.0"
  },
  "scripts": {
    "start": "cross-env PORT=4100 react-scripts start",
    "build": "react-scripts build",
    "test": "cross-env PORT=4100 react-scripts test --env=jsdom",
    "eject": "react-scripts eject"
  }
}
```

Bom, fora o trivial (como `name`, `version`, `description` etc), o que salta aos olhos são: `dependencies` e `scripts`.

- `Scripts`: são definidos pelo próprio desenvolvedor, sendo que podem ser até mesmo comandos que não utilizam alguma biblioteca `JS`. Por exemplo, poderiamos adicionar a chave `"list": "ls"` dentro de `"scripts"`, e rodar o comando com `npm run list` ou `yarn run list`, que teria como output a listagem do diretório do repositório atual.

- `Dependencies`: como o próprio nome da a entender, são as dependencias utilizadas naquele projeto. É sempre interessante/importante que você tenha ao menos uma noção do que as libs incluídas fazem... Basta acessar [https://www.npmjs.com/package/](https://www.npmjs.com/package/) e incluir no final da url o pacote que está "inspecionando"; por exemplo: [https://www.npmjs.com/package/marked](https://www.npmjs.com/package/marked)

Você pode encontrar mais informações sobre o `package.json` [aqui](https://docs.npmjs.com/cli/v7/configuring-npm/package-json).

## Instalando dependencias dos projetos

Antes de executarmos cada um dos projetos, precisamos instalar as dependencias previamente citadas:

*A partir da pasta "conduit":*
```bash
$ echo "$(cd backend && yarn)" & echo "$(cd frontend && yarn)"
```

> Você pode substituir o comando `yarn` por `npm install`


```bash
$ yarn dev
```

```bash
$ yarn start
```

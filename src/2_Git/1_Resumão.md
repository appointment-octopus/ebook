# Resumão

O que você verá nesse capítulo:

- [Resumão](#resumão)
  - [Explicação](#explicação)
  - [Flow básico de utilização](#flow-básico-de-utilização)
    - [1. Após criar repositório no Github, no `terminal`](#1-após-criar-repositório-no-github-no-terminal)
      - [Clonar um repositório](#clonar-um-repositório)
      - [Trocar de diretório](#trocar-de-diretório)
      - [Exemplo completo](#exemplo-completo)
    - [2. Após fazer as mudanças nos arquivos que quiser, no `terminal`](#2-após-fazer-as-mudanças-nos-arquivos-que-quiser-no-terminal)
      - [Listar todas as alterações feitas (o que foi adicionado/modificado/removido)](#listar-todas-as-alterações-feitas-o-que-foi-adicionadomodificadoremovido)
      - [Adicionar alterações feitas](#adicionar-alterações-feitas)
      - [Commitar](#commitar)
      - [Subir as alterações pro Github](#subir-as-alterações-pro-github)
      - [Exemplo completo](#exemplo-completo-1)

## Explicação

| _ | O que é |
| ---------- | ------- |
| Git | Ferramenta para "salvar" as varias versões dos seus arquivos/código-fonte |
| Github | Lugar pra salvar teus arquivos/código-fonte |


## Flow básico de utilização

### 1. Após criar repositório no Github, no `terminal`

#### Clonar um repositório

```bash
$ git clone <endereço do novo repositório>
```

#### Trocar de diretório

```bash
$ cd <nome do repositorio>
```

#### Exemplo completo

```bash
# ex:
# git clone https://github.com/airbnb/javascript
# cd javascript
```


### 2. Após fazer as mudanças nos arquivos que quiser, no `terminal`

#### Listar todas as alterações feitas (o que foi adicionado/modificado/removido)

```bash
$ git status
```

#### Adicionar alterações feitas

```bash
$ git add <arquivo_1> <arquivo_2>
```

#### Commitar

```bash
$ git commit -m "mensagem explicando o proposito desse commit"
```

#### Subir as alterações pro Github

```bash
$ git push origin <branch_desejada>
```

#### Exemplo completo

```bash
# ex:
# git add RemoveUserButton.js styles.css
# git commit -m "adicionando botão para remoção de usuários"
# git push origin main
```

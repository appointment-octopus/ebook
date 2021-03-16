# Resumão

O flow básico de utilização no dia a dia é:

## 1. Após criar repositório no Github, no `terminal`

### Clonar um repositório

```bash
$ git clone <endereço do novo repositório>
```

### Trocar de diretório

```bash
$ cd <nome do repositorio>
```

### Exemplo completo

```bash
# ex:
# git clone https://github.com/airbnb/javascript
# cd javascript
```


## 2. Após fazer as mudanças nos arquivos que quiser, no `terminal`

### Listar todas as alterações feitas (o que foi adicionado/modificado/removido)

```bash
$ git status
```

### Adicionar alterações feitas

```bash
$ git add <arquivo_1> <arquivo_2>
```

### Commitar

```bash
$ git commit -m "mensagem explicando o proposito desse commit"
```

### Subir as alterações pro Github

```bash
$ git push origin <branch_desejada>
```

### Exemplo completo

```bash
# ex:
# git add RemoveUserButton.js styles.css
# git commit -m "adicionando botão para remoção de usuários"
# git push origin main
```

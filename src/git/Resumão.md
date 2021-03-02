# Resumão

O flow básico de utilização no dia a dia é:

1. Após criar repositório no Github, no `terminal`:
   ```bash
   git clone <endereço do novo repositório>
   cd <nome do repositorio>

   # ex:
   # git clone https://github.com/airbnb/javascript
   # cd javascript
   ```

2. Após fazer as mudanças nos arquivos que quiser, no `terminal`:
   ```bash
   git status # vai listar todas as alterações feitas (o que foi adicionado/modificado/removido)
   
   git add . # adiciona todas as alterações

   git commit -m "mensagem explicando o proposito desse commit" # ex: git commit -m "adicionando botão para remoção de usuários"

   git push origin <branch_desejada>
   ```

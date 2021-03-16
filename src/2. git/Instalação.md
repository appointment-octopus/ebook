# Instalação e Configuração

## Instalando
### Windows

Para Windows, não tem segredo, basta simplesmente baixar o [GitBash](https://git-scm.com/downloads) :)

### Linux

> *Via de regra, voce pode replicar todos os comandos aqui no Mac; basta substituir os* "`sudo apt install ...`" *por*  "`brew install ...`"

1. Por ser muito comum, provavelmente o `git` já virá instalado no seu Linux; para averiguar, basta rodar, no seu terminal:

   ```bash
   $ which git
   /usr/bin/git
   ```

1. Caso o output tenha sido *"`git not found`"*, há de se instalar com*:

   ```bash
   $ sudo apt install git
   ```

> \* *Dependendo do Linux utilizado, pode ser que o gerenciador de pacotes seja outro em vez do apt-get (ex: pacman)*

## Configurando

Primeiro, tendo em vista que o *commit* é um registro, é importante se identificar antes de começar a utilizar o `git`:

```bash
git config --global user.name "Seu Nome"
```

```bash
git config --global user.email seu_email@exemplo.com
```

```bash
# ex:
# git config --global user.name "Joao da Silva"
# git config --global user.email joao_da_silva@gmail.com
```

Caso queira adotar outras identidades em outras pastas de trabalho, basta replicar o comando acima sem a *flag* `--global`:

```bash
cd pasta_de_trabalho
```

```bash
git config user.name "Outro Nome"
```

```bash
git config user.email outro_email@exemplo.com
```

### SSH 
> *Caso esteja utilizando GitBash no Windows não precisa se preocupar com isso*

Caso tenha utilizado `git` outras vezes, já deve ter percebido como é chato ter de se autenticar todas as vezes que vai subir um *commit* para o *Github*

Para contornar isso, vamos nos autenticar utilizando uma chave *ssh*

1. Verificar se já foram registradas chaves *ssh* para seu sistema operacional

   ```bash
   $ ls -a ~/.ssh
   .  ..  id_rsa  id_rsa.pub  known_hosts
   ```

2. Caso não hajam chaves neste diretorio, isto é, o output tenha sido

   ```bash
   $ ls -a ~/.ssh
   .  ..
   ```

   temos de criá-las.

   No terminal:

   * Pressione [enter] quantas vezes for necessário

      ```bash
      $ ssh-keygen
      ```

      > Pequena explicação: A flag '-s' gera um "script" bash pro stdout (em texto), necessário para conectar/iniciar o agente. 

   * O eval, então, "roda" esses comandos do script

      ```bash
      $ eval `ssh-agent -s`
      ```

   * adicionar a chave pro agente (caso tenha atribuido outro nome [no "$ ssh-keygen"] para a chave privada, mude o "id_rsa" para o nome correto)

      ```bash
      $ ssh-add ~/.ssh/id_rsa
      ```

3. Então, basta adicionar a chave pública no *Github*. Abra [este link](https://github.com/settings/keys), clique no botão "New SSH Key", e então copie a sua chave pública em `~/.ssh/id_rsa.pub`:

   > esses comandos são totalmente dispensáveis, já que pode abrir o arquivo e copiar manualmente
   * Para copiar pro clipboard a chave publica

      Instalar `xclip`:

      ```bash
      $ sudo apt install xclip
      ```

      Copiar arquivo pro clipboard (o equivalente a dar Ctrl+C no conteúdo do arquivo)

      ```bash
      $ xclip -sel c < ~/.ssh/id_rsa.pub
      ```

   * Agora basta colar essa chave no campo adequado para criar a chave dentro do *Github*

4. Extra: Atualizar as urls dos repositorios clonados para utilizar o *ssh* em vez do *https*. Primeiro, checar como o repositório está rastreado.
   * listar os repositórios rastreados

   ```bash
   $ git remote -v
   origin	https://github.com/appointment-octopus/ebook (fetch)
   origin	https://github.com/appointment-octopus/ebook (push)
   ```

   Caso realmente esteja utilizando *https* (e deseje alterar para utilizar *ssh*), basta rodar, no terminal, o seguinte comando:

   ```bash
   $ echo "$(git ls-remote --get-url origin)" |\
    { read url;\
     eval `git remote set-url origin git@github.com:${${url#*com/}%.git}.git`; } 
   ```

#### Como curiosidade, como o comando anterior foi construído:

-------------

Tendo em vista que uma url https padrão do github é:
> <https://github.com/appointment-octopus/ebook>

e uma url ssh padrão é:
> git@github.com:appointment-octopus/ebook.git

percebemos que necessitamos extrair o nome da organização + nome do repositório; isto é: *`appointment-octopus/ebook`*. Utilizando o pattern matching para strings padrão do bash, conseguimos fazer isso. O `#` é utilizado para remover prefixos, então:

```bash
$ URL=https://github.com/appointment-octopus/ebook
```

O `*` vai ignorar qualquer caracter até encontrar a sequencia `com/`, e então retornar o resto da string
```bash
$ echo "${URL#*com/}"
```

Porém, algumas vezes a url `https` vem com um `.git` no final; para ignorá-lo, utilizaremos o `%`, cujo qual é utilizado para remover sufixos:

```bash
$ URL=appointment-octopus/ebook.git
```

Irá retornar a string até encontrar a sequencia ".git"
```bash
$ echo "${URL%.git}
```

Portanto, juntando tudo, fica:

```bash
$ URL=https://github.com/appointment-octopus/ebook.git
```

```bash
$ echo "${${URL#*com/}%.git}"
```

Entretanto, estamos inserindo a url na mão. Felizmente existe um comando que nos retorna a url que precisamos:

```bash
$ URL="$(git ls-remote --get-url origin)"
```

Agora que temos o que queríamos (nome do usuário/organização+nome do repositório), basta formatar o url de output.

```bash
$ URL="$(git ls-remote --get-url origin)"
```

```bash
$ echo "git@github.com:${${URL#*com/}%.git}.git"
```

Mas não basta ter a url formatada se não "setarmos" ela:

```bash
$ URL="$(git ls-remote --get-url origin)"
```

```bash
eval `git remote set-url origin git@github.com:${${URL#*com/}%.git}.git`
```

Juntando tudo em um comando só, utilizando o pipe ("`|`") do bash para passar a url para a variável `url`:

```bash
$ echo "$(git ls-remote --get-url origin)" |\
   { read url;\
   eval `git remote set-url origin git@github.com:${${url#*com/}%.git}.git`; } 
```

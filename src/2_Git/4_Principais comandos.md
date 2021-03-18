# Principais comandos

Bom, enfim vamos trabalhar com um exemplo do zero.

O que você verá nesse capítulo:

- [Principais comandos](#principais-comandos)
    - [Git init](#git-init)
      - [Extra](#extra)
    - [Git status](#git-status)
    - [Git add](#git-add)
    - [Git log/reflog](#git-logreflog)
    - [Git reset/restore](#git-resetrestore)
    - [Git commit](#git-commit)
    - [Git remote](#git-remote)
    - [Git push](#git-push)
    - [Git checkout](#git-checkout)
    - [Git merge](#git-merge)
    - [Git rebase](#git-rebase)
    - [Git branch](#git-branch)
    - [Git commit amend + co-author](#git-commit-amend--co-author)

### Git init

Para este tutorial, crie uma pasta para que possa acompanhar esse tutorial de forma mais interativa:

```bash
$ mkdir aprendendo_git
```

```bash
$ cd aprendendo_git
```

Para versionar uma pasta/diretório, é preciso iniciar um repositório. A partir da pasta raíz do seu projeto, execute:

```bash
$ git init
Initialized empty Git repository in <caminho_até_diretório>/aprendendo_git/.git/
```

Após isso, liste os arquivos neste diretório:

```bash
$ ls -a
```

> a flag `-a` significa: "do not ignore entries starting with `.`"

O **Git** criou uma pasta chamada `.git`. Essa pasta contém os metadados que o git necessita para operar naquele repositório.

#### Extra

Sinta-se, obviamente, a vontade para explorar essa pasta :)

```bash
$ sudo apt install tree
```

```bash
$ tree .git
.git
├── branches
├── config
├── description
├── HEAD
├── hooks
│   ├── applypatch-msg.sample
│   ├── commit-msg.sample
│   ├── fsmonitor-watchman.sample
│   ├── post-update.sample
│   ├── pre-applypatch.sample
│   ├── pre-commit.sample
│   ├── pre-merge-commit.sample
│   ├── prepare-commit-msg.sample
│   ├── pre-push.sample
│   ├── pre-rebase.sample
│   ├── pre-receive.sample
│   └── update.sample
├── info
│   └── exclude
├── objects
│   ├── info
│   └── pack
└── refs
    ├── heads
    └── tags

9 directories, 16 files
```

### Git status

Sempre que você estiver nesse repositório, terá acesso a versão mais atual do projeto. Utilizando o comando `git status`, pode aferir quais foram as ultimas mudanças em relação ao ultimo commit (traduzindo: a ultima versão "salva" do projeto)

Como não adicionamos nenhum arquivo, caso rode este comando terá o seguinte output:

```bash
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

> hoje em dia há um movimento para que a branch padrão se chame `main` em vez de `master`, então não se surpreenda caso o seu output tenha sido diferente

Ou seja, não há nada para adicionar (e depois commitar), assim como não há uma versão anterior para se comparar com a versão atual da pasta

### Git add

Crie um arquivo `lorem_ipsum.txt`:
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris malesuada augue vel quam dignissim, nec egestas nisl pretium. Integer porttitor eleifend turpis non ullamcorper. Maecenas maximus sit amet ipsum et facilisis. Aenean tincidunt urna a ex consequat venenatis. Curabitur eget ante scelerisque tellus efficitur pulvinar ac quis lorem. Donec imperdiet ligula id tortor viverra, imperdiet consequat est suscipit. Donec congue pellentesque velit eget rhoncus. Vestibulum bibendum erat sem, sed maximus ipsum condimentum et. Vivamus lectus justo, hendrerit ac ornare eget, ultrices ut massa. Sed euismod, magna vitae ultrices aliquam, est quam volutpat mauris, id fringilla mauris sem ut diam. Mauris laoreet efficitur urna at tempor. Nulla scelerisque iaculis ligula et consequat. Nulla in viverra nunc. Nunc nibh neque, ornare ut magna sed, tempor egestas ligula. Quisque iaculis justo ut diam mattis, vitae iaculis eros luctus.
```

```bash
$ ls
lorem_ipsum.txt
```

```bash
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	lorem_ipsum.txt

nothing added to commit but untracked files present (use "git add" to track)
```

Perceba que o próprio git nos dá dicas. Execute:

```bash
$ git add lorem_ipsum.txt
```

```bash
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   lorem_ipsum.txt
```

### Git log/reflog

### Git reset/restore

### Git commit

### Git remote

### Git push

### Git checkout

### Git merge

### Git rebase

### Git branch

### Git commit amend + co-author

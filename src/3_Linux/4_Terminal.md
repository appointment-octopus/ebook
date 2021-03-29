# Terminal

Por não possuir uma interface gráfica, a primeiro contato pode ser intimidador, mas é essencial saber ao menos o básico do terminal, para interagir de forma mais prática com seu computador.

<!-- (imagem ou logo do terminal?) -->

Experimente abrir o terminal e vamos fazer algumas experimentações; 

No windows você tinha um gerenciador de tarefas, uma interface que te mostrava como funcionava a estrutura da organização dos seus arquivos, assim podendo entrar e sair de pastas, e acessar esses arquivos, executar, abrir, editar...

> A primeira vista vai reparar no símbolo `~` no começo da primeira linha, basicamente é uma abreviação para a sua pasta home no terminal.

Com o terminal aberto, utilize o comando `cd` (change directory) para alterar o diretório atual, com o acréssimo de `/` você pode acessar os arquivos de sistema do seu computador, então no seu terminal, experimente: 

```bash
$ cd /
```
Bem nesse ponto um símbolo `~$` que fica no começo do seu terminal vai ter agora `/` na frente indicando qual a pasta em que você se encontra no momento.

Agora escreva `ls` (list contents) para poder listar pastas e arquivos dentro daquele diretório. Então dentro da pasta `/` experimente usar `ls`:

```bash
$ ls
```

![terminal_ls](src/Imagens/terminal_ls.png)

Nesse ponto você pode por exemplo tentar entrar em uma pasta dentro dessa pasta utilizando `cd` ali acima junto com o nome de uma pasta presente dentro daquele diretório (que você acabou de ver usando o `ls`).

```bash
$ cd bin
```

Experimente mais uma vez listar os arquivos dentro desse outro diretório.

> Vai se deparar com alguns arquivos binários (que são arquivos que podem ser executáveis e que auxiliam na configuração interna ou execução de alguma aplicação).

<!-- Não sei se deveria colocar um capítulo separado para diretórios, e falar mais de outros comandos no terminal -->

### Diretórios

Além da pasta **bin** que guarda arquivos binários para execução, vamos citar alguns outros que provavelmente vai se deparar com eles e se perguntar, sua função ou necessidade, até porque eles também estão consumindo uma parte da "memória" do seu computador.

**/sbin:** Da mesma forma que a bin, a sbin são conjuntos de executáveis do sistema que cuidam de configurações como a segurança do computador por exemplo. É responsável por pedir credenciais ou permissão de um adm quando for instalar algum programa por exemplo.

**/boot:** Se chegou a fazer o processo de dual boot, já tem uma ideia do que é guardado aqui dentro. Bem basicamente é tudo que o seu computador precisa para poder iniciar o seu Linux corretamente.

**/dev:** Como uma abreviação para *developers*, nessa pasta estão guardadas os arquivos responsáveis pelas configurações de desenvolvedores, no geral a conversa que ocorre entre hardwares como o seu teclado, mouse, câmera, com outras partes do seu computador.

**/etc:** Guarda também um conjunto de instruções que podem ser configuradas por texto, são tão importantes quanto os arquivos contidos em dev, entretanto podem ser simplesmente serem editados em um editor de texto do seu computador.
<!-- talvez falar melhot ou um pouco mais -->

**/home:** Por default, praticamente sempre que abre o seu terminal começa nessa pasta, então funciona quase como o desktop do seu windows.

**/lib(32 e 64):** É onde as aplicações guardam arquivos ao se instalarem. Serão armazedos arquivos binários como em bin e sbin.

**/media e /mnt:** São diretórios em que você pode montar um dispositivo físico, como CD-ROM, partição do seu HD, um pendrive etc.

# Resumão Linux

Nesse capítulo você terá um 'Resumão' sobre introdução e conceitos básicos e alguns comandos em um terminal Linux, além de aprender como instalar um outro sistema operacional no seu computador ou usar uma ferramenta para poder utilizar algumas outras funções Linux.

- [Resumao Linux]()
    - [Explicação](#explicação)
    - [Dual Boot](#dual-boot)
    - [Terminal](#terminal)
        -[Alguns comandos do terminal]()
            -[Listar arquivos e pastas daquele diretório](#listar-arquivos-e-pastas-daquele-diretório)
            -[Alterar o diretório atual](#alterar-o-diretório-atual)
            -[Criar uma pasta naquele diretório](#criar-uma-pasta-naquele-diretório)
            -[Executar um arquivo](#executar-um-arquivo)
            -[Apagar um arquivo](#apagar-um-arquivo)

## Explicação

Criado em 1991 por Linus Torvalds.

Baseado em Unix

O Linux é o Kernel ou Núcleo do Sistema Operacional (faz a comunicação entre o hardware e o sistema operacional)

É desenvolvido por diversas pessoas e empresas ao redor do mundo (vários sistemas operacionais e Kernels baseados no Linux)

Multitarefa / Multiusuário

### Distribuições

O que é uma "distro"? Uma distro é uma distribuição baseada no Kernel Linux.

O Linux pode ser "distribuído" por empresas, organizações ou mesmo pessoas, quem podem colocar características próprias no sistema operacional, como configurações, aplicações, sistemas de instalação entre outras peculiaridades, assim damos o nome de distribuição, sua escolha é pessoal e depende da aplicação.

Distribuições mais conhecidas:

 - Ubuntu
 - Debian
 - SuSE
 - fedora
 - popOS!

## Requisitos para Instalação

Processador dual core de 2GHz ou superior.

2 GB de memória RAM.

40 GB de espaço livre no disco rígido.

## Dual Boot

Particionar o HD para receber o novo sistema operacional.
Bootar um pendrive para colocar o instalador do sistema operacional dentro dele.
Dentro da Bios, e com o pendrive no computador fazer ele bootar primeiro o pendrive para rodar o instalador do sistema operacional. 

## Terminal

O Terminal, Shell ou Konsole é uma linha de comando onde podemos executar programas específicos do Linux.

A maioria dos comandos são iguais em diversas distribuições.

Uso para automação de processos através dos comandos, facilita o trabalho no Sistema para Profissionais da Área.

O Terminal pode ser aberto de diversas formas, mas a sequência de teclas **CTRL + ALT + T** facilita seu acesso.

Dentro do terminal a sequência de teclas **CTRL + SHIFT + T** abre uma nova aba.

O comando `pwd` mostra o caminho do diretório.

```bash
$ pwd
```

O comando `ls` lista os diretórios e arquivos da pasta. O comando dir pode ser usado também, mas o comando anterior funciona melhor.

```bash
$ ls
```

O comando `cd` (change directory) muda o diretório atual, ou seja, muda o caminho, podemos entrar e sair de pastas.

```bash
$ cd
```
O comando `mkdir `(make directory) cria um diretório de arquivos, uma pasta.

```bash
$ mkdir teste
```

Para sair da pasta atual e retornar para a anterior é só digitar o comando `cd ..`.
# Linux

Nesse capítulo você terá uma introdução a conceitos básicos e alguns comandos em um terminal Linux, além de aprender como instalar um outro sistema operacional no seu computador ou usar uma ferramenta para poder utilizar algumas ferramentas Linux.

- [Linux]()
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

| _ | O que é |
| ---------- | ------- |
| Linux | Sistema operacional de código aberto |
| Terminal | É um programa que recebe os comandos do usuário a partir do teclado e repassa-os às camadas de baixo nível do sistema operacional. |

## Dual Boot

Particionar o HD para receber o novo sistema operacional.
Bootar um pendrive para colocar o instalador do sistema operacional dentro dele.
Dentro da Bios, e com o pendrive no computador fazer ele bootar primeiro o pendrive para rodar o instalador do sistema operacional. 

## Terminal

### Alguns comandos do terminal

#### Listar arquivos e pastas daquele diretório

```bash
$ ls
```

#### Alterar o diretório atual

```bash
$ cd /nome_do_diretório
```
> apenas um `cd` faz você voltar para a home.

#### Criar uma pasta naquele diretório

```bash
$ mkdir nome_da_pasta
```

#### Executar um arquivo

```bash
$ ./nome_do_arquivo
```
#### Apagar um arquivo

```bash
$ rm nome_arquivo
```
> caso o arquivo não esteja na pasta em que está no momento, basta colocar o caminho antes do nome.

```bash
$ rm /caminho/nome_arquivo
```

> cada `/` representa um caminho antes de uma pasta
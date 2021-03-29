# Git & Github

## Git

Lembra quando salvava os arquivos como `projeto-final.txt`, `projeto-final-2.txt`, `projeto-final-mesmo_agora_vai.txt` (etc)?

Git soluciona isso. Serve justamente pra versionar seus arquivos (além de providenciar varias outras utilidades como consequencia disso), mas de uma forma muito mais elegante.

Considerando aquele exemplo besta acima, suponha que cada um dos arquivos possua os seguintes conteúdos:

1. `projeto-final.txt`
    ```
    Amanhã será um dia bonito
    ```

2. `projeto-final-2.txt`
    ```
    Amanhã será um belíssimo dia!
    ```

3. `projeto-final-mesmo_agora_vai.txt`
    ```
    Os dias porvir hão de ser belos!
    ```

Utilizando git, considerando essa linha do tempo, você poderia ter apenas um arquivo (`projeto-final.txt` [com o conteúdo de `projeto-final-mesmo_agora_vai.txt`]), com a opção de retornar ao conteúdo das versões anteriores sempre que quisesse.

Além disso, Git possui algo muito incrível que é o sistema de Branches (traduzindo, seriam "galhos" ou "ramificações"); isso é, você pode criar branches independentes com propósitos distintos (por exemplo: uma branch com código mais estavel, outra para experimentações e ai vai da imaginação [ou não])

Tudo isso ficará mais claro conforme formos praticando :)

## Github

Bom, todo esse versionamento é incrivel; mas ele funciona somente localmente. Github surge, portanto, para armazenar repositórios online; dessa forma possibilita que:
- Você possa recuperar seu repositório/código para trabalhar em outros computadores
- Você possa compartilhar seu código com outras pessoas de forma que ambos trabalharão na mesma base de código, cada um podendo inserir seus próprios versionamentos (ou, *commits*).

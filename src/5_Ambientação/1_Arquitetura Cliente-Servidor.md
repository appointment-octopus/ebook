# Arquitetura Cliente-Servidor

<!-- falar de monolitico -->


De forma geral, principalmente se tratando de aplicações Web:

- Cliente = Front-end
  - executado no computador do usuário
  - responsável pelo *"visual"*
- Servidor = Back-end
  - processos e serviços que são executados em um servidor dedicado (ou processos executados em *background* na máquina do usuário)
  - responsável pela comunicação com banco de dados

Ok, mas como isso funciona? Quando você acessa um site, está acessando a aplicação "cliente" - que é responsável por estruturar os dados vindos do Servidor em um template visual.


## Exemplo 1

> (não real, apenas para ilustração)

[![Blogimg](https://cdn.dribbble.com/users/33073/screenshots/15152642/media/100af76a27f33770df4dc3ae53e9f41f.png)](https://dribbble.com/shots/15152642-My-Personal-Website-Blog-Launched)
> *Fonte: [Dribbble - My Personal Website - Blog Launched 🚀](https://dribbble.com/shots/15152642-My-Personal-Website-Blog-Launched)*

1. o Usuário acessa a aplicação-**cliente** no endereço [https://www.blog.com]()
2. a aplicação-**cliente** pede à aplicação-**servidor** os últimos 3 posts em [https://www.api_do_blog.com/posts]() 
    1. aplicação-**servidor** acessa o **banco de dados**, que retorna todos os `N` posts já feitos, estruturados da forma: 
        ```json
        {
            nome: "Nome do post",
            conteúdo: "Lorem ipsum dolor sit amet",
            data_de_publicação: "DD-MM-YYYY"
        }
        ```

    2. aplicação-**servidor** ordena esses dados pela data
    3. aplicação-**servidor** retorna os 3 posts mais recentes para a aplicação-**cliente**
3. aplicação-**cliente** estrutura os dados recebidos de uma forma visual:
    ```html
    <body>
        { for post in posts }
        <div>
            <p>{ post.nome }</p>
            <p>{ post.conteúdo }</p>
            <p>{ post.data_de_publicação }</p>            
        </div>
        { end for}
    </body>
    ```
4. aplicação-**cliente** retorna `html` final do endereço [https://www.blog.com]() ao Usuário, que então é renderizado pelo navegador
    ```html
    <body>
        <div>
            <p>Post A</p>
            <p>Conteudo do Post A</p>
            <p>25-03-2021</p>
        </div>
        <div>
            <p>Post B</p>
            <p>Conteudo do Post B</p>
            <p>24-03-2021</p>
        </div>
        <div>
            <p>Post C</p>
            <p>Conteudo do Post C</p>
            <p>21-03-2021</p>
        </div>
    </body>
    ```

## Exemplo 2

> (não real, apenas para ilustração)

1. Usuário abre jogo [Pokemon](https://play.google.com/store/apps/details?id=com.pokemon.pokemontcg&hl=en&gl=US) pelo aplicativo no celular
2. Usuário toca no ícone de lista de pokemons
3. aplicativo faz requisição para servidor em [pokeapi.co/api/v2/pokemon](https://pokeapi.co/api/v2/pokemon?limit=-1)
4. servidor acessa banco de dados, retorna todos os pokemons, com `nome` + `url`...
5. aplicativo mostra lista de pokemons

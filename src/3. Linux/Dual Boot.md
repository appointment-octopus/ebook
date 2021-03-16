Caso esteja iniciando e gostaria de fazer isso com um bom começo, recomendamos a utilização de um sistema operacional baseado no Linux, como o Ubuntu por exemplo que fácil instalar e usar. Linux é uma boa opção por motivos como seu software aberto (que pode ser visto e melhorado por qualquer um), e por conta da sua alta capacidade de processamento (até mesmo em hardwares mais antigos), isso auxilia por exemplo em um cenário que precisa lidar com uma grande quantidade de dados.

E mesmo sabendo que é uma boa opção, ainda sim, possui outros motivos para manter outro sistema operacional na sua máquina.

Para resolvermos essa questão pode-se optar por fazer um Dual Boot. No geral isso implica dizer, que podemos colocar mais do que apenas um sistema operacional em seu computador, basta termos um pen-drive bootável, e espaço no seu disco rígido suficiente para isso.

### Começando

1. Faça o download do [Ubuntu](https://ubuntu.com/#download) (a 20.04 LTS é uma boa opção).

2. Tenha certeza de que tem ao menos 50 GB de espaço sobrando no seu HD.

3. Uma unidade flash USB com no mínimo 8 GB.

4. E um programa para para poder criar um USB bootável, uma sugestão seria o [Rufus](https://rufus.ie/)

### 1º passo: Crie um USB bootável com o Ubuntu

Antes de começar esse passo certifique-se de que não há nenhum arquivo importante dentro do seu pendrive, já que esse procedimento irá ser reescrito fazendo com que perca qualquer conteúdo que havia contido antigamente.

Com seu pendrive pronto para ser reescrito, insira-o em seu computador e abra o Rufus.

![interface_Rufus](ebook/src/Imagens/Rufus_1.png)

Ele irá detectar automaticamente o drive USB inserido.

Em 'Boot selection' selecione a imagem ISO do Ubuntu que havia feito o download anteriormente. Depois que selecionar irá aparecer alguns avisose uma opção de escrita da ISO. Responda 'yes', escolha a opção recomendada, e confirme que está ciente que os arquivos dentro da unidade serão destruídos.

Depois disso o botão de "Ready", vai ser habilitado.
Clique e espere alguns minutos enquanto o USB vai sendo reescrito.
Isso pode demorar alguns minutos dependendo da velocidade do seu USB.

![Copying_ISO_Rufus](ebook/src/Imagens/Rufus_2.png)

Quando terminar, remova seu USB de forma segura, agora dentro dele existe uma imagem de Ubuntu pronta para ser instalada em um computador.

> *Embora não seja exatamente necessário, recomenda-se desfragmentar o disco do seu computador para poder consolidar os arquivos do seu computador para o 'início' do seu disco, dessa forma liberando mais espaço antes de fazer o particionamento.*

### 2º passo: Aloque espaço no seu disco rígido.

É necessário particionar seu disco rígido para separar um espaço de atuação para o novo sistema operacional que será instalado no seu computador.

Vá no menu iniciar do windows e procure por "Partições" ou por "Gerenciamento de disco".

Vai se deparar com uma tela similar a esta, nela vai listar as unidades de espaço contidas dentro do seu computador.

![Gerenciamento_de_disco](ebook/src/Imagens/gerenciamento_de_disco.jpeg)

Escolha algum dos espaços tendo em mente que você irá dividir uma dessas unidades, caso tenha mais de uma, opte pela maior provavelmente a sua unidade "(C:)".

Clique com o botão direito na que escolheu.
Clique em "Diminuir Volume...".

O espaço de disco que o Ubuntu LTS costuma requisitar, gira em torno de 20 GB ou mais.

> *Tenha em mente que por mais que ele precise apenas de pouco espaço, vai ser um outro sistema operacional onde irá precisar instalar softwares e salvar arquivos, logo é bom se reservar uma boa quantidade de espaço para não ter problemas por falta dele no futuro*

Logo o espaço que irá diminuir seria de ao menos 20000 MB.

![gerenciamento_de_disco_exemplo](ebook/src/Imagens/gerenciamento_de_disco_1.jpeg)

### 3º passo: Instalação.
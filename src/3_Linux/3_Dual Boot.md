# Dual Boot

Esse passo tem a inteção de explicar como vai ser a instalação de outro sistema operacional dentro do seu computador, para não ter que abrir mão de uma interface que já é uma amiga de longa data, mas quer também exeperimentar a possibilidade de ter uma nova opção para desenvolver.

### Começando

**Warning:** Antes de mais nada, faça esse passo a passo num dia calmo e que esteja tranquilo e disposto a possivelmente encontrar alguns problemas.

Esse tutorial segue um fluxo simples e contínuo para instalação do Ubuntu, caso se interesse por outra distribuição do Linux, aconselho a pesquisar um pouco, mas caso seja essa mesmo que gostaria, vamos para o tutorial! :)

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

Coloque o Pendrive de com o Boot do Ubuntu em uma unidade USB do seu computador e o reinicie. Enqaunto ele estiver fazendo o processo de "Ligar" novamente, **PRESSIONE VÁRIAS VEZES** a tecla F11 ou F12 (na verdade pode variar até mesmo para as teclas F10, F8, F2, já que é uma coisa diferente desde a fabricação do computador), então caso não consiga chegar até a sua tela de bios, basta reiniciar novamente e escolher outra tecla.

Obtendo êxito, use as teclas do seu teclado para acessar o Boot Menu (menu de boot) e escolher o seu pendrive de boot, que nesse caso é o "3. USB HDD: SanDisk-(USB 2.0)".

![Boot_Menu](src/Imagens/boot_menu-ubuntu.jpg)

Sempre selecionando as opções e clicando em **Continuar**

Dessa forma o processo de instalação do Ubuntu será iniciado e poderá escolher qual idioma gostaria de fazer o processo de instalação.

![Install_ubuntu_1](src/Imagens/install_ubuntu_1.png)

Depois poderá escolher a opção do Layout do seu teclado;

Irá escolher entre a instalação normal e a instalação mínima, e dependendo se já efetuou a configuração da sua internet, opte por selecionar as opções que baixa as atualizações juntamente com a instalação do Ubuntu.

![Install_ubuntu_2](src/Imagens/install_ubuntu_2.jpg)

![Install_ubuntu_3](src/Imagens/install_ubuntu_3.jpg)

Escolha a sua localidade;

Defina as suas credenciais de nome, usuário e senha;

Espere as etapas finais da instalação e ao fim clique no botão "Reiniciar agora".

**Lempre-se de desconectar o seu pen-drive antes de reiniciar**

Quando terminar de reiniciar irá se deparar com uma tela indicando que conseguiu chegar ao enfim dual boot :) 

![Menu_de_Boot](src/Imagens/menu_de_boot.jpg)

<!-- imagens e alguns elementos do texto desse tutorial, foram retirados de [Mundo Ubuntu](https://www.mundoubuntu.com.br/tutoriais/instalacao/396-instalacao-facil-do-ubuntu-20-04-lts-no-windows-10-dual-boot) -->
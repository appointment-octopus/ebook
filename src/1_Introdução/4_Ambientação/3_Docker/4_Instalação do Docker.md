# Instalação do Docker

### Docker

O método mais recomendado é indo diretamente pela fonte: [Install Docker](https://docs.docker.com/engine/install/)

Mas, por questões de simplicidade:

```console
$ curl -sSL https://get.docker.com/ | sh
$ exec $SHELL
$ sudo usermod -aG docker $(whoami)
```

Verifique se consegue rodar normalmente:

```console
$ docker run hello-world
```


### Docker-compose

Novamente, o mais recomendado é ir direto pela fonte: [Install Docker Compose](https://docs.docker.com/compose/install/)

Mas, por simplicidade -> para instalar a versão mais atual do `docker-compose`, execute o seguinte script:

```bash
url="https://github.com/docker/compose/releases/latest"

latest_version=$(curl $url -s -L -I -o /dev/null -w '%{url_effective}' | { read -r redirected_url; echo "${redirected_url##*/}"; })

curl -L https://github.com/docker/compose/releases/download/"$latest_version"/docker-compose-"$(uname -s)"-"$(uname -m)" > /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose
```

Verifique que instalou corretamente:

```console
$ docker-compose -v

docker-compose version 1.29.2, build 5becea4c
```

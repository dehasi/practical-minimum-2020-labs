ldd
otool -L

docker run hello-world

docker run ubuntu:14.04

docker run ubuntu:14.04 echo hello
docker run ubuntu:14.04 ls

### Разные способы запуска контейнера

docker run --interactive ubuntu:14.04 echo hello
echo ls | docker run --interactive ubuntu:14.04
echo hello | docker run --interactive ubuntu:14.04 tr [eo] [EO]

docker run --interactive --tty ubuntu:14.04

docker run --detach --rm  redis
docker attach <hash>


docker run --interactive --tty --name ubn ubuntu:14.04
docker restart ubn
docker attach ubn

docker stop 93f008a36902df610a2cb2be422570e60f42b24fdfea9dc08bf921f834653783


### Файловая система

docker run -it --rm --env "LOL=KEK" ubuntu

docker run --interactive --tty --rm --volume $(pwd):/hd  ubuntu:14.04

docker volume ls
docker volume create my-volume

docker run --interactive --tty --rm --volume my-volume:/hd  ubuntu:14.04
docker volume remove  my-volume

### Сети
docker run --detach --rm --publish 8080:80 nginx

docker run --interactive --tty --rm --network none  ubuntu:14.04
docker network ls

ifconfig find ip eth0

docker inspect <hash>
docker inspect c870bc956375 | jq '.[0].Config'
docker inspect c870bc956375 | jq '.[0].NetworkSettings.Networks.bridge'

docker network ls
docker network create my-net
docker network rm my-net


docker run --interactive --tty --rm   --network my-net --name buntu1 ubuntu:14.04
docker run --interactive --tty --rm   --network my-net --name buntu2 ubuntu:14.04

### Создаем свой образ
docker run --interactive --tty --name buntu1 ubuntu:14.04
docker commit 09873b3e2bf2  lol:kek

docker push lol:kek
docker history lol:kek


#### Dockerfile

```
FROM ubuntu:14.04 # или FROM scratch
ADD/COPY script.sh /usr/bin/script.sh # лучше использовать COPY
RUN chmod +x script.sh
VOLUME /data
ENV PATH /usr/bin:$PATH
EXPOSE 8080 
ENTRYPOINT/CMD [“program”, “arg1”, “arg2”]
```

docker build /path/to/Dockerfile --tag lol:kek

docker image ls
docker images
docker image ls -a 
docker rmi 
docker logs
docker logs -f



#!/bin/bash
IMAGE=$(docker images ubuntu-dev | grep -v "REPO")
UNAME=$(uname -m)

if [[ "$1" == "clean" ]]; then
  docker stop CloudTools
  docker rm CloudTools
  exit 0
fi

if [[ -z "$IMAGE" ]]; then
  echo "INFO: Building Base Image"
  echo "UNAME $UNAME"
  docker build --platform linux/$UNAME --no-cache -t ubuntu-dev:latest .
fi

DOCKER_PS=$(docker ps | grep -v CONTAINER | grep "CloudTools")
if [[ -z "$DOCKER_PS" ]]; then
  echo "INFO: Starting CloudTools Image"
  RUN=$(docker ps -a | grep -v "REPO" | grep CloudTools | grep Exited)
  if [[ -z "$RUN" ]]; then
    docker run -it --name CloudTools -d -p8081:8081 --platform linux/$UNAME --volume $(pwd):/home/ubuntu ubuntu-dev:latest
  else
    docker start CloudTools
  fi
fi

echo "INFO: Login CloudTools"
docker exec -it CloudTools /bin/bash

#!/bin/bash
IMAGE=$(docker images ubuntu-dev | grep -v "REPO")
UNAME=$(uname -m)

echo "IMAGE: $IMAGE"
echo "UNAME: $UNAME"

if [[ "$1" == "clean" ]]; then
  docker stop /cloud-tools
  docker rm /cloud-tools
  exit 0
fi

if [[ -z "$IMAGE" ]]; then
  echo "INFO: Building Base Image"
  echo "UNAME $UNAME"
  docker build --platform linux/$UNAME --no-cache -t ubuntu-dev:latest .
fi

DOCKER_PS=$(docker ps | grep -v CONTAINER | grep "cloud-tools")
if [[ -z "$DOCKER_PS" ]]; then
  docker run -it --name CloudTools -d -p8081:8081 --platform linux/$UNAME --volume $(pwd):/home/ubuntu ubuntu-dev:latest
fi

docker exec -it CloudTools /bin/bash

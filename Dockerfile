FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update && \
    apt-get -y install \
    lsb-release \
    htop \
    curl \
    netcat \
    jq \
    wget \
    vim \
    git \
    net-tools \
    iputils-ping \
    awscli \
    python3-pip \
    virtualenv \
    openjdk-11-jre \
    bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir /root/.aws
RUN mkdir -p /home/ubuntu
WORKDIR /home/ubuntu
ENTRYPOINT ["bash"]

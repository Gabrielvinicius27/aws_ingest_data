#imagem Docker do node, versão alpine.
FROM node:alpine

#RUN npm install -g npm@latest

# Adding bash in alpine
RUN apk update && apk add bash

# Install pip
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache

# Install aws cli
RUN pip3 install awscli

# Install Serverless
RUN npm config set strict-ssl false && \
    npm install -g serverless@1.29.2 && \
    export PATH=$PATH:/usr/local/bin/serverless
WORKDIR /mnt
CMD [ "serverless", "deploy", "--force"]

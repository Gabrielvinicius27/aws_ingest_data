FROM node:14.15.1-alpine
USER root
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

# Copiar o serverless.yaml e requirements.txt da pasta local para a imagem
COPY /container_mnt/aws-ingest-data/. /mnt/aws-ingest-data/.

WORKDIR /mnt/aws-ingest-data

# Instala as bibliotecas do arquivo requirements.txt
RUN pip3 install -r requirements.txt

# Instala o plugin do serverless que interage com o requirements.txt
RUN sls plugin install -n serverless-python-requirements

# Copia o
COPY . /mnt/aws-ingest-data

CMD [ "sls", "deploy", "--force"]

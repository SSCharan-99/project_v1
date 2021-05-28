FROM ubuntu:20.04
ENTRYPOINT []
FROM node as prod

WORKDIR /app

COPY package*.json ./

RUN npm install

WORKDIR /app/client

COPY ./package*.json ./

RUN npm install

WORKDIR /app

COPY . .

ENV NODE_ENV=production
RUN chmod +x /app/start_services.sh


RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==2.6.0
ADD . /app/
RUN chmod +x /app/services.sh
CMD ["npm","start","/app/start_services.sh"]


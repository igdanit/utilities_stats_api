FROM node:20.3
WORKDIR /etc/indicationAPI
COPY ./dist .
COPY ./package.json .
COPY ./package-lock.json .
RUN npm install
CMD ["node", "main.js"]

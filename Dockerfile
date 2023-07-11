FROM node:20.3
WORKDIR /code
COPY /dist /API
WORKDIR API
CMD ["node", "main.js"]

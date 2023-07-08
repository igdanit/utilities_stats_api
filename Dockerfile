FROM node:20.3
WORKDIR /code
COPY /dist /API
CMD ["node", "main.js"]

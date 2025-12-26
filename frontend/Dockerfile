FROM node:20-slim

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 5173

# Commande pour autoriser l'accès externe au container
CMD ["npm", "run", "dev", "--", "--host"]
FROM node:20-alpine

WORKDIR /app

# Copy package files first (better caching)
COPY package*.json ./

# Install everything (including dev deps like tailwind)
RUN npm install

# Copy full project
COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]
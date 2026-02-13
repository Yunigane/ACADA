FROM node:20-bookworm-slim

# Install Python 3 and build dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install n8n globally
RUN npm install -g n8n

# Create n8n data directory and set permissions
RUN mkdir -p /home/node/.n8n && chown -R node:node /home/node/.n8n

# Set up work directory
WORKDIR /home/node
USER node

# Expose n8n port
EXPOSE 5678

# Start n8n
ENTRYPOINT ["n8n"]

FROM python:3.11

WORKDIR /app

# 1. Instala Node.js primeiro
RUN apt-get update && apt-get install -y nodejs npm

# 2. Copia os arquivos de dependências
COPY package.json package-lock.json ./

# 3. Instala dependências do Node (incluindo Tailwind)
RUN npm install
RUN npm install -D tailwindcss postcss autoprefixer

# 4. Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia todo o projeto
COPY . .

# 6. Gera os arquivos CSS (com verificação)
RUN echo "Verificando arquivos..." && \
    ls -la static/css/ && \
    npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --minify

EXPOSE 8000

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
# 🩺 Projeto Kaya Doc

Sistema desenvolvido com **Python**, **Django** e **Tailwind CSS**, com o objetivo de cadastrar, listar e exibir os detalhes dos médicos da empresa **Kaya Mind**.

## ✨ Funcionalidades

- 📋 Listagem e detalhes dos médicos;
- 🛠 Cadastro de médicos via Django Admin;
- 🔍 Filtro por especialidade e valores;
- 🔎 Busca por nome e especialidade;
- 🤖 **Funcionalidade extra**: Chat com Inteligência Artificial usando a **API da OpenAI**  
  > É necessário informar uma **API KEY** para utilizar o chat.

---

## ⚙️ Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- [Node.js (LTS)](https://nodejs.org/en/download)
- Tailwind CSS

---

## 💻 Instalação dos Pré-requisitos

### 🪟 Windows

#### Python

1. Acesse: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Baixe o instalador para Windows
3. Execute o instalador e **marque a opção "Add Python to PATH"**
4. Verifique a instalação:

```bash
python --version
```

#### Node.js

1. Acesse: [https://nodejs.org/en/download](https://nodejs.org/en/download)
2. Baixe e instale a versão LTS
3. Verifique a instalação:

```bash
node --version
npm --version
```

#### Tailwind CSS

```bash
npm install tailwindcss @tailwindcss/cli
```

---

### 🐧 Linux

#### Python
##### Python geralmente vem pré-instalado. Verifique com:

```bash
python3 --version
# ou instale:
sudo apt update
sudo apt install python3
```

#### Node.js

```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
```

##### Verifique a instalação:
```bash
node --version
npm --version
```

#### Tailwind CSS

```bash
npm install tailwindcss @tailwindcss/cli
```

---

## 🚀 Executando o Projeto

### Clonando o Repositório

```bash
git clone https://github.com/lyalima/desafio_kaya.git
cd desafio_kaya
```

### Criando e Ativando o Ambiente Virtual

#### Windows

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalando Dependências

```bash
pip install -r requirements.txt
```

### Aplicando as Migrações

```bash
# Windows
python manage.py migrate

# Linux
python3 manage.py migrate
```

### Criando Superusuário

```bash
# Windows
python manage.py createsuperuser

# Linux
python3 manage.py createsuperuser
```

---

## 💡 Rodando o Projeto

### 1. Executando o Tailwind CSS

#### Windows

```bash
npx @tailwindcss/cli -i ./static/css/input.css -o ./static/css/output.css --watch
```

#### Linux

```bash
tailwindcss -i static/css/input.css -o static/css/output.css --watch
```

### 2. Rodando o Servidor Django

```bash
# Windows
python manage.py runserver

# Linux
python3 manage.py runserver
```

---

## ⚙️ Usando Makefile (opcional)

### Windows

1. No arquivo `Makefile`, altere a 5ª linha para:

```make
python manage.py runserver
```

2. Instale o [Chocolatey](https://chocolatey.org/install):

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = `
[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

3. Execute o projeto:

```bash
make dev
```

### Linux

1. No arquivo `Makefile`, altere a 5ª linha para:

```make
python3 manage.py runserver
```

2. Execute o projeto:

```bash
make dev
```

---

## 🌐 Acesso

### O projeto estará disponível em:  
👉 [http://127.0.0.1:8000/medicos](http://127.0.0.1:8000/medicos)

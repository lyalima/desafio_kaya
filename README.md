# Projeto Kaya Doc
Projeto feito com Python, Django e Tailwind CSS, com o objetivo 
de cadastrar, listar e mostrar os detalhes sobre os médicos da empresa Kaya Mind.

O projeto conta com funcionalidades como: 
  - Listagem e detalhes dos médicos;
  - Cadastro de médicos via Django Admin;
  - Filtro de médicos por especialidade e valores;
  - Busca de médicos por nome e especialidade;
  - Funcionalidade extra: Chat com Inteligência Artificial usando a API da OpenAI
  (É necessário uma API KEY para usar o chat).

## Pré-requisitos

- Python 3.10 ou superior
- Node JS
- Tailwind CSS

## Instalação dos pré-requisitos

### No Windows

#### Python

##### Acesse o site oficial: https://www.python.org/downloads/

##### Baixe o instalador para Windows (versão recomendada)

##### Execute o instalador

##### IMPORTANTE: Marque a opção "Add Python to PATH" antes de instalar

##### Siga as instruções do instalador

##### Verifique a instalação com o comando no CMD:

```bash
python --version
```

#### Node JS

##### Acesse o site oficial: https://nodejs.org/

##### Baixe a versão LTS para Windows

##### Execute o instalador com as configurações padrão

##### Verifique a instalação com:

```bash
node --version
npm --version
```

#### Tailwind CSS

```bash
npm install tailwindcss @tailwindcss/cli
```

### No Linux 

#### Python

##### Abra o terminal (Ctrl+Alt+T)

##### Python geralmente vem pré-instalado. Verifique com:

```bash
python3 --version
```

##### Se necessário, instale com:

```bash
sudo apt update
sudo apt install python3
```

#### Node JS

##### No terminal, execute:

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

##### No terminal execute:

```bash
npm install tailwindcss @tailwindcss/cli
```

## Baixando e Executando o projeto

### Clonando o Repositório

#### No terminal execute:

```bash
git clone https://github.com/lyalima/gerenciador_de_tarefas.git
cd gerenciador_de_tarefas
```

### Criando e ativando o ambiente virtual 

#### No Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### No Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalação de dependências 

```bash
pip install -r requirements.txt
```

### Aplicando as migrações

```bash
python manage.py migrate
```

### Criando um superusuário

```bash
python manage.py createsuperuser
```

### Execute o projeto com:

#### Executando o Tailwind

```bash
tailwindcss -i static/css/input.css -o static/css/output.css --watch
```

#### Executando o servidor Django

```bash
python manage.py runserver
```

### Ou use:

```bash
make dev
```

### A API estará disponível em http://127.0.0.1:8000/.

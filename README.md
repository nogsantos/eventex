# Eventex

## Virtual env

No python 3, o virtual env já vem na biblioteca padrão

### Criação no diretório de trabalho

```bash
python -m venv .[nome-do-diretorio-de-trabalho]
```

### Ativar o virtual env

```bash
source .[nome-do-diretorio-de-trabalho]/bin/activate
```

### Instalação do Django

Com o virtual env ativo, instalar as dependências do projeto

```bash
pip install django
```

### Criar um projeto Django

Após a instalação da lib, para iniciar um novo projeto django

```bash
django-admin startproject [nome-do-projeto] [local] # Para criar no diretório corrente use '.'
```

## Ajustes dos projeto

### Simplificando a chamanda ao manage.py

Como sempre iremos trabalhar com o virtual env ativo, haverá uma variável de ambiente definindo o path dele, dessa forma, para criar um alias ao `manage.py`, basta apenas digitar:

```bash
alias manage='python $VIRTUAL_ENV/../manage.py'
```

Assim, para uma nova chamada ao `manage.py` em qualquer diretório do sistema, basta digitar:

```bash
$ manage

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
```

### Criando uma Django app

Uma biblioteca python que segue algumas convensões do django

```bash
manage startapp [nome]
```

## Expessão regular para subistituir valores

Seleciona todas as propriedades `src e hrf` que pertencem as tags `img, css e js`

```regex
(src|href)="((img|css|js).\*?)"
```

Substitue pelo primeiro grupo `$1` `src e hrf` com os valores do segundo grupo selecionad `$2` juntamente com a tag static

```regex
$1="{% static '$2'%}"
```

## Config lib

- [python-decouple](https://pypi.org/project/python-decouple/)
  - Substitui valores pelas variáveis de ambiente. Também é possível definir valores padrões
- [dj-database-url](https://pypi.org/project/dj-database-url/)
  - Extrai as informações necessárias para a configuração do banco de dados através da leitura de uma url. Essa lib consegue mapear atraves de uma url, todos os parâmetros do dicionário de configuração do banco de dados da aplicação
- [dj-static](https://pypi.org/project/dj-static/)
  - Uma aplicação wisg padrão do python, que ficará na frente do django para servir os arquivos estáticos.

#### Publicação no Heroku

Para publicar uma aplicação python no heroku, duas lib são necessárias, porém, não precisam ser instaladas no ambiente de desenvolvimento, dessa forma, apenas apontando-as no arquivo requirements é o suficiente.

- [gunicorn](https://pypi.org/project/gunicorn/)
  - É o servidor web que recebe as requisições e as repassa para o django
- [psycopg2](https://pypi.org/project/psycopg2/)
  - Drive do banco PostgreSQL para o django utilizado pelo heroku

# Eventex

[![Build Status](https://travis-ci.org/nogsantos/eventex.svg?branch=master)](https://travis-ci.org/nogsantos/eventex) [![Maintainability](https://api.codeclimate.com/v1/badges/16789efdf99182761d1a/maintainability)](https://codeclimate.com/github/nogsantos/eventex/maintainability) [![Coverage Status](https://coveralls.io/repos/github/nogsantos/eventex/badge.svg?branch=master)](https://coveralls.io/github/nogsantos/eventex?branch=master)

## Setup

1. Clone o repositorio
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as dependencias
5. Configure a instancia com o .env
6. Execute os testes

```console
git clone git@github.com:nogsantos/eventex.git
cd eventex
python -m venv .eventex
source .eventex/bin/activate
pip install -r requirements-dev.txt
cp contrib/env.sample .env
python manage.py test
```

## Publish

Dependencia [The Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

1. Crie uma instancia
2. Envie as configuracoes para o heroku
3. Defina uma SECRET_KEY segura para a instancia
4. Defina DEBUG=False
5. Configure o servico de email
6. Envie o codigo

```console
heroku create my-new-instance
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBU=False
# configura o email
git push heroku master --force
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

## Heroku

**Autenticar na conta**

```bash
$ heroku login
```

**Criar o app**

```bash
heroku apps:create eventex-nogsantos
```

**Abriar a aplicação no navegador**

```bash
heroku open
```

**Configura as variáveis de ambiente**

```bash
heroku config:set [CHAVE]=[VALOR]
```

**Visualiza as configuracoes definidas no heroku**

```bash
heroku config
```

**Envia o projeto**

```bash
git push heroku master --force
```

**Executar comandos no heroku**

Para executar as migrations no heroku, no terminal

```bash
heroku run python manage.py migrate
```

Criar o superuser do django

```bash
heroku run python manage.py createsuperuser
```

**Habilita sendgrid para envio de emails**

> Ao abrir a documentação do sendgrind, no heroku está exemplificado usando o pacote do próprio sendgrid, sendo necessário a instalação dele no projeto para isso. No caso, nesse projeto, não será utilizado esse pacote, usaremos o próprio smtp para isso.

```bash
heroku addons:create sendgrid:starter
--return
Creating sendgrid:starter on ⬢ eventex-nogsantos... free
Created sendgrid-animated-85358 as SENDGRID_PASSWORD, SENDGRID_USERNAME
Use heroku addons:docs sendgrid to view documentation
```

## Docs

Em docs, os módulos possuirão os requisitos

### Cenários

Devem possuir as sessões de:

- **Contexto**: Descreve o estado inicial
- **Ação**: O que irá ocorrer após o estado inicial
- **Resultado / Expectativa**: Após a ação, o que deve ocorrer

## Dev environment

No projeto, está disponível o `django-extensions`, e em desenvolvimento o `Jupyter`. Juntos possibilitam o uso do notebook para facilitar o desenvolvimento e testes.

```bash
python manage.py shell_plus --notebook
```

## Django model

**dumpdata**

O comando `dumpdata` gera um dump em `json` dos modelos criados nos apps para visualizacao no terminal

```bash
python manage.py dumpdata --indent 4 subscriptions
```

## Django admin

**Create super user**

```bash
python manage.py createsuperuser
```

## Expressões regulares

### Módulos do python

- `match`: `re.match('abc', 'abc')`
- `search`: `re.search('abc', 'efgabc')`
- `findall`: `re.findall('abc', '123abc456abc')`

> Metacaracteres das expressões regulares.
> Ponto (.) == qualquer caracter, exceto nova linha (\n)
> Âncoras (^\$) == início e fim de string
> Classe de caracter ([])

### Sequências especiais definidas por padrão

Todas a sequencias especiais usam a `\`

- `\d` == [0-9]
- `\D` == [^0-9] **Negação da classe**
- `\s` == [\t\n\r\f\v]
- `\S` == [^\t\n\r\f\v] **Negação da classe**
- `\w` == [a-zA-Z0-9_]
- `\W` == [^a-za-z0-9_] **Negação da classe**

> É importante e recomendado utilizar o `r` raw string para evitar que o python interprete caracteres especiais na avaliação do pattern. Ex.: `match(r'\\section', '\\section\n')`

### Meta characteres

- `｜` pipe, representa o `OR`

### Repetições

Usa-se a notação com `{}`

**Quantidades específicas de repetições**

- `{int}` Exatamente a quantidade de digitos

```regex
match(r'\d{4}', '123456')
# Encontra '1234'
```

**Quantidades mínima de repetições**

- `{from, to}` de até

```regex
match(r'\d{2, }', '123456')
```

# Eventex

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

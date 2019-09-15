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

## Publicar app no heroku

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

**Envia o projeto**

```bash
git push heroku master --force
```

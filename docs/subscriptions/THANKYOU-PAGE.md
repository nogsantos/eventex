# Cenário

### Contexto

**Dado que** um visitante se inscreve em `/subscription/`

### Ação

**Quando** a operacao e bem sucedida

### Resultado / expectativa

**Então** o sistema redireciona para `/subscription/uuid/`

- **e** o identificador do usuario nao pode ser a sua primary key ou um identificador sequencial
- **e** informa que ele sera contactado
- **e** exibe os dados fornecidos na inscricao

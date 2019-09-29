# Cenário

### Contexto

**Dado que** um visitante acessa `/subscription/`

### Ação

**Quando** ele preenche o formulário

- **e** os campos são **`nome`, `email`, `cpf` e `telefone`** são informados
- **e** ele clica em enviar

### Resultado / expectativa

**Então** o sistema envia um email de confirmação

- **e** o remetente é `contato@eventex.com.br`
- **e** o destinatário é o visitante
- **e** o remetente está em cópia carbono
- **e** o visitante é redirecionado para `/subscription/`
- **e** o visitante vê uma mensagem de sucesso

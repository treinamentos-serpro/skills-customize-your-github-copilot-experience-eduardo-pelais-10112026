# 📘 Atividade: Construindo REST APIs com FastAPI

## 🎯 Objetivo

Construir uma API REST com FastAPI, criando endpoints, validando dados com Pydantic e implementando operações CRUD com os códigos de status HTTP corretos.

## 📝 Tarefas

### 🛠️ Primeiros Endpoints GET

#### Descrição
Crie uma aplicação FastAPI que responda a requisições GET. Para executar o servidor, instale as dependências com `pip install fastapi uvicorn` e rode `uvicorn starter-code:app --reload` no diretório da atividade. Acesse `http://127.0.0.1:8000/docs` para testar seus endpoints pelo navegador.

#### Requisitos
O programa concluído deve:

- Possuir um endpoint `GET /` que retorne `{"message": "Hello, FastAPI!"}`
- Possuir um endpoint `GET /hello/{name}` que retorne `{"message": "Hello, <name>!"}` com o nome informado na URL
- Possuir um endpoint `GET /square/{number}` que receba `number` como inteiro e retorne `{"number": 4, "square": 16}` ao acessar `GET /square/4`
- Retornar erro `422` quando `number` não for um inteiro (ex.: `GET /square/abc`)

### 🛠️ Modelos de Dados e Criação de Itens

#### Descrição
Defina um modelo Pydantic para representar um item da loja e crie um endpoint para cadastrar novos itens. O FastAPI usa o modelo para validar automaticamente o corpo da requisição JSON.

#### Requisitos
O programa concluído deve:

- Definir uma classe `Item` com os campos `name` (texto), `price` (número maior que zero) e `in_stock` (booleano, com valor padrão `True`)
- Possuir um endpoint `POST /items` que receba um `Item` no corpo da requisição
- Armazenar o item no dicionário `items` com um `id` inteiro atribuído automaticamente (1, 2, 3...)
- Retornar o item cadastrado, incluindo o `id`, com o código de status `201`
- Retornar erro `422` quando `price` for zero ou negativo, ou quando `name` estiver ausente
- Exemplo de corpo da requisição:
  ```json
  {"name": "Caneca", "price": 25.5}
  ```

### 🛠️ CRUD Completo com Tratamento de Erros

#### Descrição
Complete a API com as operações de listar, buscar, atualizar e remover itens. Quando um item não existir, a API deve responder com `404 Not Found`, usando `HTTPException`.

#### Requisitos
O programa concluído deve:

- Possuir um endpoint `GET /items` que retorne a lista de todos os itens cadastrados
- Aceitar o parâmetro de consulta opcional `max_price` em `GET /items` para retornar apenas itens com preço menor ou igual ao valor informado
- Possuir um endpoint `GET /items/{item_id}` que retorne o item correspondente
- Possuir um endpoint `PUT /items/{item_id}` que substitua os dados do item pelos dados enviados no corpo da requisição
- Possuir um endpoint `DELETE /items/{item_id}` que remova o item e retorne `204 No Content`
- Retornar `404` com a mensagem `"Item not found"` quando o `item_id` informado não existir em `GET`, `PUT` ou `DELETE`

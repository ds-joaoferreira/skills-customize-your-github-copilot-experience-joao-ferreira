# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar um catálogo de livros usando FastAPI. Ao concluir a atividade, você saberá criar rotas HTTP, validar dados com modelos Pydantic e retornar respostas apropriadas para operações de leitura e escrita.

## 📝 Tasks

### 🛠️ Criar a Rota Inicial da API

#### Descrição

Complete a rota inicial do projeto e crie um endpoint `GET /books` que retorne o catálogo de livros armazenado em memória.

#### Requisitos

O programa concluído deve:

- Iniciar uma aplicação FastAPI com `uvicorn starter-code:app --reload`
- Responder a `GET /` com uma mensagem identificando a API
- Responder a `GET /books` com uma lista JSON de livros
- Representar cada livro com `id`, `title`, `author` e `year`

### 🛠️ Adicionar Validação e Cadastro de Livros

#### Descrição

Use um modelo Pydantic para validar os dados de um novo livro e implemente `POST /books`. O identificador deve ser criado pela API, sem ser enviado pelo cliente.

#### Requisitos

O programa concluído deve:

- Definir um modelo `BookCreate` com `title`, `author` e `year`
- Aceitar novos livros por meio de `POST /books`
- Gerar um `id` único para cada novo livro
- Retornar o livro criado com status HTTP `201`
- Rejeitar requisições que não tenham campos obrigatórios ou tenham tipos inválidos

Exemplo de corpo da requisição:

```json
{
  "title": "The Little Prince",
  "author": "Antoine de Saint-Exupery",
  "year": 1943
}
```

### 🛠️ Implementar Consulta e Remoção por ID

#### Descrição

Complete os endpoints para buscar um livro específico e removê-lo do catálogo. A API deve informar claramente quando o livro solicitado não existe.

#### Requisitos

O programa concluído deve:

- Responder a `GET /books/{book_id}` com o livro correspondente
- Responder a `DELETE /books/{book_id}` removendo o livro e retornando uma confirmação
- Retornar status HTTP `404` para um `book_id` inexistente
- Manter os endpoints organizados com métodos HTTP e caminhos RESTful
- Testar as rotas pela documentação interativa em `/docs`

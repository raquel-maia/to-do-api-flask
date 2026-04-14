# To-Do List API

API REST para gerenciamento de tarefas. O projeto tem como objetivo demonstrar a implementação de um CRUD funcional, aplicando boas práticas de arquitetura, organização de código e integração com banco de dados NoSQL.

---

# 🚀 Tecnologias

* **Backend**: Python (Flask)
* **Banco de Dados**: MongoDB Atlas (NoSQL)
* **Arquitetura**: Arquitetura em Camadas (Controller, Service, Repository, Config, Schemas)

---

# 📋 Funcionalidades

* **CRUD de Tarefas**: Criação, listagem, busca por ID, atualização e remoção de tarefas.
* **Filtro por status**: Permite listar tarefas com base no status.
* **Contagem de tarefas por status**: Implementação de aggregation no MongoDB para análise de dados.

### 📊 Exemplo de retorno (contagem por status)

```json
[
  {
    "status": "pending",
    "count": 2
  },
  {
    "status": "completed",
    "count": 3
  }
]
```

---

### Validações de Negócio

* Título obrigatório (3-100 caracteres)
* Validação de status (`pending`, `in_progress`, `completed`, `cancelled`)
* Validação de prioridade (`low`, `medium`, `high`)
* Data de vencimento validada (não permite datas no passado)
* Bloqueio de edição para tarefas com status `completed`

---

# 📂 Estrutura do Projeto

O projeto foi organizado em uma arquitetura de camadas para garantir a separação de responsabilidades e facilitar a manutenção:

**/config**
Contém as configurações globais da aplicação e a lógica de conexão com o banco de dados.

**/controllers**
Responsável por receber as requisições HTTP e retornar as respostas da API.

**/services**
Camada que contém as regras de negócio e validações da aplicação.

**/repositories**
Responsável pela comunicação direta com o banco de dados (MongoDB).

**/schemas**
Define a estrutura e serialização dos dados retornados pela API.

---

# 🔄 Fluxo da Aplicação

A requisição percorre diferentes camadas da aplicação até retornar uma resposta ao cliente.

```
Cliente (Postman / Frontend)
│
▼
HTTP Request (GET, POST, PUT, DELETE)
│
▼
Controller (Flask Routes)
Recebe a requisição e extrai os dados
(request.json / request.args)
│
▼
Service Layer (TaskService)
Aplica regras de negócio:
- validações
- regras de status
- formatação de datas
- tratamento de erros
│
▼
Repository Layer
Responsável pelo acesso ao banco:
- consultas
- inserções
- atualizações
- remoções
│
▼
MongoDB (NoSQL)
Armazenamento das tarefas
│
▼
Repository retorna os dados
│
▼
Service aplica formatação com schemas
│
▼
Controller retorna JSON
(jsonify + status HTTP)
│
▼
Cliente recebe a resposta da API
```

---

# 🛠️ Configuração e Execução

## Pré-requisitos

* Python 3.x instalado
* Acesso a uma instância do MongoDB (o projeto utiliza **MongoDB Atlas**)

## Instalação

### 1️⃣ Clone o repositório

```bash
git clone <link-do-seu-repo>
cd <nome-do-projeto>
```

### 2️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure a conexão com o banco de dados

Configure a variável de ambiente:

```
MONGO_URI=sua_string_de_conexao
```

Também é necessário adicionar o IP da sua máquina no **Network Access** no painel do MongoDB Atlas.

### 4️⃣ Execute a aplicação

```bash
python app.py
```

---

# 🧪 Testes

A API foi validada utilizando **Postman**.

As rotas seguem o padrão **RESTful**, retornando códigos HTTP adequados:

* **200** – Sucesso
* **201** – Recurso criado
* **400** – Erro de validação
* **404** – Recurso não encontrado
* **500** – Erro interno do servidor

---

# 🧠 Notas de Desenvolvimento

**Arquitetura em Camadas**
O projeto utiliza separação de responsabilidades entre Controller, Service e Repository para melhorar organização, manutenção e escalabilidade do código.

**Aggregation com MongoDB**
Foi implementado o uso de aggregation (`$group` e `$sum`) para gerar métricas de tarefas por status, demonstrando capacidade de análise de dados além do CRUD básico.

**Tratamento de Erros**
Foram implementados tratamentos de exceções para garantir respostas estruturadas e evitar falhas inesperadas na API.

---

Desenvolvido por **Raquel Maia**

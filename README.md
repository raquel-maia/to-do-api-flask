# To-Do List itaú

API REST para gerenciamento de tarefas desenvolvida como desafio técnico para a vaga de **Analista de Engenharia de TI Júnior**. O foco do projeto é a implementação de um CRUD funcional, seguindo boas práticas de arquitetura, organização de código e integração com banco de dados NoSQL.

## 🚀 Tecnologias

* **Backend**: Python (Flask)

* **Banco de Dados**: MongoDB Atlas (NoSQL) 

* **Arquitetura**: Arquitetura em Camadas (Controller, Service, Repository, Config, Schemas)

## 📋 Funcionalidades

* **CRUD de Tarefas**: Criação, listagem, busca por ID, atualização e remoção de tarefas.

* **Validações de Negócio**:

* Título obrigatório (3-100 caracteres).

* Validação de status (`pending`, `in_progress`, `completed`, `cancelled`).

* Validação de prioridade (`low`, `medium`, `high`).

* Data de vencimento validada (não permite datas no passado).

* Bloqueio de edição para tarefas com status `completed`.

## 📂 Estrutura do Projeto
O projeto foi organizado em uma arquitetura de camadas para garantir a separação de responsabilidades e facilitar a manutenção:

* /config: Contém as configurações globais da aplicação e a lógica de conexão com o banco de dados.

* /controllers: Atua como a interface da API, responsável por receber as requisições HTTP e retornar as respostas adequadas ao cliente.

* /repositories: Camada de acesso aos dados, responsável pela interação direta com o MongoDB.

* /schemas: Define a estrutura dos objetos e a serialização dos dados, garantindo a consistência das informações.

* /services: Contém as regras de negócio e as validações da aplicação, atuando como o núcleo do sistema.


## 🛠️ Configuração e Execução

### Pré-requisitos

* Python 3.x instalado.
* Acesso a uma instância do MongoDB (o projeto utiliza **MongoDB Atlas**).

### Instalação

1. Clone o repositório:
```bash
git clone <link-do-seu-repo>
cd <nome-do-projeto>

```

2. Instale as dependências:
```bash
pip install -r requirements.txt

```

3. Configure a conexão com o banco de dados:
* O projeto está configurado para o **MongoDB Atlas**.
* Certifique-se de configurar a variável de ambiente `MONGO_URI` com a sua string de conexão.

* Configure o IP da sua máquina no "Network Access" (Whitelist) do seu painel do Atlas.


4. Execute a API:
```bash
python app.py

```

## 🧪 Testes

A API foi validada via Postman. As rotas seguem o padrão RESTful com códigos de resposta HTTP coerentes (200, 201, 400, 404, 500).


### Notas de Desenvolvimento

* **Código Limpo**: O projeto foi estruturado para garantir a separação de responsabilidades (camadas Controller, Service e Repository), facilitando a manutenção.

* **Tratamento de Erros**: Implementado tratamento de exceções para garantir respostas estruturadas ao cliente, evitando erros silenciosos.

Desenvolvido por: Raquel Maia


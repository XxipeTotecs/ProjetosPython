# Din-Din API

Desafio-Back-end-03-dindin-dbeifood

## Descrição

Bem-vindo(a) à documentação da nossa API de gestão financeira Din-Din API. Com esta API, você poderá gerenciar com muito mais conforto a sua vida financeira.

A nossa API foi desenvolvida para simplificar o controle financeiro das pessoas. Com ela, você poderá acompanhar saldos, gerar relatórios de transferências e consultar extratos entre outras funcionalidades.

Nossa documentação é abrangente e oferece todas as informações necessárias para você começar a utilizar a API. Ela inclui detalhes sobre os endpoints disponíveis, os parâmetros de entrada e saída, exemplos de código, autenticação e segurança, entre outros.

A documentação também apresenta as melhores práticas para utilização da API e dicas para otimizar o desempenho e a segurança da integração utilizando o padrão REST.

Caso precise de ajuda, nossa equipe de suporte técnico está pronta para ajudá-lo(a) a implementar a API da melhor forma possível.

Estamos animados em tê-lo(a) como nosso(a) cliente e esperamos que a nossa API de gestão financeira seja uma ferramenta valiosa para sua empresa. Obrigado por escolher a nossa plataforma e aproveite ao máximo nossa documentação!

Atenciosamente,
Equipe de desenvolvimento da Din-Din API.

## Instalação

1. Clone este repositório: `git clone git@github.com:rdvid/desafio-backend-03-dindin-dbeifood.git`
2. Navegue até a pasta do seu repositório local: `cd desafio-backend-03-dindin-dbeifood`
3. Instale as dependencias necessárias: `npm install`
4. Inicialize o projeto no terminal: `npm run dev`

## Como Usar

Uma vez rodando, a nossa API pode ser acessada através de requisições HTTP por um cliente local.

### Endpoints

Endpoins disponíveis até o momento:

### **Login do usuário**

- `POST /login`: Essa rota é uma tela de login, ela demanda um objeto no corpo da requisição, contendo "email" e "senha" (Atenção com a estrutura do objeto, é fundamental que a requisição respeite as nomenclaturas). Esta rota retorna o usuário cadastrado e um Token JWT que pode e deve ser usado para acessar demais rotas referentes as credenciais informadas.

#### **Exemplo de Requisição**

```javascript
// POST /login
{
    "email": "jose@email.com",
    "senha": "123456"
}
```

#### **Exemplo de Resposta**

```javascript
// HTTP Status 200
{
    "usuario": {
        "id": 1,
        "nome": "José",
        "email": "jose@email.com"
    },
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiaWF0IjoxNjIzMjQ5NjIxLCJleHAiOjE2MjMyNzg0MjF9.KLR9t7m_JQJfpuRv9_8H2-XJ92TSjKhGPxJXVfX6wBI"
}
```

### **Cadastrar usuário**

- `POST /usuario`: Esta rota é uma tela de cadastramento, com ela novos usuários podem se registrar e assim fazer uso da aplicação. Ela recebe um Objeto JSON no corpo da requisição com os campos/propriedades: "nome", "email" e "senha". (não se preocupe, a senha é armazenada de forma segura no banco de dados através de criptografia aplicada):

#### **Examplo de requisição**

```javascript
// POST /usuario
{
    "nome": "José",
    "email": "jose@email.com",
    "senha": "123456"
}
```

#### **Exemplos de resposta**

```javascript
// HTTP Status 200 / 201 / 204
{
    "id": 1,
    "nome": "José",
    "email": "jose@email.com"
}
```

- `PUT /usuario`: Essa rota serve para editar as informações de um usuário já existente dentro da plataforma. "nome", "email" e "senha" novos são necessários nessa operação.

#### **Exemplo de requisição**

```javascript
// PUT /usuario
{
    "nome": "José de Abreu",
    "email": "jose_abreu@email.com",
    "senha": "j4321"
}
```

#### **Exemplos de resposta**

```javascript
// HTTP Status 200 / 201 / 204
// Sem conteúdo no corpo (body) da resposta
```

### **Listar categorias**

- `GET /categoria`: Essa rota serve para listar todas as categorias de transações registradas até o momento.

#### **Exemplo de requisição**

```javascript
// GET /categoria
// Não é necessário enviar nenhum dado para essa operação.
```

#### **Exemplos de resposta**

```javascript
// HTTP Status 200 / 201 / 204
[
  {
    id: 1,
    descricao: "Roupas",
  },
  {
    id: 2,
    descricao: "Mercado",
  },
];
```

```javascript
// HTTP Status 200 / 201 / 204
[];
```

### **Listar transações**

- `GET /transacao/`: Essa rota lista todas as transações da conta conectada.

#### **Exemplo de requisição**

```javascript
// GET /transacao
// Não é necessário enviar nenhum dado para essa operação.
```

#### **Exemplos de resposta**

```javascript
// HTTP Status 200 / 201 / 204
[
  {
    id: 1,
    tipo: "saida",
    descricao: "Sapato amarelo",
    valor: 15800,
    data: "2022-03-23T15:35:00.000Z",
    usuario_id: 5,
    categoria_id: 4,
    categoria_nome: "Roupas",
  },
  {
    id: 3,
    tipo: "entrada",
    descricao: "Salário",
    valor: 300000,
    data: "2022-03-24T15:30:00.000Z",
    usuario_id: 5,
    categoria_id: 6,
    categoria_nome: "Salários",
  },
];
```

```javascript
// HTTP Status 200 / 201 / 204
[];
```

### **Detalhar uma transação do usuário logado**

- `GET /transacao/:id`: Ao especificar o numero de alguma transação na url, é retornado o detalhamento dessa transação.

#### **Exemplo de requisição**

```javascript
// GET /transacao/2
// Sem conteúdo no corpo (body) da requisição
```

#### **Exemplos de resposta**

```javascript
// HTTP Status 200 / 201 / 204
{
    "id": 3,
    "tipo": "entrada",
    "descricao": "Salário",
    "valor": 300000,
    "data": "2022-03-24T15:30:00.000Z",
    "usuario_id": 5,
    "categoria_id": 6,
    "categoria_nome": "Salários",
}
```

### **Registar uma transacao**

- `POST /transacao`: Essa rota serve para registrar uma transação. Para que isso aconteça é necessário que, no corpo da requisição, seja adicionado um objeto JSON contendo "tipo", "descricao", "valor", "data", "id da categoria da transacao" (Atente-se a forma como as propriedades do JSON são escritas, é necessário respeitar a verbosidade).

#### **Exemplo de requisição**

```javascript
// POST /transacao
{
    "tipo": "entrada",
    "descricao": "Salário",
    "valor": 300000,
    "data": "2022-03-24T15:30:00.000Z",
    "categoria_id": 6
}
```

#### **Exemplos de resposta**

```javascript
// HTTP Status 200 / 201 / 204
{
    "id": 3,
    "tipo": "entrada",
    "descricao": "Salário",
    "valor": 300000,
    "data": "2022-03-24T15:30:00.000Z",
    "usuario_id": 5,
    "categoria_id": 6,
    "categoria_nome": "Salários",
}
```

### **Atualizar transação do usuário logado**

- `PUT /transacao/:id`: Ao utilizar o metodo PUT em uma transação especificada através de um ID, é possível alterar algumas informações como: "descricao", "valor", "data", "categoria_id" e "tipo", passados através de um objeto JSON informado no corpo da requisição.

#### **Exemplo de requisição**

```javascript
// PUT /transacao/2
{
	"descricao": "Sapato amarelo",
	"valor": 15800,
	"data": "2022-03-23 12:35:00",
	"categoria_id": 4,
	"tipo": "saida"
}
```

#### **Exemplos de resposta**

```javascript
// HTTP Status 200 / 201 / 204
// Sem conteúdo no corpo (body) da resposta
```

### **Excluir transação do usuário logado**

- `DELETE /transacao/:id`: Essa rota deleta uma transação especifica.

#### **Exemplo de requisição**

```javascript
// DELETE /transacao/2
//
```

#### **Exemplos de resposta**

```javascript
// HTTP Status 200 / 201 / 204
// Sem conteúdo no retorno
```

### **Obter extrato de transações**

- `GET /transacao/extrato`: Ao utilizar a rota de extrato, é retornado um objeto JSOn que informa a totalidade somada dos valores que sairam e que entraram na conta até o momento atual:

#### **Exemplo de requisição**

```javascript
// DELETE /transacao/extrato
// Sem conteúdo no corpo (body) da requisição
```

#### **Exemplos de resposta**

```javascript
// HTTP Status 200 / 201 / 204
{
	"entrada": 300000,
	"saida": 15800
}
```

para utilizar a API, utilize um serviço para requisições HTTP como Axios ou HTTPModule em Angular ou uma aplicação para requisições como [Postman](https://www.postman.com/), [Insomnia](https://insomnia.rest/) or [cURL](https://curl.se/).

## Desenvolvedores

| [<img src="https://avatars.githubusercontent.com/u/65367617" width=115><br><sub>Diego Oliveira</sub>](https://github.com/1983-diego) | [<img src="https://avatars.githubusercontent.com/u/60834135" width=115><br><sub>Rafael David</sub>](https://github.com/rdvid) |
| :----------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------: |

## Contact

If you have any questions or suggestions about this project, feel free to contact me through my GitHub profile: [@rdvid](https://github.com/rdvid).

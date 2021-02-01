# Problema

Precisamos criar uma mecanica para nos ajudar em procedimentos de combate a fraude, para isso foi criado uma base de dados com uma relação de CPFs cujo cadastro deverá ser negado caso um determinado usuário tente aplicar para uma das oportunidades disponíveis na plataforma.

Para atender essa demanda, iremos criar um serviço (uma API RESTful) que avalia se o CPF informado aparece na lista de negação.

# Requisitos

- CRUD para manipulação da lista de negação
    - Um modelo com um único campo
    - O número do documento precisa ser um número válido
- Carga de uma [lista](deny.txt) pré-definida de documentos com restrição
- Uma rota para avaliar um número de documento, retornando os valores abaixo:
    - ALLOW para documentos que não aparecem na lista
    - DENY para documentos que aparecem na lista, portanto com restrição
- Instruções para execução do projeto

# Premissas

A aplicação deve ser escrita usando Django e Django Rest Framework.

# Extras

- Rotas para o CRUD da lista de negação protegidas usando JWT
- Django Admin habilitado para manipulação da lista de negação
- Utilização de cache
- Testes
- Docker para criação da infraestrutura
- Checagem de código usando linter e/ou formatadores

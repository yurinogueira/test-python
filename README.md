# Executando
___
## Via Docker
* Caso prefira fazer a execução via docker.
* Receba a imagem utilizando o seguinte comando:
  ```shell
  docker pull yurinogueira/test-python-docker
  ```
* Execute a imagem docker utilizando o seguinte comando:
  ```shell
  docker run -p 8000:8000 -td test-python-docker
  ```
* Vá até a pasta do projeto usando o seguinte comando:
  ```shell
  cd test-python
  ```
* Então execute o servidor com o seguinte comando:
  ```shell
  python3 manage.py runserver 0.0.0.0:8000
  ```
 Veja o próximo passo em *Instruções*.
___
## Normal
* Necessário possuir Django e Django Rest Framework.
* Realizar a instalação do Django CPF com o seguinte comando:
  ```shell
  pip install django-cpf
  ```
* Realizar a instalação do Django Admin com o seguinte comando:
  ```shell
  pip install django-admin
  ```
* Realizar a instalação do Django Rest Framework JWT com o seguinter comando:
  ```shell
  pip install djangorestframework-jwt
  ```
* Clone o repositório onde preferir.
* Então execute o servidor com o seguinte comando:
  - Linux:
    ```shell
    python3 manage.py runserver
    ```
  - Windows:
    ```shell
    py manage.py runserver
    ```
___
# Instruções
* Para carregar a lista pré-definida de CPFs com restrição com o seguinte comadno:
  - Linux:
    ```shell
    python3 manage.py load_defaults
    ```
  - Windows:
    ```shell
    py manage.py load_defaults
    ```
  
* Para realizar os testes basta utilizar o seguinte comando:
  - Linux:
    ```shell
    python3 manage.py test
    ```
  - Windows:
    ```shell
    py manage.py test
    ```
* O acesso ao Django Admin estará localizado em localhost:8000/admin/
* Comandos para exemplo (Esses comandos podem ser acessados pelo navegador diretamente):
  * Para verificar se o CPF está no banco de dados (logo está bloqueado) e retorna DENY e caso não esteja ele não está bloqueado então retorna ALLOW
    ```shell
    curl http://localhost:8000/catalog/checkcpf/<cpf>/
    ```
  * Para receber o token JWT para ser utilizado no CRUD:
    ```shell
    curl -X POST -d "username=username&password=password" http://localhost:8000/login/
    ```
  * Para adicionar um novo CPF a lista de bloqueados:
    ```shell
     curl -H "Authorization: JWT <JWT>" -d "username=username&password=password" http://localhost:8000/catalog/addcpf/<cpf>/
    ```
  * Para deletar um CPF da lista de bloqueados:
    ```shell
     curl -H "Authorization: JWT <JWT>" -d "username=username&password=password" http://localhost:8000/catalog/deletecpf/<cpf>/
    ```
  * Para receber um Json {"cpf", ['cpf_1', 'cpf_2',...]} que é a lista de CPFs cadastrados no banco de dados:
    ```shell
     curl -H "Authorization: JWT <JWT>" -d "username=username&password=password" http://localhost:8000/catalog/getcpfs/
    ```
# Outros
 * O código foi formatado usando o Pylint.
 * Foi utilizado cache no método getcpfs e no checkcpf.

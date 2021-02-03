# Como executar
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
* Após isso carregar a lista pré-definida de CPFs com restrição com o seguinte comadno:
  - Linux:
    ```shell
    python3 manage.py load_defaults
    ```
  - Windows:
    ```shell
    py manage.py load_defaults
    ```

* Então executar o servidor com o seguinte comando:
  - Linux:
    ```shell
    python3 manage.py runserver
    ```
  - Windows:
    ```shell
    py manage.py runserver
    ```


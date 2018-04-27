# digital-nextel-test

## Requisitos:

* Stubby4j >= v.5.0.1
* Python >= 3.5

### Instalação

Crie um virtual environment, aqui vamos utilizar o `virtualenvwrapper`

```shell
$ mkvirtualenv -p python3 nextelinterview
```

Clone o projeto e acesse o brach 'dev'.

```shell
$ git clone git@github.com:vandersondev/digital-nextel-test.git
$ cd digital-nextel-test
$ git checkout dev
```

Instale as dependencias

```shell
$ pip install -r requirements.txt
```

### Execução

Levante o stubby4j

```shell
$ java -jar <jar do stubby4j> -d tech_assignment_mobile_stubs.yml
```

Dentro do diretório `/digital-nextel-test/app/` execute

```shell
$ FLASK_APP=app.py flask run
```

### Execução dos testes

Em `/digital-nextel-test/` execute o comando:

```shell
$ python -m pytest
```

### Como utilizar o Stubby4j:

Descompacte o arquivo mobile_assignment.zip (o arquivo se encontra na branch master desse repositório)

Baixe o jar do stubby4j e coloque-o na pasta `mobile_tech_assignment`.

Execute o stubby4j através do comando:

```shell
$ java -jar <jar do stubby4j> -d tech_assignment_mobile_stubs.yml
```
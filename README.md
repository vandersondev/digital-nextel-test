# digital-nextel-test

## Requisitos

* Stubby4j >= v.5.0.1
* Python >= 3.5.0

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

Instale as dependências

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

## O projeto

Para o projeto escolhi utilizar o micro framework Flask.

Flask é um framework Python voltado para desenvolvimento de aplicações web. Sua filosofia de micro framework mantém seu núcleo simples, porém extensível, possibilita utilizar apenas as bibliotecas necessárias ao projeto.

Como a aplicação demandava apenas consultas em um web services, Flask se demonstrou a opção mais correta, apesar de ser um micro framework. A ferramenta disponibiliza Blueprint object, uma forma de modularizar e escalar a aplicação no futuro.

Para este projeto criei uma arquivo de `app.py` onde ficam as views da aplicação e separei as consultas em um arquivo `getdata.py`, assim o arquivo `app.py` só tem a responsabilidade de invocar funções que requisitam os dados e repassar os dados para o template. O tratamento dos dados é todo feito no arquivo `getdata.py`.

Para testar a aplicação utilizei pytest, pois é uma forma simples de testar aplicações Python.

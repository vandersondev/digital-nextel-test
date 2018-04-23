# digital-nextel-test

Olá :)

O objetivo desta etapa não é somente resolver o problema proposto. Mesmo que este problema não seja extenso, nós esperamos que você encaminhe um código que acredite ser de qualidade, possível de ser rodado e evoluído. Use esse problema para nos mostrar as práticas que você utiliza no dia-a-dia para escrever um bom código.
 
Para a sua solução você poderá usar: Python, Swift, Java, Kotlin ou React Native.

 Alguns pontos que avaliamos:
- design da solução

- legibilidade

- facilidade de evolução e manutenção da aplicação

- testes automatizados / uso de boas práticas de agilidade

- operacionalidade

- arquitetura da aplicação

- experiência de usuário

- apresentação e arquitetura de informações

 
Você poderá utilizar quaisquer bibliotecas que você acredite que vão te auxiliar a desenvolver a solução, bem como bibliotecas de testes unitários ou ferramentas de build disponíveis para a linguagem que você escolher, mas pedimos que você elabore os motivos pelos quais as escolheu.

 
A segurança do sistema é muito importante para nós e certas extensões de arquivos serão bloqueadas por razão de segurança. Assegure-se de que não há nenhum arquivo executável (como .exe, .lib, .jar, .class) na sua submissão. Nosso sistema bloqueará tais arquivos por motivos de segurança e queremos evitar qualquer atraso no seu processo. 

Encaminhe uma breve descrição do design e suposições junto com o seu código, detalhes de implementação e arquitetura, bem como as instruções detalhadas de como rodar sua aplicação.

Queremos que nosso processo de seleção seja justo e as pessoas tenham as mesmas chances. Para isto, solicitamos que você não compartilhe ou publique nenhum destes problemas ou a sua solução.

Como regra geral, lhe concedemos três (03) dias, partindo do dia em que você recebe o exercício, para criar esta solução. Caso você necessite de mais tempo, não hesite em nos solicitar. Se você tiver qualquer dúvida sobre o seu processo de seleção, por favor, entre em contato comigo.

 
A Nextel deseja lhe oferecer a oportunidade de ter uma carreira desafiadora em nossos times dinâmicos. Nós lhe desejamos um bom trabalho e aguardamos ansiosamente a sua resposta!


# The Vacation Planner

Você recebeu quinze dias de férias para tirar a qualquer momento do próximo ano e está planejando visitar o Rio de Janeiro.

Para isso, você gostaria de encontrar a quinzena com a melhor temperatura possível. Encontrar esse padrão parece ser muito difícil a olho nu, então você resolve criar uma aplicação que consuma dados climáticos e sugira as melhores épocas do ano.
 
* Para encontrar a lista de cidades disponíveis, você utiliza (GET) localhost:8882/cities/

* Para descobrir os climas diários para um determinado ID em um determinado ano, você utiliza (GET) localhost:8882/cities/<id>/year/<ano>

* Para encontrar a lista de condições climáticas existentes, você utiliza (GET) localhost:8882/weather/

 
Sua aplicação deve ser capaz de receber informações como dias de férias, cidade-destino e intervalo de temperaturas aceitáveis para exibir todos os intervalos maiores ou iguais ao número de dias de férias inseridos que satisfaçam as características especificadas.




Exemplos de entrada:

1.

- O usuário seleciona que tem quinze dias de férias.

– O usuário seleciona a cidade como Porto Alegre

– O usuário seleciona os climas desejados como Clear, Partly Cloudy, Cold

 
- A saída mostra que, para Porto Alegre, existem pelo menos 3 combinações para o ano:

- De 20 de Junho a 10 de Julho

- De 09 de Maio a 26 de Maio

- De 02 de Abril a 16 de Abril

 
2.

- O usuário seleciona que tem quinze dias de férias.

– O usuário seleciona a cidade como Rio de Janeiro

– O usuário seleciona os climas desejados como Clear, Hot, Partly Cloudy, Fair

 
- A saída mostra que, para o Rio de Janeiro, existe pelo menos uma combinação para o ano:

- De 10 a 30 de Novembro




Utilize sua criatividade na hora de criar estas telas, se preocupando com a interação do usuário com sua aplicação.

Você pode utilizar as bibliotecas de sua preferência, desde que estabeleça uma estratégia de gerenciamento de dependências, com instruções para a configuração e execução da aplicação com estas bibliotecas.




Requisitos:

Stubby4j >= v.5.0.1

 
Como utilizar o Stubby4j:

Descompacte o arquivo mobile_assignment.zip

Baixe o jar do stubby4j e coloque-o na pasta mobile_tech_assignment.

Execute o stubby4j através do comando: 

java -jar <jar do stubby4j> -d tech_assignment_mobile_stubs.yml


Até breve!

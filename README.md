# Projeto de TCC: Relação entre Investimento e Desempenho Acadêmico no Sertão dos Crateús

Este repositório contém o projeto desenvolvido para o Trabalho de Conclusão de Curso (TCC) com o tema: **Relação entre Investimento e Desempenho Acadêmico no Sertão dos Crateús**.

## Estrutura do Repositório
O repositório está organizado nas seguintes pastas:

- **dados_escolares:**
  - Contém os dados escolares utilizados no projeto, como notas de matemática, português e médias de desempenho por município.

- **dados_financeiros:**
  - Contém os dados financeiros relacionados aos investimentos em educação nos municípios analisados.

- **ontologia:**
  - Contém a definição da ontologia RDF utilizada para modelar e representar as relações entre os dados financeiros e escolares.

- **entuba_dados_escolares:**
  - Contém o código responsável por realizar a importação e o carregamento dos dados escolares para o banco de dados PostgreSQL.

## Objetivo do Projeto
Este projeto tem como objetivo explorar e analisar a correlação entre os investimentos em educação e o desempenho acadêmico em municípios do Sertão dos Crateús, utilizando uma abordagem de modelagem semântica com RDF e bancos de dados relacionais.

## Tecnologias Utilizadas
- **Python**: Manipulação e importação de dados.
- **PostgreSQL**: Armazenamento e gerenciamento de dados.
- **RDF (Resource Description Framework)**: Modelagem e representação semântica dos dados.
- **psycopg2**: Conector Python para PostgreSQL.
- **rdflib**: Biblioteca para trabalhar com grafos RDF em Python.

## Como Executar
1. Certifique-se de ter o banco de dados PostgreSQL configurado com as tabelas necessárias.
2. Execute os scripts da pasta `entuba_dados_escolares` para importar os dados.
3. Utilize a ontologia presente na pasta `ontologia` para explorar as relações entre os dados financeiros e escolares.



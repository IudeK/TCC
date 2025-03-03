
# Projeto: Grafo RDF - Relação entre Investimento e Desempenho Acadêmico no Sertão dos Crateús

Este projeto cria e manipula um grafo RDF para modelar a relação entre investimentos financeiros e o desempenho acadêmico em municípios do Sertão dos Crateús, utilizando dados armazenados em um banco de dados PostgreSQL.

## Tecnologias Utilizadas
- Python 3
- Biblioteca `psycopg2` para conexão com PostgreSQL
- Biblioteca `rdflib` para manipulação de grafos RDF
- Banco de Dados: PostgreSQL

## Estrutura do Projeto

### Conexão com o Banco de Dados
O arquivo conecta-se a um banco de dados PostgreSQL utilizando o seguinte dicionário de configuração:

```python
db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432'
}
```

### Definição do Grafo RDF
O grafo RDF é criado utilizando a biblioteca `rdflib` e define as seguintes classes e propriedades:

- **Classes:** `DadoFinanceiro`, `DadoEscolar`, `Municipio`, `Ano`, `Anos`, `NotaMatematica`, `NotaPortugues`, `Media`, `Valor`, `Estado`
- **Propriedades:** `temMunicipio`, `temAno`, `temValor`, `temNotaMatematica`, `temNotaPortugues`, `temMedia`, `temAnos`, `temEstado`, `relacionadoCom`

### Extração e Inserção de Dados
Os dados são extraídos de duas tabelas PostgreSQL:

- `dados_financeiros`
- `dados_escolares`

E são adicionados ao grafo RDF através das funções `add_dados_financeiros()` e `add_dados_escolares()`.

### Exportação
Ao final da execução, o grafo RDF é salvo no formato Turtle (`grafo.ttl`).

## Como Executar o Projeto
1. Instale as bibliotecas necessárias:

    ```bash
    pip install psycopg2 rdflib
    ```

2. Configure o banco de dados PostgreSQL e ajuste as credenciais em `db_config`.

3. Execute o script:

    ```bash
    python3 nome_do_arquivo.py
    ```

4. O arquivo `dados.ttl` será gerado no diretório raiz.

# Ontologia: Relação entre Investimento e Desempenho Acadêmico no Sertão dos Crateús

Este documento descreve a ontologia para modelar a relação entre investimentos financeiros e o desempenho acadêmico em municípios do Sertão dos Crateús.

## Prefixos

```turtle
@prefix ex: <http://grafo_relacao_investimento_x_desempenho_academico_no_sertao_dos_crateus/> .
```

## Classes

```turtle
ex:DadoFinanceiro a rdfs:Class .
ex:DadoEscolar a rdfs:Class .
ex:Municipio a rdfs:Class .
ex:Ano a rdfs:Class .
ex:NotaMatematica a rdfs:Class .
ex:NotaPortugues a rdfs:Class .
ex:Media a rdfs:Class .
ex:Valor a rdfs:Class .
ex:Estado a rdfs:Class .
```

## Propriedades

```turtle
ex:temMunicipio a rdf:Property ;
  rdfs:domain ex:DadoEscolar ;
  rdfs:range ex:Municipio .

ex:temAno a rdf:Property ;
  rdfs:domain ex:DadoEscolar, ex:DadoFinanceiro ;
  rdfs:range ex:Ano .

ex:temValor a rdf:Property ;
  rdfs:domain ex:DadoFinanceiro ;
  rdfs:range ex:Valor .

ex:temNotaMatematica a rdf:Property ;
  rdfs:domain ex:DadoEscolar ;
  rdfs:range ex:NotaMatematica .

ex:temNotaPortugues a rdf:Property ;
  rdfs:domain ex:DadoEscolar ;
  rdfs:range ex:NotaPortugues .

ex:temMedia a rdf:Property ;
  rdfs:domain ex:DadoEscolar ;
  rdfs:range ex:Media .

ex:temAnos a rdf:Property ;
  rdfs:domain ex:DadoEscolar, ex:DadoFinanceiro ;
  rdfs:range ex:Anos .

ex:temEstado a rdf:Property ;
  rdfs:domain ex:DadoEscolar ;
  rdfs:range ex:Estado .

ex:relacionadoCom a rdf:Property ;
  rdfs:domain ex:DadoEscolar ;
  rdfs:range ex:DadoFinanceiro .
```

## Descrição

- **Classes**: As classes representam as entidades principais do modelo, como dados financeiros e escolares, municípios, anos, e outros elementos como notas e médias.
- **Propriedades**: As propriedades representam as relações entre as classes, como `temMunicipio`, `temAno`, `temValor`, etc.


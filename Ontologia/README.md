
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
Ao final da execução, o grafo RDF é salvo no formato Turtle (`dados.ttl`).

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

## Estrutura das Tabelas no Banco de Dados

### `dados_financeiros`
- `id` (int)
- `municipio` (text)
- `anos` (text)
- `ano` (int)
- `valor` (decimal)

### `dados_escolares`
- `id` (int)
- `municipio` (text)
- `anos` (text)
- `nota_matematica` (decimal)
- `nota_portugues` (decimal)
- `media` (decimal)
- `ano` (int)
- `estado` (text)

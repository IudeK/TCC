# Importação de Planilhas do INEP

Este script Python realiza a importação de dados de planilhas do INEP para um banco de dados PostgreSQL. Ele processa planilhas contendo informações escolares e insere os dados na tabela `dados_escolares`.

## Pré-requisitos

- Python 3.x
- Bibliotecas: `pandas`, `psycopg2`
- Banco de Dados PostgreSQL

## Configuração

1. Atualize as credenciais do banco de dados no dicionário `db_config` no código principal.

## Como Executar

1. Certifique-se de ter o arquivo `divulgacao_anos_iniciais_municipios_2021.xlsx` e `divulgacao_anos_finais_municipios_2019.xlsx` no mesmo diretório do script.
2. Execute o script usando:
   ```bash
   python importacao_planilhas.py
   ```

## Estrutura das Planilhas

- As planilhas devem ter cabeçalhos padronizados, com as notas a partir da quinta coluna.
- A filtragem é feita considerando apenas escolas do tipo `Municipal`.

## Contato

Para dúvidas ou melhorias, entre em contato com o desenvolvedor.

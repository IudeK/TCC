import pandas as pd
import psycopg2
import re

# Parâmetros de conexão
db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432'
}

municipios = [
    "Ararendá", "Catunda", "Crateús", "Hidrolândia", "Independência",
    "Ipaporanga", "Ipueiras", "Monsenhor Tabosa", "Nova Russas",
    "Novo Oriente", "Poranga", "Santa Quitéria", "Tamboril"
]


def load_and_process_excel(file_path, data_type):
    df = pd.read_excel(file_path)

    if data_type == 'iniciais':
        df = df.drop(df.columns[4:10], axis=1)
    elif data_type == 'finais':
        df = df.drop(df.columns[84:], axis=1)
        df = df.drop(df.columns[4:60], axis=1)

    df.columns = df.iloc[8]
    df = df.iloc[9:]
    df_filtrado = df[df.iloc[:, 3] == 'Municipal']
    df_filtrado.replace(['-', 'ND'], None, inplace=True)

    insert_table(df_filtrado, data_type)


def insert_table(table, data_type):
    try:
        conn = psycopg2.connect(**db_config)
        print("Conexão bem sucedida!")
        cursor = conn.cursor()

        for _, row in table.iterrows():
            estado, municipio = row[0], row[2]
            pos = 4
            while pos < len(row):
                ano = re.sub(r'\D', '', table.columns[pos])

                notas = [
                    process_value(row[pos]),
                    process_value(row[pos + 1]),
                    process_value(row[pos + 2])
                ]

                cursor.execute(
                    """
                    INSERT INTO dados_escolares (estado, municipio, anos, nota_matematica, nota_portugues, media, ano)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """,
                    (estado, municipio, data_type, *notas, ano)
                )
                pos += 3

        conn.commit()
        print("Dados inseridos com sucesso!")

    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()


def process_value(value):
    value = str(value).replace(',', '.').strip()
    return None if not re.search(r'[\d.]', value) else value


if __name__ == "__main__":
    load_and_process_excel('divulgacao_anos_iniciais_municipios_2021.xlsx', 'iniciais')
    load_and_process_excel('divulgacao_anos_finais_municipios_2019.xlsx', 'finais')
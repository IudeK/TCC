import psycopg2
from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD, RDFS

# Parâmetros de conexão
db_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432'
}

conn = psycopg2.connect(**db_config)
cur = conn.cursor()

EX = Namespace("http://grafo_relacao_investimento_x_desempenho_academico_no_sertao_dos_crateus/")  # Definição da namespace
g = Graph()

def main():
    # Define classes
    g.add((EX.DadoFinanceiro, RDF.type, RDFS.Class))
    g.add((EX.DadoEscolar, RDF.type, RDFS.Class))

    # Definir as "subclasses" como entidades específicas
    g.add((EX.Municipio, RDF.type, RDFS.Class))
    g.add((EX.Ano, RDF.type, RDFS.Class))
    g.add((EX.Anos, RDF.type, RDFS.Class))
    g.add((EX.NotaMatematica, RDF.type, RDFS.Class))
    g.add((EX.NotaPortugues, RDF.type, RDFS.Class))
    g.add((EX.Media, RDF.type, RDFS.Class))
    g.add((EX.Valor, RDF.type, RDFS.Class))
    g.add((EX.Estado, RDF.type, RDFS.Class))

    # Associar propriedades com domínio e intervalo
    g.add((EX.temMunicipio, RDF.type, RDF.Property))
    g.add((EX.temMunicipio, RDFS.domain, EX.DadoEscolar))
    g.add((EX.temMunicipio, RDFS.range, EX.Municipio))

    g.add((EX.temAno, RDF.type, RDF.Property))
    g.add((EX.temAno, RDFS.domain, EX.DadoEscolar))
    g.add((EX.temAno, RDFS.range, EX.Ano))

    g.add((EX.temValor, RDF.type, RDF.Property))
    g.add((EX.temValor, RDFS.domain, EX.DadoFinanceiro))
    g.add((EX.temValor, RDFS.range, EX.Valor))

    g.add((EX.temNotaMatematica, RDF.type, RDF.Property))
    g.add((EX.temNotaMatematica, RDFS.domain, EX.DadoEscolar))
    g.add((EX.temNotaMatematica, RDFS.range, EX.NotaMatematica))

    g.add((EX.temNotaPortugues, RDF.type, RDF.Property))
    g.add((EX.temNotaPortugues, RDFS.domain, EX.DadoEscolar))
    g.add((EX.temNotaPortugues, RDFS.range, EX.NotaPortugues))

    g.add((EX.temMedia, RDF.type, RDF.Property))
    g.add((EX.temMedia, RDFS.domain, EX.DadoEscolar))
    g.add((EX.temMedia, RDFS.range, EX.Media))

    g.add((EX.temAnos, RDF.type, RDF.Property))
    g.add((EX.temAnos, RDFS.domain, EX.DadoEscolar))
    g.add((EX.temAnos, RDFS.range, EX.Anos))

    g.add((EX.temAnos, RDF.type, RDF.Property))
    g.add((EX.temAnos, RDFS.domain, EX.DadoFinanceiro))
    g.add((EX.temAnos, RDFS.range, EX.Anos))

    g.add((EX.temEstado, RDF.type, RDF.Property))
    g.add((EX.temEstado, RDFS.domain, EX.DadoEscolar))
    g.add((EX.temEstado, RDFS.range, EX.Estado))

    # Relacionamento entre DadoEscolar e DadoFinanceiro
    g.add((EX.relacionadoCom, RDF.type, RDF.Property))
    g.add((EX.relacionadoCom, RDFS.domain, EX.DadoEscolar))
    g.add((EX.relacionadoCom, RDFS.range, EX.DadoFinanceiro))

    # Adicionar dados
    add_dados_financeiros()
    add_dados_escolares()

    cur.close()
    conn.close()

    # Salvar grafo RDF em formato Turtle
    g.serialize(destination='dados.ttl', format='turtle')
    print("Dados RDF salvos em 'dados.ttl'")

def add_dados_financeiros():
    cur.execute("SELECT id, municipio, anos, ano, valor FROM dados_financeiros")
    rows = cur.fetchall()
    for row in rows:
        id, municipio, anos, ano, valor = row
        uri = URIRef(f"http://grafo_relacao_investimento_x_desempenho_academico_no_sertao_dos_crateus/DadoFinanceiro/{id}")
        g.add((uri, RDF.type, EX.DadoFinanceiro))
        g.add((uri, EX.temMunicipio, Literal(municipio, datatype=XSD.string)))
        g.add((uri, EX.temAno, Literal(ano, datatype=XSD.gYear)))
        g.add((uri, EX.temValor, Literal(valor, datatype=XSD.decimal)))
        g.add((uri, EX.temAnos, Literal(anos, datatype=XSD.string)))  # Adiciona o valor de temAnos nos dados financeiros

def add_dados_escolares():
    cur.execute("SELECT id, municipio, anos, nota_matematica, nota_portugues, media, ano, estado FROM dados_escolares")
    rows = cur.fetchall()
    for row in rows:
        id, municipio, anos, nota_matematica, nota_portugues, media, ano, estado = row
        uri = URIRef(f"http://grafo_relacao_investimento_x_desempenho_academico_no_sertao_dos_crateus/DadoEscolar/{id}")
        g.add((uri, RDF.type, EX.DadoEscolar))
        g.add((uri, EX.temMunicipio, Literal(municipio, datatype=XSD.string)))
        g.add((uri, EX.temAno, Literal(ano, datatype=XSD.gYear)))
        g.add((uri, EX.temNotaMatematica, Literal(nota_matematica, datatype=XSD.decimal)))
        g.add((uri, EX.temNotaPortugues, Literal(nota_portugues, datatype=XSD.decimal)))
        g.add((uri, EX.temMedia, Literal(media, datatype=XSD.decimal)))
        g.add((uri, EX.temAnos, Literal(anos, datatype=XSD.string)))
        g.add((uri, EX.temEstado, Literal(estado, datatype=XSD.string)))  # Adiciona o valor de temEstado nos dados escolares

if __name__ == "__main__":
    main()

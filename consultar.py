"""Roda uma consulta SQL contra os CSVs fictícios de dados/ e imprime o resultado.

Cada CSV vira uma tabela com o nome do arquivo (clientes, produtos, pedidos).

    .venv/bin/python consultar.py --sql "SELECT * FROM clientes LIMIT 5"
    .venv/bin/python consultar.py --arquivo respostas/02-pedidos-mais-caros-de-marco.sql
"""
import argparse
import pathlib

import duckdb

RAIZ = pathlib.Path(__file__).resolve().parent


def conectar(pasta_dados=None):
    pasta = pathlib.Path(pasta_dados) if pasta_dados else RAIZ / "dados"
    con = duckdb.connect()
    for csv in sorted(pasta.glob("*.csv")):
        con.execute("CREATE VIEW %s AS SELECT * FROM read_csv_auto('%s', header=true)" % (csv.stem, csv.as_posix()))
    return con


def consultar(sql, pasta_dados=None):
    return conectar(pasta_dados).execute(sql).fetchdf()


def main():
    parser = argparse.ArgumentParser(description="Consulta SQL nos dados fictícios do curso.")
    grupo = parser.add_mutually_exclusive_group(required=True)
    grupo.add_argument("--sql", help="texto da consulta")
    grupo.add_argument("--arquivo", help="arquivo .sql com a consulta")
    args = parser.parse_args()
    sql = args.sql if args.sql else pathlib.Path(args.arquivo).read_text(encoding="utf-8")
    df = consultar(sql)
    print(df.to_string(index=False))
    print("(%d linhas)" % len(df))


if __name__ == "__main__":
    main()

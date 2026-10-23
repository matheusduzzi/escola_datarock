"""Testes do curso primeiros-passos-dados.

Cada teste roda a sua resposta (pasta respostas/) contra dados/ e confere o RESULTADO (linhas, colunas, valores,
ordem), nunca o texto do código. A referência é recalculada aqui só com a stdlib, lendo os CSVs.
Os números dos critérios de aceite dos exercícios são as constantes deste arquivo.

Salve as respostas em respostas/, com os nomes pedidos nos enunciados, e rode:
    .venv/bin/pytest -q tests
Para usar outra pasta: ALVO=outra-pasta .venv/bin/pytest -q tests
"""
import csv
import hashlib
import importlib.util
import os
import pathlib
import subprocess
import sys
from collections import Counter, defaultdict

import pandas as pd
import pytest

RAIZ = pathlib.Path(__file__).resolve().parents[1]
DADOS = RAIZ / "dados"
ALVO = RAIZ / os.environ.get("ALVO", "respostas")

sys.path.insert(0, str(RAIZ))
from consultar import consultar  # noqa: E402

# Números dos critérios de aceite (copiados para exercicios/NN-*.md).
EX01_LINHAS = 8
EX02_LINHAS = 10
EX02_TOPO = (808, 3538.15)
EX03_LINHAS = 5
EX03_TOPO = "Esporte"
EX04_LINHAS = 11
EX04_TOPO = ("Campinas", 627)
EX05_LINHAS = 17
EX06_IMPUTADOS = 11
EX07_LINHAS = 6


def ler(nome):
    with open(DADOS / nome, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


CLIENTES = ler("clientes.csv")
PRODUTOS = ler("produtos.csv")
PEDIDOS = ler("pedidos.csv")
PRODUTO = {p["id_produto"]: p for p in PRODUTOS}
CLIENTE = {c["id_cliente"]: c for c in CLIENTES}


def _exige(arquivo):
    if not (ALVO / arquivo).exists():
        pytest.skip("crie respostas/%s para rodar este teste" % arquivo)


def sql(arquivo):
    _exige(arquivo)
    return consultar((ALVO / arquivo).read_text(encoding="utf-8"))


def modulo(arquivo):
    _exige(arquivo)
    spec = importlib.util.spec_from_file_location(arquivo.replace("-", "_")[:-3], str(ALVO / arquivo))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------- dados ----------

def _hashes(pasta):
    return {p.name: hashlib.sha1(p.read_bytes()).hexdigest() for p in sorted(pasta.glob("*.csv"))}


def test_dados_reprodutiveis_e_pequenos(tmp_path):
    subprocess.run([sys.executable, str(DADOS / "gerar.py"), "--saida", str(tmp_path)],
                   check=True, capture_output=True)
    assert _hashes(tmp_path) == _hashes(DADOS)
    assert sum(p.stat().st_size for p in DADOS.glob("*.csv")) <= 1024 * 1024


def test_bordas_plantadas():
    assert sum(1 for p in PEDIDOS if p["valor"] == "") == EX06_IMPUTADOS
    bauru = {c["id_cliente"] for c in CLIENTES if c["cidade"] == "Bauru"}
    assert bauru and not any(p["id_cliente"] in bauru for p in PEDIDOS)


# ---------- SQL ----------

def test_ex01():
    df = sql("01-produtos-de-esporte.sql")
    assert list(df.columns) == ["id_produto", "nome", "preco"]
    esperado = sorted((p for p in PRODUTOS if p["categoria"] == "Esporte"),
                      key=lambda p: (-float(p["preco"]), p["nome"]))
    assert len(df) == EX01_LINHAS == len(esperado)
    assert [int(x) for x in df["id_produto"]] == [int(p["id_produto"]) for p in esperado]
    # borda escondida: dois produtos com o mesmo preço, desempate por nome
    precos = list(df["preco"])
    assert len(set(precos)) < len(precos)


def test_ex02():
    df = sql("02-pedidos-mais-caros-de-marco.sql")
    assert list(df.columns) == ["id_pedido", "data_pedido", "valor"]
    candidatos = [p for p in PEDIDOS if p["status"] == "entregue" and p["valor"] != ""
                  and p["data_pedido"].startswith("2026-03")]
    esperado = sorted(candidatos, key=lambda p: (-float(p["valor"]), int(p["id_pedido"])))[:10]
    assert len(df) == EX02_LINHAS
    assert [int(x) for x in df["id_pedido"]] == [int(p["id_pedido"]) for p in esperado]
    assert (int(df["id_pedido"][0]), float(df["valor"][0])) == EX02_TOPO
    # borda escondida: pedido caro em 28/02, em 01/04, cancelado caro em março e valor vazio
    datas = [str(d)[:7] for d in df["data_pedido"]]
    assert set(datas) == {"2026-03"}
    assert df["valor"].notna().all()


def test_ex03():
    df = sql("03-faturamento-por-categoria.sql")
    assert list(df.columns) == ["categoria", "pedidos", "faturamento"]
    pedidos, fat = Counter(), defaultdict(float)
    for p in PEDIDOS:
        if p["status"] != "entregue":
            continue
        cat = PRODUTO[p["id_produto"]]["categoria"]
        pedidos[cat] += 1
        if p["valor"] != "":
            fat[cat] += float(p["valor"])
    assert len(df) == EX03_LINHAS
    assert df["categoria"][0] == EX03_TOPO
    for _, linha in df.iterrows():
        # borda escondida: pedido sem valor conta em pedidos e não soma no faturamento
        assert linha["pedidos"] == pedidos[linha["categoria"]]
        assert linha["faturamento"] == pytest.approx(fat[linha["categoria"]], abs=0.01)
    assert list(df["faturamento"]) == sorted(df["faturamento"], reverse=True)


def test_ex04():
    df = sql("04-pedidos-por-cidade.sql")
    assert list(df.columns) == ["cidade", "total_pedidos"]
    contagem = Counter(CLIENTE[p["id_cliente"]]["cidade"] for p in PEDIDOS)
    esperado = sorted(contagem.items(), key=lambda kv: (-kv[1], kv[0]))
    assert len(df) == EX04_LINHAS
    assert [(c, int(n)) for c, n in zip(df["cidade"], df["total_pedidos"])] == esperado
    assert (df["cidade"][0], int(df["total_pedidos"][0])) == EX04_TOPO
    # borda escondida: Bauru só tem clientes sem pedido e não aparece
    assert "Bauru" not in set(df["cidade"])


def test_ex05():
    df = sql("05-clientes-sem-pedido.sql")
    assert list(df.columns) == ["id_cliente", "nome", "cidade"]
    com_pedido = {p["id_cliente"] for p in PEDIDOS}
    esperado = sorted(int(c["id_cliente"]) for c in CLIENTES if c["id_cliente"] not in com_pedido)
    assert len(df) == EX05_LINHAS
    assert [int(x) for x in df["id_cliente"]] == esperado
    # borda escondida: os clientes de Bauru estão na lista
    assert (df["cidade"] == "Bauru").sum() == sum(1 for c in CLIENTES if c["cidade"] == "Bauru")


# ---------- pandas ----------

def _pedidos_tratados_referencia():
    df = pd.read_csv(DADOS / "pedidos.csv")
    preco = {int(k): float(v["preco"]) for k, v in PRODUTO.items()}
    falta = df["valor"].isna()
    df.loc[falta, "valor"] = [round(q * preco[i], 2) for q, i in
                              zip(df.loc[falta, "quantidade"], df.loc[falta, "id_produto"])]
    return df


def test_ex06():
    tratar = modulo("06-tratar-nulos.py").tratar_nulos
    pedidos = pd.read_csv(DADOS / "pedidos.csv")
    produtos = pd.read_csv(DADOS / "produtos.csv")
    df = tratar(pedidos.copy(), produtos.copy())
    assert len(df) == len(PEDIDOS)
    assert "valor_imputado" in df.columns
    assert df["valor"].notna().all()
    assert int(df["valor_imputado"].sum()) == EX06_IMPUTADOS
    ref = _pedidos_tratados_referencia().set_index("id_pedido")["valor"]
    got = df.set_index("id_pedido")["valor"]
    # borda escondida: valor registrado não muda; o que faltava vira quantidade x preço
    assert got.sort_index().round(2).tolist() == ref.sort_index().round(2).tolist()


def test_ex07():
    mensal = modulo("07-faturamento-mensal.py").faturamento_mensal
    df = mensal(_pedidos_tratados_referencia())
    assert list(df.columns) == ["mes", "pedidos", "faturamento"]
    ref = _pedidos_tratados_referencia()
    ref = ref[ref["status"] == "entregue"]
    pedidos, fat = Counter(), defaultdict(float)
    for d, v in zip(ref["data_pedido"], ref["valor"]):
        pedidos[d[:7]] += 1
        fat[d[:7]] += float(v)
    assert len(df) == EX07_LINHAS
    assert list(df["mes"]) == sorted(pedidos)
    for _, linha in df.iterrows():
        assert int(linha["pedidos"]) == pedidos[linha["mes"]]
        assert linha["faturamento"] == pytest.approx(fat[linha["mes"]], abs=0.01)
    # borda escondida: cancelados fora e pedidos de 28/02 e 01/04 no mês certo
    assert int(df["pedidos"].sum()) == len(ref)

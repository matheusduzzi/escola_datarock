# Primeiros passos em dados: SQL e Python

Kit do curso da Escola Datarock. Aqui estão os dados da Loja Exemplo, os enunciados dos exercícios e
os testes que corrigem a sua resposta. As aulas ficam na plataforma do curso.

Tudo em `dados/` é fictício. A Loja Exemplo não existe.

## Preparar a máquina (uma vez)

Você precisa do Python 3.12 ou mais novo.

```bash
git clone https://github.com/matheusduzzi/escola_datarock.git
cd escola_datarock
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

No Windows, troque `.venv/bin/` por `.venv\Scripts\`.

## Rodar uma consulta

```bash
.venv/bin/python consultar.py --sql "SELECT * FROM clientes LIMIT 5"
```

Cada arquivo de `dados/` vira uma tabela: `clientes`, `produtos` e `pedidos`.

## Fazer um exercício

1. Leia o enunciado no fim da página da aula (ele também está em `exercicios/`).
2. Salve a sua resposta em `respostas/`, com o nome de arquivo que o enunciado pede.
3. Rode o teste do exercício:

```bash
.venv/bin/pytest -q tests/test_exercicios.py::test_ex01
```

Passou, está certo. Falhou, a mensagem diz o que não bateu. Exercício sem arquivo em `respostas/`
aparece como pulado. Para rodar todos de uma vez: `.venv/bin/pytest -q tests`.

## Pastas

| Pasta | O que é |
|---|---|
| `dados/` | os CSVs da Loja Exemplo e o gerador (`gerar.py`, seed 42) |
| `exercicios/` | os enunciados dos 8 exercícios |
| `respostas/` | onde você salva as suas respostas |
| `consultas/` | as consultas do projeto final (aula 8) |
| `tests/` | os testes que corrigem a sua resposta |

Travou num exercício? Peça uma dica à Tutoria do curso.

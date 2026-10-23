# Exercício 6: preencher o valor que faltou

Objetivo avaliado: O5.

Dados: `dados/pedidos.csv` e `dados/produtos.csv` (fictícios, gerados por `dados/gerar.py`, seed 42).

Entregue: um arquivo `06-tratar-nulos.py` com a função `tratar_nulos(pedidos, produtos)`. Ela
recebe os dois DataFrames (tabelas do pandas) e devolve os pedidos com:
- a mesma quantidade de linhas;
- `valor` preenchido como `quantidade * preco` do produto (2 casas) só onde estava vazio;
- uma coluna nova `valor_imputado`, verdadeira nas linhas que você preencheu.

Critério de aceite: o teste `test_ex06` passa. Ele confere que nenhuma linha some, que não
sobra valor vazio, que 11 linhas foram preenchidas (`EX06_IMPUTADOS`) e que todo valor que já
existia ficou igual.

Dica 1 (pista): o preço não está na tabela de pedidos. Como você trouxe a categoria no SQL do
exercício 3? O pandas tem o mesmo movimento.

Dica 2 (caminho): `merge` com produtos pelo `id_produto`, marque onde `valor` é nulo, preencha
só essas linhas e tire a coluna de preço antes de devolver.

---

Correção: rode o teste abaixo contra a sua resposta. A resolução comentada fica com a Tutoria, peça uma dica quando travar.
Teste: `tests/test_exercicios.py::test_ex06` (confere linhas, colunas e valores; borda escondida: valor registrado não pode mudar).

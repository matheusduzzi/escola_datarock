# Exercício 1: produtos de Esporte do mais caro ao mais barato

Objetivo avaliado: O1.

Dados: `dados/produtos.csv` (fictícios, gerados por `dados/gerar.py`, seed 42).

Entregue: um arquivo `01-produtos-de-esporte.sql` com uma consulta que devolve `id_produto`,
`nome` e `preco` dos produtos da categoria Esporte, do mais caro ao mais barato. Quando dois
produtos têm o mesmo preço, o de nome em ordem alfabética vem primeiro.

Critério de aceite: o teste `test_ex01` passa. Ele confere as 3 colunas nessa ordem, 8 linhas
(constante `EX01_LINHAS`) e a ordem exata dos produtos, inclusive no empate.

Dica 1 (pista): qual coluna diz a categoria do produto? E o que acontece com a ordem quando dois
preços são iguais e você não diz nada?

Dica 2 (caminho): filtre a categoria no WHERE, ordene pelo preço do maior para o menor e coloque
um segundo critério de ordenação para o empate.

---

Correção: rode o teste abaixo contra a sua resposta. A resolução comentada fica com a Tutoria, peça uma dica quando travar.
Teste: `tests/test_exercicios.py::test_ex01` (confere linhas, colunas e ordem; inclui o empate de preço escondido).

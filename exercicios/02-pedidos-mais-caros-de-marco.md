# Exercício 2: os 10 pedidos entregues mais caros de março

Objetivo avaliado: O1.

Dados: `dados/pedidos.csv` (fictícios, gerados por `dados/gerar.py`, seed 42).

Entregue: um arquivo `02-pedidos-mais-caros-de-marco.sql` que devolve `id_pedido`,
`data_pedido` e `valor` dos 10 pedidos com status `entregue` mais caros de março de 2026. Valor
maior primeiro; no empate de valor, o menor `id_pedido` primeiro. Pedido sem valor registrado
não entra.

Critério de aceite: o teste `test_ex02` passa. Ele confere 10 linhas (`EX02_LINHAS`), a ordem
dos ids e o topo: pedido 808, valor 3538.15 (`EX02_TOPO`). Nenhuma data fora de março.

Dica 1 (pista): onde termina março? O dia 31 entra? E o dia 1 de abril?

Dica 2 (caminho): três condições no WHERE (status, início do mês, fim do mês), mais uma para
tirar o valor vazio. Depois ORDER BY com desempate e LIMIT.

---

Correção: rode o teste abaixo contra a sua resposta. A resolução comentada fica com a Tutoria, peça uma dica quando travar.
Teste: `tests/test_exercicios.py::test_ex02` (confere linhas, ordem e valores; bordas escondidas: pedidos caros em 28/02 e 01/04, um cancelado caro em março e um valor vazio em março).

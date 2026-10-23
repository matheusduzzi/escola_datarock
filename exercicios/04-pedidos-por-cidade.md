# Exercício 4: pedidos por cidade

Objetivo avaliado: O3.

Dados: `dados/pedidos.csv` e `dados/clientes.csv` (fictícios, gerados por `dados/gerar.py`, seed 42).

Entregue: um arquivo `04-pedidos-por-cidade.sql` que devolve `cidade` e `total_pedidos`
(todos os pedidos, de qualquer status), do maior total para o menor. No empate, cidade em ordem
alfabética.

Critério de aceite: o teste `test_ex04` passa. Ele confere 11 linhas (`EX04_LINHAS`), Campinas
no topo com 627 pedidos (`EX04_TOPO`) e a lista inteira recalculada a partir dos CSVs.

Dica 1 (pista): qual coluna existe nas duas tabelas?

Dica 2 (caminho): JOIN por `id_cliente`, depois GROUP BY pela cidade e COUNT.

---

Correção: rode o teste abaixo contra a sua resposta. A resolução comentada fica com a Tutoria, peça uma dica quando travar.
Teste: `tests/test_exercicios.py::test_ex04` (confere linhas, ordem e valores; borda escondida: uma cidade só com clientes sem pedido não pode aparecer).

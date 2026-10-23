# Exercício 3: faturamento por categoria

Objetivo avaliado: O2.

Dados: `dados/pedidos.csv` e `dados/produtos.csv` (fictícios, gerados por `dados/gerar.py`, seed 42).

Entregue: um arquivo `03-faturamento-por-categoria.sql` que devolve, só para pedidos
`entregue`, as colunas `categoria`, `pedidos` (quantos pedidos entregues, inclusive os sem valor
registrado) e `faturamento` (soma dos valores registrados, com 2 casas). Maior faturamento
primeiro.

Critério de aceite: o teste `test_ex03` passa. Ele confere 5 linhas (`EX03_LINHAS`), Esporte no
topo (`EX03_TOPO`) e, para cada categoria, a contagem e a soma recalculadas a partir do CSV.

Dica 1 (pista): a categoria não está na tabela de pedidos. Onde ela está? E qual a diferença
entre `COUNT(*)` e `COUNT(valor)`?

Dica 2 (caminho): junte pedidos e produtos pelo `id_produto`, filtre os entregues, agrupe por
categoria, conte as linhas e some o valor.

O JOIN aparece de verdade na aula 4. Aqui ele é a ponte até a categoria; copie a linha e siga.

---

Correção: rode o teste abaixo contra a sua resposta. A resolução comentada fica com a Tutoria, peça uma dica quando travar.
Teste: `tests/test_exercicios.py::test_ex03` (confere linhas, colunas e valores; borda escondida: pedido sem valor conta em `pedidos` e não soma em `faturamento`).

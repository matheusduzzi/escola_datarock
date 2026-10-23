# Exercício 5: quem nunca comprou

Objetivo avaliado: O4.

Dados: `dados/clientes.csv` e `dados/pedidos.csv` (fictícios, gerados por `dados/gerar.py`, seed 42).

Entregue: um arquivo `05-clientes-sem-pedido.sql` que devolve `id_cliente`, `nome` e `cidade`
dos clientes que nunca fizeram pedido, em ordem de `id_cliente`. No fim do arquivo, um
comentário SQL (`-- ...`) de 2 a 3 frases explicando por que o LEFT JOIN da aula 5 devolve mais
linhas que o INNER JOIN na mesma base.

Critério de aceite: o teste `test_ex05` passa. Ele confere 17 linhas (`EX05_LINHAS`) e os ids
exatos. O comentário é lido pela tutoria, que confere se ele cita o cliente sem par.

Dica 1 (pista): se o JOIN normal some com quem não tem pedido, qual JOIN mantém essas pessoas?
O que aparece nas colunas de pedido para elas?

Dica 2 (caminho): LEFT JOIN de clientes para pedidos, depois fique só com as linhas em que a
coluna de pedido veio vazia.

---

Correção: rode o teste abaixo contra a sua resposta. A resolução comentada fica com a Tutoria, peça uma dica quando travar.
Teste: `tests/test_exercicios.py::test_ex05` (confere linhas e ids; borda escondida: os clientes de uma cidade inteira sem pedido estão na lista).

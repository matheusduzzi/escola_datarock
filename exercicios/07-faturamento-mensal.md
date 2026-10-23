# Exercício 7: faturamento por mês

Objetivo avaliado: O5.

Dados: `dados/pedidos.csv` já tratado pela regra do exercício 6 (o teste monta essa versão
sozinho e entrega para a sua função).

Entregue: um arquivo `07-faturamento-mensal.py` com a função `faturamento_mensal(pedidos)`. Ela
devolve um DataFrame com as colunas `mes` (texto `AAAA-MM`), `pedidos` (quantos entregues) e
`faturamento` (soma do valor, 2 casas), só com pedidos `entregue`, em ordem de mês.

Critério de aceite: o teste `test_ex07` passa. Ele confere 6 linhas (`EX07_LINHAS`), os meses
em ordem e, mês a mês, a contagem e a soma recalculadas a partir do CSV.

Dica 1 (pista): a data está como texto. Como você tira dela só o ano e o mês?

Dica 2 (caminho): filtre os entregues, crie a coluna `mes` com `pd.to_datetime` e
`dt.strftime`, agrupe por `mes` contando pedidos e somando valor.

---

Correção: rode o teste abaixo contra a sua resposta. A resolução comentada fica com a Tutoria, peça uma dica quando travar.
Teste: `tests/test_exercicios.py::test_ex07` (confere linhas, colunas e valores; bordas escondidas: cancelados fora e pedidos de 28/02 e 01/04 no mês certo).

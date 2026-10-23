# Exercício 8: projeto final, análise exploratória da Loja Exemplo

Objetivo avaliado: O6.

Dados: `dados/clientes.csv`, `dados/produtos.csv` e `dados/pedidos.csv` (fictícios, gerados por
`dados/gerar.py`, seed 42).

Entregue: um repositório (ou uma pasta) com um `README.md` que responde 3 perguntas de negócio
que você escolheu sobre a Loja Exemplo. Para cada pergunta: a consulta SQL ou o código pandas, o
número que saiu, uma frase de leitura e a checagem que você fez para confiar no número. Inclua
as consultas dos exercícios 1 a 7 numa pasta `consultas/`.

Exemplos de pergunta (pode usar outras): qual mês teve o maior ticket médio? Qual cidade compra
mais Eletro? Quanto do faturamento de março vem dos 10 maiores pedidos?

Critério de aceite: 3 de 4 critérios da rubrica abaixo no nível "Atende" ou acima.

Dica 1 (pista): qual pergunta a gerente da Loja Exemplo faria na segunda de manhã? Comece por ela.

Dica 2 (caminho): escreva a pergunta, rode a consulta, anote o número, confira por um segundo
caminho (contagem na mão, outra consulta, SQL contra pandas) e só então escreva a leitura.

## Rubrica de avaliação

Quatro critérios, quatro níveis. Cada nível descreve o que se vê na entrega.

| Critério | Não atende | Atende parcialmente | Atende | Supera |
|---|---|---|---|---|
| Pergunta de negócio | não há pergunta, só gráficos ou tabelas soltas | perguntas genéricas ("analisar as vendas") | 3 perguntas que a gerente da Loja Exemplo usaria para decidir algo | as perguntas se encadeiam: a resposta de uma leva à próxima |
| Consulta e número | consulta ausente ou que não roda contra `dados/` | roda, mas o número do README não bate com a saída | toda resposta tem consulta que roda e o número igual à saída | consultas organizadas em `consultas/` com nome que diz a pergunta |
| Verificação humana feita | aceita o número como veio | confere só que a consulta não deu erro | confere cada número por um segundo caminho (outra consulta, pandas, contagem na mão) | registra um erro que pegou na checagem e como corrigiu |
| Tratamento de borda | ignora nulos, cancelados e clientes sem pedido | trata uma das bordas sem dizer a regra | declara a regra para nulos, cancelados e clientes sem pedido em cada resposta que depende delas | mostra quanto o número muda com e sem a regra |

Aprovação: 3 de 4 critérios em "Atende" ou acima.

---

Avaliação: a rubrica acima (4 critérios, 4 níveis)
Teste: não se aplica (rubrica). A tutoria usa os níveis para dar dica, nunca para entregar a resposta.

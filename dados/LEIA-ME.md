# Dados do curso primeiros-passos-dados

**Tudo aqui é fictício.** A Loja Exemplo não existe. Os clientes se chamam "Cliente 0001",
"Cliente 0002" e assim por diante. As cidades são só rótulos de região. Nenhum dado vem de
cliente, de pessoa ou de empresa real.

## Como gerar

```bash
python3 dados/gerar.py
```

O gerador só usa a biblioteca padrão do Python. Os testes e as consultas usam as versões fixadas
em `../requirements.txt` (Python 3.12 ou mais novo; rodado só em 3.14.5). Seed fixa: **42**. Rodar duas vezes dá os mesmos arquivos,
byte a byte (o teste `test_dados_reprodutiveis_e_pequenos` confere por hash).

## Arquivos

| Arquivo | Linhas | Colunas |
|---|---|---|
| `clientes.csv` | 300 | id_cliente, nome, cidade, uf, data_cadastro |
| `produtos.csv` | 40 | id_produto, nome, categoria, preco |
| `pedidos.csv` | 3003 | id_pedido, id_cliente, id_produto, data_pedido, quantidade, valor, status |

Contagens da saída do `gerar.py` em 2026-10-19:
`clientes=300 produtos=40 pedidos=3003 clientes_sem_pedido=17 valor_nulo=11`.
Tamanho total: 136 KB (`du -ch dados/*.csv`).

Os pedidos vão de 2026-01-01 a 2026-06-30. `status` é `entregue` ou `cancelado`.

## Casos de borda plantados de propósito

| Borda | Onde | Exercício que depende |
|---|---|---|
| 17 clientes sem nenhum pedido, entre eles os 3 clientes de Bauru | `clientes.csv` | 4 (Bauru some no JOIN) e 5 |
| 11 pedidos com `valor` vazio (valor não registrado no caixa) | `pedidos.csv` | 2, 3, 6 |
| pedidos caros em 2026-02-28 e 2026-04-01 e um cancelado caro em março | `pedidos.csv` | 2 e 7 |
| dois produtos de Esporte com o mesmo preço | `produtos.csv` | 1 (desempate por nome) |
| valores iguais entre pedidos de março | `pedidos.csv` | 2 (desempate por id_pedido) |

Não edite os CSVs à mão. Se precisar de outro caso, mude o `gerar.py`, gere de novo e rode os
testes do curso.

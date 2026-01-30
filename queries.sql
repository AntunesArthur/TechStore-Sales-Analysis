-- #1
SELECT nome, email FROM
 Clientes WHERE cidade='São Paulo';

-- #2 
SELECT nome_produto, preco FROM
 Produtos WHERE preco > 800;

-- #3
SELECT nome, nome_produto FROM
((Vendas JOIN Clientes ON Vendas.id_cliente = Clientes.id_cliente) JOIN Produtos ON Vendas.id_produto = Produtos.id_produto)

-- #4
SELECT SUM(Vendas.quantidade * Produtos.preco) FROM
Vendas
INNER JOIN Produtos ON Produtos.id_produto = Vendas.id_produto

-- #5
SELECT Clientes.nome, SUM(Vendas.quantidade * Produtos.preco) AS ValorGasto FROM
Vendas
INNER JOIN Produtos ON Produtos.id_produto = Vendas.id_produto
INNER JOIN Clientes ON Clientes.id_cliente = Vendas.id_cliente
GROUP BY Clientes.nome
ORDER BY ValorGasto DESC;
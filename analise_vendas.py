import sqlite3

#O arquivo do banco de dados está dentro da pasta, por essa razão não foi necessário utilizar a biblioteca os
db_file = "loja.db"

#Conecta ao banco
conexao = sqlite3.connect(db_file)
cursor = conexao.cursor() 

#Listagem simples para verificar o nome e e-mail de clientes de São Paulo
cursor.execute("SELECT nome, email FROM" \
" Clientes WHERE cidade='São Paulo';")
clientes = cursor.fetchall()
print(f"1. Clientes de São Paulo: {clientes}\n")


#Filtro de preço para avaliar produtos que custam mais que 800R$
cursor.execute("SELECT nome_produto, preco FROM" \
" Produtos WHERE preco > 800;")
produtos = cursor.fetchall()
print(f"2. Produtos acima de 800R$: {produtos}\n")

#Relatório de vendas para verificar o que cada cliente comprou
cursor.execute("SELECT nome, nome_produto FROM"
" ((Vendas JOIN Clientes ON Vendas.id_cliente = Clientes.id_cliente) JOIN Produtos ON Vendas.id_produto = Produtos.id_produto)")
relatorio = cursor.fetchall()
print("3. O que cada cliente comprou:")
for i in range(len(relatorio)):
    print(f"- Cliente {relatorio[i][0]} comprou um {relatorio[i][1]}\n")

#Faturamento total das vendas
cursor.execute("SELECT SUM(Vendas.quantidade * Produtos.preco) FROM" \
" Vendas" \
" INNER JOIN Produtos ON Produtos.id_produto = Vendas.id_produto")
faturamento = cursor.fetchone()[0]
print(f"4. Faturamento total da loja: {faturamento} \n")

#Fornecer o nome e o quanto cada cliente gastou por ordem decrescente 
cursor.execute("SELECT Clientes.nome, SUM(Vendas.quantidade * Produtos.preco) AS ValorGasto FROM" \
" Vendas" \
" INNER JOIN Produtos ON Produtos.id_produto = Vendas.id_produto" \
" INNER JOIN Clientes ON Clientes.id_cliente = Vendas.id_cliente" \
" GROUP BY Clientes.nome" \
" ORDER BY ValorGasto DESC;")
resultados = cursor.fetchall()
print("5. Balanço de quanto cada cliente gastou: ")
for i in range(len(resultados)):
    print(f"- Cliente {resultados[i][0]} gastou {resultados[i][1]} na loja\n")

# Salva as alterações e fecha
conexao.commit()
conexao.close()
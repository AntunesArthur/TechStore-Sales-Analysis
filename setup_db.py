import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

#Guarda o SQL dentro de uma variável de texto 
sql_script = """
-- 1. Criação das Tabelas
DROP TABLE IF EXISTS Vendas;
DROP TABLE IF EXISTS Clientes;
DROP TABLE IF EXISTS Produtos;

CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    cidade VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE Produtos (
    id_produto INT PRIMARY KEY,
    nome_produto VARCHAR(100),
    preco DECIMAL(10, 2),
    categoria VARCHAR(50)
);

CREATE TABLE Vendas (
    id_venda INT PRIMARY KEY,
    id_cliente INT,
    id_produto INT,
    data_venda DATE,
    quantidade INT,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
);

-- 2. Inserção de Dados
INSERT INTO Clientes VALUES 
(1, 'Ana Silva', 'São Paulo', 'ana@email.com'),
(2, 'Bruno Souza', 'Rio de Janeiro', 'bruno@email.com'),
(3, 'Carla Dias', 'Belo Horizonte', 'carla@email.com'),
(4, 'Daniel Rocha', 'São Paulo', 'daniel@email.com');

INSERT INTO Produtos VALUES 
(101, 'Notebook Dell', 3500.00, 'Eletrônicos'),
(102, 'Mouse Logitech', 150.00, 'Acessórios'),
(103, 'Monitor LG 24', 900.00, 'Eletrônicos'),
(104, 'Teclado Mecânico', 250.00, 'Acessórios');

INSERT INTO Vendas VALUES 
(1, 1, 101, '2025-01-10', 1),
(2, 2, 103, '2025-01-12', 2),
(3, 3, 102, '2025-01-15', 1),
(4, 1, 102, '2025-01-16', 1),
(5, 4, 104, '2025-01-20', 3);
"""
#Executa o script
cursor.executescript(sql_script)
conexao.commit()
conexao.close()
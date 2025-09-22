#criando e conectanto ao banco de dados

import sqlite3

#Criar a uma conexão com banco de dados chamado de "escola.db"
conexao = sqlite3.connect("escola.db")

#Criamos um objeto "cursor" vai servir para executar os comandos SQL

cursor = conexao.cursor()

#Criando uma tabela no banco chamada de "alunos"

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    curso TEXT                      
    )             
               
               
""")
print("Tabela criada com sucesso!")



#Inserindo um valor no banco de dados (aluno)

cursor.execute("""
INSERT INTO alunos (nome, idade, curso)
VALUES (?, ?, ?)                          
""", 
("Laura", 24, "Engenharia")
)

lista_alunos = [
    ("Raul", 20, "Direito"),
    ("Vinicius", 31, "Computação"),
    ("Vitoria", 78, "medicina"),
]

#Executemany permite inserir múltiplas linhas
cursor.executemany("""
INSERT INTO alunos (nome, idade, curso)
VALUES (?, ?, ?)                          
""",
lista_alunos )


#Confirmar as alterações do banco

conexao.commit()
print("Dados inseridos com sucesso!")
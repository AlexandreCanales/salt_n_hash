import bcrypt
import sqlite3

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

senha_em_bytes = senha.encode('utf-8')

salt = bcrypt.gensalt()
hash_seguro = bcrypt.hashpw(senha_em_bytes, salt).decode('utf-8')  # Convertemos para string

conexao = sqlite3.connect("banco_senhas.db")
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        usuario TEXT PRIMARY KEY,
        senha TEXT
    )
''')

cursor.execute("SELECT usuario FROM usuarios WHERE usuario = ?", (usuario,))
if cursor.fetchone():
    print("Este usuário já existe!")
else:
    cursor.execute("INSERT INTO usuarios VALUES (?, ?)", (usuario, hash_seguro))
    conexao.commit()
    print("Cadastro realizado com sucesso!")

conexao.close()






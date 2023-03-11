import sqlite3
bd = sqlite3.connect('escola.db')
comandoSQL = "insert into alunos (matricula, nome, nota1, nota2, nota3) values(?,?,?,?,?);"
try:
  cur = bd.cursor()
  cur.execute(comandoSQL,(1,'José',8.0,4.5,7.5))
  bd.commit()
  print ("Um registro incluido com sucesso")
except sqlite3.Error as erro:
  print("Erro na operação:",erro)
  bd.rollback()

bd.close()
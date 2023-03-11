import sqlite3
bd=sqlite3.connect('escola.db')
cur = bd.cursor()
comandoSQL = "select * from alunos;"
cur.execute(comandoSQL)
while True:
  registro = cur.fetchone()
  if registro == None:
    break
  print (registro)
bd.close()
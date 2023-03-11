# Criar BD
import sqlite3
bd = sqlite3.connect('escola.db')

# Criar Tabela
try:        
  cur = bd.cursor()
  comandoSQL = '''create table alunos (
                  matricula integer primary key,
                  nome text(20) not null,
                  nota1 float null,
                  nota2 float null,
                  nota3 float null)'''

  cur.execute(comandoSQL)
  print ('Tabela de alunos criada com sucesso')
except sqlite3.Error as erro:
  print("Erro na operação:",erro)
  bd.rollback()

bd.close()
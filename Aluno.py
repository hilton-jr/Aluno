import sqlite3

class Aluno:
    def __init__(self,matAluno,nomeAluno):
        self.matricula = matAluno
        self.nome = nomeAluno
        self.nota1 = 0
        self.nota2 = 0
        self.nota3 = 0
        
    def lanca_notas(self,n1,n2,n3):
        self.nota1 = n1
        self.nota2 = n2
        self.nota3 = n3

    def calc_media(self):
        return (self.nota1 + self.nota2 + self.nota3)/3
    
    def situacao(self):
        if self.calc_media() >= 7.0:
            return 'Aprovado'
        else:
            return 'Reprovado'
    
    def inserir_bd(self):
        bd = sqlite3.connect('escola.db')
        comandoSQL = "insert into alunos (matricula, nome, nota1, nota2, nota3) values(?,?,?,?,?);"
        try:
            cur = bd.cursor()
            cur.execute(comandoSQL,(self.matricula, self.nome, self.nota1, self.nota2, self.nota3))
            bd.commit()
            print ("Um registro incluido com sucesso")
        except sqlite3.Error as erro:
            print("Erro na operação:",erro)
            bd.rollback()
        bd.close()

    def recuperar_aluno_bd(self, mat):
        bd=sqlite3.connect('escola.db')
        cur = bd.cursor()
        comandoSQL = "select nome,nota1,nota2,nota3 from alunos where matricula = ?;"
        cur.execute(comandoSQL,(str(mat)))
        registro = cur.fetchone()
        if registro == None:
            resposta = False
        else:
            self.nome = registro[0]
            self.nota1 = registro[1]
            self.nota2 = registro[2]
            self.nota3 = registro[3]
            resposta = True
        bd.close()
        return resposta

    def excluir_aluno_bd(self, mat):
        bd=sqlite3.connect('escola.db')
        cur = bd.cursor()
        comandoSQL = "delete from alunos where matricula=?;"
        try:
            cur=bd.cursor()
            cur.execute(comandoSQL, (str(mat)))
            bd.commit()
            resposta = True
        except sqlite3.Error as erro:
            print("Erro na operação:",erro)
            bd.rollback()
            resposta = False
        bd.close()
        return resposta        

    def alterar_aluno_bd(self,mat,nome,nota1,nota2,nota3):
        bd=sqlite3.connect('escola.db')
        cur = bd.cursor()
        comandoSQL = '''update alunos  
                        set nome = ?, nota1 = ?, nota2 = ?, nota3 = ?
                        where matricula = ?;'''
        try:
            cur=bd.cursor()
            cur.execute(comandoSQL,(nome,nota1,nota2,nota3,(str(mat))))
            bd.commit()
            resposta = True
        except sqlite3.Error as erro:
            print("Erro na operação:",erro)
            bd.rollback()
            resposta = False
        bd.close()
        return resposta    
    
    

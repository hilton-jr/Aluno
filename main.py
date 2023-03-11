from Aluno import Aluno
import sqlite3

while True:
    print('''

          =================================
                 CADASTRO DE ALUNOS
          =================================
          1. Incluir um novo aluno
          2. Alterar dados de um aluno
          3. Excluir um aluno
          4. Consultar dados de um aluno
          5. Relatório de aprovação
          6. Sair da aplicação
          =================================
          ''')
    opcao = int(input("Entre com a opção desejada: "))
    
    match opcao:
        case 1:
            print('Opção 1 foi escolhida.\n')
            mt = int(input('Informe matricula: '))
            mn = input('Informe nome: ')
            novoAluno = Aluno(mt,mn)
            novoAluno.inserir_bd()            
            continue
        case 2:
            print('Opção 2 foi escolhida.')
            mt = int(input('Informe matricula: '))
            aluno = Aluno(mt,'fulano')
            print('-'*40)
            if aluno.recuperar_aluno_bd(mt):
                print(f'Matricula: {aluno.matricula}')
                print(f'Nome: {aluno.nome}')
                print(f'Nota 1: {aluno.nota1}')
                print(f'Nota 2: {aluno.nota2}')
                print(f'Nota 3: {aluno.nota3}')
                novoNome = input('\nInforme o novo nome do aluno: ')
                novaNota1 = input('Informe a nova nota 1 do aluno: ')
                novaNota2 = input('Informe a nova nota 2 do aluno: ')
                novaNota3 = input('Informe a nova nota 3 do aluno: ')
                if aluno.alterar_aluno_bd(mt,novoNome,novaNota1,novaNota2,novaNota3):
                    print(f'Dados da matricula {mt} alterada no banco de dados')
                else:
                    print(f'ERRO: Aluno {mt} não foi alterado')
            else:
                print(f'ERRO: Matricula {mt} não existe no banco de dados')
            print('-'*40)
            continue
        case 3:
            print('Opção 3 foi escolhida.')
            mt = int(input('Informe matricula: '))
            aluno = Aluno(mt,'fulano')
            print('-'*40)
            if aluno.recuperar_aluno_bd(mt):
                print(f'Matricula: {aluno.matricula}')
                print(f'Nome: {aluno.nome}')
                print(f'Nota 1: {aluno.nota1}')
                print(f'Nota 2: {aluno.nota2}')
                print(f'Nota 3: {aluno.nota3}')
                conf = input('\nConfirma a excusão? (s/n)')
                if conf=='s':
                    if aluno.excluir_aluno_bd(mt):
                        print(f'Matricula {mt} excluída do banco de dados')
                    else:
                        print(f'ERRO: Matricula {mt} não foi excluída')
            else:
                print(f'ERRO: Matricula {mt} não existe no banco de dados')
            print('-'*40)
            continue
            continue
        case 4:
            print('Opção 4 foi escolhida.\n')
            mt = int(input('Informe matricula: '))
            aluno = Aluno(mt,'fulano')
            print('-'*40)
            if aluno.recuperar_aluno_bd(mt):
                print(f'Matricula: {aluno.matricula}')
                print(f'Nome: {aluno.nome}')
                print(f'Nota 1: {aluno.nota1}')
                print(f'Nota 2: {aluno.nota2}')
                print(f'Nota 3: {aluno.nota3}')
            else:
                print(f'ERRO: Matricula {mt} não existe no banco de dados')
            print('-'*40)
            continue
        case 5:
            print('Opção 5 foi escolhida.')
            bd=sqlite3.connect('escola.db')
            cur = bd.cursor()
            comandoSQL = "select matricula,nome,nota1,nota2,nota3 from alunos;"
            cur.execute(comandoSQL)
            print ('(matricula, nome, nota1,nota2,nota3) media situacao)')
            while True:
                registro = cur.fetchone()
                if registro == None:
                    break
                n1 = float(registro[2])
                n2 = float(registro[3])
                n3 = float(registro[4])
                media = (n1+n2+n3)/3
                if media >= 7.0:
                    situacao = 'Aprovado'
                else:
                    situacao = 'Reprovado'
                print (registro, media, situacao)
            bd.close()
            continue
        case 6:
            print('Encerrando a aplicação...')
            break
        case _:
            print('ERRO: Opção inválida!')
            
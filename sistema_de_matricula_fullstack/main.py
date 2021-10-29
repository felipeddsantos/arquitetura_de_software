'''

Arquitetura de Software - Sistema de Matrícula FullStack (Programa Principal)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from flask import Flask, render_template, url_for, request, json, jsonify, flash, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.validators import Required
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, text, select, create_engine, exc, exists
from aluno import Aluno
from professor import Professor
from coordenador import Coordenador
from disciplina import Disciplina
from banco import Banco

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'any secret string'

alunos = []
disciplinas = []
requisicoes = []

@app.route('/aAluno', methods = ['GET', 'POST'])
def aAluno():

   try:

      if(request.method == 'GET'):

         db = Banco()
         res = db.criarTabelaAluno()

         if(res == False):

             return 'Erro inesperado. Tente novamente mais tarde.'

         else:

            matricula = request.args.get('matricula')
            senha = request.args.get('senha')

            aluno = Aluno('', '', matricula, '', '', '', '', '')

            s = db.obterAluno(aluno, res)

            if(s == False):

               return 'Erro inesperado. Tente novamente mais tarde.'

            for row in s:

               if(row.senha == senha):

                     trig = 'sucesso'

                     nome = row.nome

                     sobrenome = row.sobrenome

                     global matricula_aluno

                     matricula_aluno = row.matricula

                     return render_template('paluno.html', trig = trig, nome = nome, sobrenome = sobrenome)

               else:

                  trig1 = ''

                  trig2 = 'senha'

                  return render_template('laluno.html', trig1 = trig1, trig2 = trig2)

            trig1 = 'matricula'

            trig2 = ''

            return render_template('laluno.html', trig1 = trig1, trig2 = trig2)

      if(request.method == 'POST'):

         if(request.form.get('senha') != request.form.get('senha2')):

            trig1 = 'senha'

            trig2 = ''

            return render_template('raluno.html', trig1 = trig1, trig2 = trig2)

         nome = request.form.get('nome')
         sobrenome = request.form.get('sobrenome')
         matricula = request.form.get('matricula')
         email = request.form.get('email')
         senha = request.form.get('senha')
         nascimento = request.form.get('nascimento')
         telefone = request.form.get('telefone')
         curso = request.form.get('curso')
         
         aluno = Aluno(nome, sobrenome, matricula, email, senha, nascimento, telefone, curso)
         
         db = Banco()
         res = db.criarTabelaAluno()

         if(res == False):

             return 'Erro inesperado. Tente novamente mais tarde.'

         else:

            s = db.obterAluno(aluno, res)

            if(s == False):

               return 'Erro inesperado. Tente novamente mais tarde.'

            for row in s:

               trig1 = ''

               trig2 = 'matricula'

               return render_template('raluno.html', trig1 = trig1, trig2 = trig2)

            if(db.adicionarAluno(aluno, res)):

               trig = 'sucesso'

               return render_template('principal.html', trig = trig)

            else:
          
               return 'Erro inesperado. Tente novamente mais tarde.'

   except:

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/aProfessor', methods = ['GET', 'POST'])
def aProfessor():

   try:

      if(request.method == 'GET'):

         db = Banco()
         res = db.criarTabelaProfessor()

         if(res == False):

             return 'Erro inesperado. Tente novamente mais tarde.'

         else:

            registro_professor = request.args.get('registro')
            senha = request.args.get('senha')

            professor = Professor('', '', registro_professor, '', '', '', '', '')

            s = db.obterProfessor(professor, res)

            if(s == False):

               return 'Erro inesperado. Tente novamente mais tarde.'

            for row in s:

               if(row.senha == senha):

                     trig = 'sucesso'

                     nome = row.nome

                     sobrenome = row.sobrenome

                     global registro_professor_r

                     registro_professor_r = row.registro

                     return render_template('pprofessor.html', trig = trig, nome = nome, sobrenome = sobrenome)

               else:

                  trig1 = ''

                  trig2 = 'senha'

                  return render_template('lprofessor.html', trig1 = trig1, trig2 = trig2)

            trig1 = 'registro'

            trig2 = ''

            return render_template('lprofessor.html', trig1 = trig1, trig2 = trig2)

      if(request.method == 'POST'):

         if(request.form.get('senha') != request.form.get('senha2')):

            trig1 = 'senha'

            trig2 = ''

            return render_template('rprofessor.html', trig1 = trig1, trig2 = trig2)

         nome = request.form.get('nome')
         sobrenome = request.form.get('sobrenome')
         registro = request.form.get('registro')
         email = request.form.get('email')
         senha = request.form.get('senha')
         nascimento = request.form.get('nascimento')
         telefone = request.form.get('telefone')
         unidade = request.form.get('unidade')

         professor = Professor(nome, sobrenome, registro, email, senha, nascimento, telefone, unidade)

         db = Banco()
         res = db.criarTabelaProfessor()

         if(res == False):

             return 'Erro inesperado. Tente novamente mais tarde.'

         else:

            s = db.obterProfessor(professor, res)

            if(s == False):

               return 'Erro inesperado. Tente novamente mais tarde.'

            for row in s:

               trig1 = ''

               trig2 = 'registro'

               return render_template('rprofessor.html', trig1 = trig1, trig2 = trig2)

            if(db.adicionarProfessor(professor, res)):

               trig = 'sucesso'

               return render_template('principal.html', trig = trig)

            else:
          
               return 'Erro inesperado. Tente novamente mais tarde.'

   except:

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/aCoordenador', methods = ['GET', 'POST'])
def aCoordenador():

   try:

      if(request.method == 'GET'):

         db = Banco()
         res = db.criarTabelaCoordenador()

         if(res == False):

             return 'Erro inesperado. Tente novamente mais tarde.'

         else:

            registro = request.args.get('registro')
            senha = request.args.get('senha')

            coordenador = Coordenador('', '', registro, '', '', '', '', '')

            s = db.obterCoordenador(coordenador, res)

            if(s == False):

               return 'Erro inesperado. Tente novamente mais tarde.'

            for row in s:

               if(row.senha == senha):

                     trig = 'sucesso'

                     nome = row.nome

                     sobrenome = row.sobrenome

                     global registro_coordenador

                     registro_coordenador = row.registro

                     return render_template('pcoordenador.html', trig = trig, nome = nome, sobrenome = sobrenome)

               else:

                  trig1 = ''

                  trig2 = 'senha'

                  return render_template('lcoordenador.html', trig1 = trig1, trig2 = trig2)

            trig1 = 'registro'

            trig2 = ''

            return render_template('lcoordenador.html', trig1 = trig1, trig2 = trig2)

      if(request.method == 'POST'):

         if(request.form.get('senha') != request.form.get('senha2')):

            trig1 = 'senha'

            trig2 = ''

            return render_template('rcoordenador.html', trig1 = trig1, trig2 = trig2)

         nome = request.form.get('nome')
         sobrenome = request.form.get('sobrenome')
         registro = request.form.get('registro')
         email = request.form.get('email')
         senha = request.form.get('senha')
         nascimento = request.form.get('nascimento')
         telefone = request.form.get('telefone')
         curso = request.form.get('curso')

         coordenador = Coordenador(nome, sobrenome, registro, email, senha, nascimento, telefone, curso)

         db = Banco()
         res = db.criarTabelaCoordenador()

         if(res == False):

             return 'Erro inesperado. Tente novamente mais tarde.'

         else:

            s = db.obterCoordenador(coordenador, res)

            if(s == False):

               return 'Erro inesperado. Tente novamente mais tarde.'

            for row in s:

               trig1 = ''

               trig2 = 'registro'

               return render_template('rcoordenador.html', trig1 = trig1, trig2 = trig2)

            if(db.adicionarCoordenador(coordenador, res)):

               trig = 'sucesso'

               return render_template('principal.html', trig = trig)

            else:
          
               return 'Erro inesperado. Tente novamente mais tarde.'

   except:

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/aDisciplina', methods = ['GET', 'POST'])
def aDisciplina():

   try:

      if(request.method == 'POST'):

         nome = request.form.get('nome')
         codigo = request.form.get('codigo')
         horario = request.form.get('horario')
         unidade = request.form.get('unidade')
         registro_professor = request.form.get('registro_professor')

         db = Banco()
         res = db.criarTabelaDisciplina()

         if(res == False):

             return 'Erro inesperado. Tente novamente mais tarde.'

         else:

            disciplina = Disciplina('', codigo, '', '', '', '')

            s = db.obterDisciplina(codigo, res)

            if(s == False):

               return 'Erro inesperado. Tente novamente mais tarde.'

            for row in s:

               trig1 = 'codigo'

               trig2 = ''

               return render_template('rdisciplina.html', trig1 = trig1, trig2 = trig2)

         res = db.criarTabelaProfessor()

         if(res == False):

             return 'Erro inesperado. Tente novamente mais tarde.'

         else:

            professor = Professor('', '', registro_professor, '', '', '', '', '')

            s = db.obterProfessor(professor, res)

            if(s == False):

               return 'Erro inesperado. Tente novamente mais tarde.'

            for row in s:

               res = db.criarTabelaDisciplina()

               global registro_coordenador

               disciplina = Disciplina(nome, codigo, horario, unidade, registro_professor, registro_coordenador)

               if(db.adicionarDisciplina(disciplina, res)):

                  trig = 'dsucesso'

                  return render_template('pcoordenador.html', trig = trig)

            trig1 = ''

            trig2 = 'professor'

            return render_template('rdisciplina.html', trig1 = trig1, trig2 = trig2)

   except:

      return 'Erro inesperado. Tente novamente mais tarde'

@app.route('/rAluno', methods=['GET', 'POST'])
def rAluno():

   try:

      trig1 = ''

      trig2 = ''

      return render_template('raluno.html', trig1 = trig1, trig2 = trig2)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/rProfessor', methods=['GET', 'POST'])
def rProfessor():

   try:

      trig1 = ''

      trig2 = ''

      return render_template('rprofessor.html', trig1 = trig1, trig2 = trig2)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/rCoordenador', methods=['GET', 'POST'])
def rCoordenador():

   try:

      trig1 = ''

      trig2 = ''

      return render_template('rcoordenador.html', trig1 = trig1, trig2 = trig2)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/rDisciplina', methods = ['GET', 'POST'])
def rDisciplina():

   try:

      trig1 = ''

      trig2 = ''

      return render_template('rdisciplina.html', trig1 = trig1, trig2 = trig2)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/rMatricula', methods = ['GET', 'POST'])
def rMatricula():

   try:

      if(request.method == 'GET'):

         db = Banco()
         res = db.criarTabelaRequisicao()

         if(res == False):

             return 'Erro inesperado. Tente novamente mais tarde.'

         else:

            for cada in disciplinas:

               if request.args.get(str(cada.codigo)) != None:

                  global matricula_aluno

                  if(db.adicionarRequisicao(matricula_aluno, cada.codigo, cada.registro_coordenador, res) == False):

                     return 'Erro inesperado. Tente novamente mais tarde.'

            trig = 'dsucesso'

            return render_template('paluno.html', trig = trig)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/lAluno', methods = ['GET', 'POST'])
def lAluno():

   try:

      trig1 = ''

      trig2 = ''

      return render_template('laluno.html', trig1 = trig1, trig2 = trig2)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/lProfessor', methods = ['GET', 'POST'])
def lProfessor():

   try:

      trig1 = ''

      trig2 = ''

      return render_template('lprofessor.html', trig1 = trig1, trig2 = trig2)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/lCoordenador', methods = ['GET', 'POST'])
def lCoordenador():

   try:

      trig1 = ''

      trig2 = ''

      return render_template('lcoordenador.html', trig1 = trig1, trig2 = trig2)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/disciplinasProfessor', methods = ['GET', 'POST'])
def disciplinasProfessor():

   try:

      db = Banco()
      res = db.criarTabelaDisciplina()

      if(res == False):

         return 'Erro inesperado. Tente novamente mais tarde.'

      global registro_professor_r

      disciplina = Disciplina('', '', '', '', registro_professor_r, '')

      s = db.obterDisciplinaProfessor(disciplina, res)

      disciplinas.clear()

      for row in s:

         disciplinas.append(row)

      if(s == False):

         return 'Erro inesperado. Tente novamente mais tarde.'

      return render_template('disciplinasprofessor.html', disciplinas = disciplinas)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/notasProfessor', methods = ['GET', 'POST'])
def notasProfessor():

   try:

      disciplina_selecionada = request.args.get('selecionado')

      db = Banco()
      res = db.criarTabelaMatricula()

      if(res == False):

         return 'Erro inesperado. Tente novamente mais tarde.'

      s = db.obterMatricula(disciplina_selecionada, res)

      print(disciplina_selecionada)

      alunos.clear()

      for row in s:

         print(row.aluno)

         alunos.append(row)

      return render_template('notasprofessor.html', alunos = alunos)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/notas', methods = ['GET', 'POST'])
def notas():

   try:

      db = Banco()
      res = db.criarTabelaMatricula()

      global matricula_aluno

      if(res == False):

         return 'Erro inesperado. Tente novamente mais tarde.'

      s = db.obterMatriculaAluno(matricula_aluno, res)

      res = db.criarTabelaDisciplina()

      alunos.clear()

      disciplinas.clear()

      for row in s:

         alunos.append(row)

         r = db.obterDisciplina(row.disciplina, res)

         for cada in r:

            disciplinas.append(cada.nome)

      return render_template('notas.html', alunos = alunos, disciplinas = disciplinas)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/matricula', methods = ['GET', 'POST'])
def matricula():

   try:

      db = Banco()
      res = db.criarTabelaDisciplina()

      if(res == False):

         return 'Erro inesperado. Tente novamente mais tarde.'

      s = db.obterTodasDisciplinas(res)

      disciplinas.clear()

      for row in s:

         disciplinas.append(row)

      if(s == False):

         return 'Erro inesperado. Tente novamente mais tarde.'

      return render_template('matricula.html', disciplinas = disciplinas)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/aMatricula', methods = ['GET', 'POST'])
def aMatricula():

   try:

      if(request.method == 'GET'):

         db = Banco()
         res = db.criarTabelaMatricula()

         requisicoes.clear()

         if(res == False):

             return 'Erro inesperado. Tente novamente mais tarde.'

         else:

            for cada in disciplinas:

               if request.args.get(str(cada.disciplina) + str(cada.aluno)) == (str(cada.disciplina) + str(cada.aluno)):

                  print("ok")

                  if(db.adicionarMatricula(cada.aluno, cada.disciplina, 0, 0.0, res) == False):

                     return 'Erro inesperado. Tente novamente mais tarde.'

                  requisicoes.append(cada)

            res = db.criarTabelaRequisicao()

            if(res == False):

               return 'Erro inesperado. Tente novamente mais tarde.'

            else:

               for cada in requisicoes:

                  s = db.obterTodasRequisicao(res)

                  for row in s:

                     if(row.aluno == cada.aluno) and (row.disciplina == cada.disciplina):

                        if(db.deletarRequisicao(row.id_requisicao, res) == False):

                           return 'Erro inesperado. Tente novamente mais tarde.'
      
               trig = 'asucesso'

               return render_template('pcoordenador.html', trig = trig)

   except:

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/matriculasCoordenador', methods = ['GET', 'POST'])
def matriculasCoordenador():

   try:

      db = Banco()
      res = db.criarTabelaRequisicao()

      if(res == False):

         return 'Erro inesperado. Tente novamente mais tarde.'

      s = db.obterRequisicao(registro_coordenador, res)

      disciplinas.clear()

      for row in s:

         disciplinas.append(row)

      if(s == False):

         return 'Erro inesperado. Tente novamente mais tarde.'

      return render_template('matriculascoordenador.html', disciplinas = disciplinas)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/listaProfessor', methods = ['GET', 'POST'])
def listaProfessor():

   try:

      db = Banco()
      res = db.criarTabelaMatricula()

      for cada in alunos:

         nota = request.form.get(str(cada.id_matricula) + 'a')

         faltas = request.form.get(cada.aluno)

         s = db.atualizarMatricula(cada.id_matricula, cada.aluno, cada.disciplina, nota, faltas, res)

      trig = 'alterar'

      return render_template('pprofessor.html', trig = trig)

   except:

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/logout', methods = ['GET', 'POST'])
def logout():

   try:

      trig = ''

      global matricula_aluno

      global registro_professor_r

      matricula_aluno = ''

      registro_professor_r = ''

      return render_template('principal.html', trig = trig)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/pAluno', methods = ['GET', 'POST'])
def pAluno():

   try:

      trig = ''

      return render_template('paluno.html', trig = trig)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/pProfessor', methods = ['GET', 'POST'])
def pProfessor():

   try:

      trig = ''

      return render_template('pprofessor.html', trig = trig)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/pCoordenador', methods = ['GET', 'POST'])
def pCoordenador():

   try:

      trig = ''

      return render_template('pcoordenador.html', trig = trig)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

@app.route('/', methods = ['GET', 'POST'])
def main():

   try:

      trig = ''

      return render_template('principal.html', trig = trig)

   except: 

      return 'Erro inesperado. Tente novamente mais tarde.'

if __name__ == '__main__':

   app.run(debug = True, host = '0.0.0.0', port = 8080)

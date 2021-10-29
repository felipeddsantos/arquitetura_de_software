'''

Arquitetura de Software - Sistema de Matrícula (Classe Banco de Dados)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, Date, text, select, delete, create_engine, exc, exists, Float

class Banco:

    db = create_engine("postgresql+psycopg2://postgres:m@rvel314@localhost/ASA")

    def criarTabelaAluno(self):

        try:

            metadados = MetaData()
            aluno_tb = Table('tb_alunos', metadados, Column('id_aluno', Integer, primary_key=True), Column('nome', String(60)), Column('sobrenome', String(60)), Column('matricula', String(30)), Column('email', String(30)), Column('senha', String(30)), Column('nascimento', Date), Column('telefone', String(20)), Column('curso', String(60)))
            metadados.create_all(self.db)
            res = aluno_tb

        except:

            res = False

        return res

    def criarTabelaProfessor(self):

        try:

            metadados = MetaData()
            professor_tb = Table('tb_professores', metadados, Column('id_professor', Integer, primary_key=True), Column('nome', String(60)), Column('sobrenome', String(60)), Column('registro', String(30)), Column('email', String(30)), Column('senha', String(30)), Column('nascimento', Date), Column('telefone', String(20)), Column('unidade', String(60)))            
            metadados.create_all(self.db)
            res = professor_tb

        except:

            res = False

        return res

    def criarTabelaCoordenador(self):

        try:

            metadados = MetaData()
            coordenador_tb = Table('tb_coordenadores', metadados, Column('id_coordenador', Integer, primary_key=True), Column('nome', String(60)), Column('sobrenome', String(60)), Column('registro', String(30)), Column('email', String(30)), Column('senha', String(30)), Column('nascimento', Date), Column('telefone', String(20)), Column('curso', String(60)))            
            metadados.create_all(self.db)
            res = coordenador_tb

        except:

            res = False

        return res

    def criarTabelaDisciplina(self):

        try:

            metadados = MetaData()
            disciplina_tb = Table('tb_disciplinas', metadados, Column('id_disciplina', Integer, primary_key=True), Column('nome', String(60)), Column('codigo', String(20)), Column('horario', String(20)), Column('unidade', String(50)), Column('registro_professor', String(30)), Column('registro_coordenador', String(30)))           
            metadados.create_all(self.db)
            res = disciplina_tb

        except:

            res = False

        return res

    def criarTabelaMatricula(self):

        try:

            metadados = MetaData()
            matricula_tb = Table('tb_matriculas', metadados, Column('id_matricula', Integer, primary_key=True), Column('aluno', String(30)), Column('disciplina', String(30)), Column('faltas', Integer), Column('nota', Float))           
            metadados.create_all(self.db)
            res = matricula_tb

        except:

            res = False

        return res

    def criarTabelaRequisicao(self):

        try:

            metadados = MetaData()
            requisicao_tb = Table('tb_requisicoes', metadados, Column('id_requisicao', Integer, primary_key=True), Column('aluno', String(30)), Column('disciplina', String(30)), Column('coordenador', String(30)))           
            metadados.create_all(self.db)
            res = requisicao_tb

        except:

            res = False

        return res

    def adicionarAluno(self, aluno, aluno_tb):
    
        try:

           insert_command = aluno_tb.insert().values(nome = aluno.nome, sobrenome = aluno.sobrenome, matricula = aluno.matricula, email = aluno.email, senha = aluno.senha, nascimento = aluno.nascimento, telefone = aluno.telefone, curso = aluno.curso)
           conn = self.db.connect()
           conn.execute(insert_command)
           res = True
    
        except:

           res = False

        return res

    def adicionarProfessor(self, professor, professor_tb):
    
        try:

           insert_command = professor_tb.insert().values(nome = professor.nome, sobrenome = professor.sobrenome, registro = professor.registro, email = professor.email, senha = professor.senha, nascimento = professor.nascimento, telefone = professor.telefone, unidade = professor.unidade)
           conn = self.db.connect()
           conn.execute(insert_command)
           res = True
    
        except:

           res = False

        return res

    def adicionarCoordenador(self, coordenador, coordenador_tb):
    
        try:

           insert_command = coordenador_tb.insert().values(nome = coordenador.nome, sobrenome = coordenador.sobrenome, registro = coordenador.registro, email = coordenador.email, senha = coordenador.senha, nascimento = coordenador.nascimento, telefone = coordenador.telefone, curso = coordenador.curso)
           conn = self.db.connect()
           conn.execute(insert_command)
           res = True
    
        except:

           res = False

        return res

    def adicionarDisciplina(self, disciplina, disciplina_tb):
    
        try:

           insert_command = disciplina_tb.insert().values(nome = disciplina.nome, codigo = disciplina.codigo, horario = disciplina.horario, unidade = disciplina.unidade, registro_professor = disciplina.registro_professor, registro_coordenador = disciplina.registro_coordenador)
           conn = self.db.connect()
           conn.execute(insert_command)
           res = True
    
        except:

           res = False

        return res

    def adicionarMatricula(self, aluno, disciplina, faltas, nota, matricula_tb):
    
        try:

           insert_command = matricula_tb.insert().values(aluno = aluno, disciplina = disciplina, faltas = faltas, nota = nota)
           conn = self.db.connect()
           conn.execute(insert_command)
           res = True
    
        except:

           res = False

        return res

    def adicionarRequisicao(self, aluno, disciplina, coordenador, requisicao_tb):
    
        try:

           insert_command = requisicao_tb.insert().values(aluno = aluno, disciplina = disciplina, coordenador = coordenador)
           conn = self.db.connect()
           conn.execute(insert_command)
           res = True
    
        except:

           res = False

        return res

    def atualizarAluno(self, aluno, matricula, aluno_tb):
    
        try:

           insert_command = aluno_tb.update().where(aluno_tb.c.matricula).values(nome = aluno.nome, sobrenome = aluno.sobrenome, matricula = aluno.maricula, email = aluno.email, senha = aluno.senha, nascimento = aluno.nascimento, telefone = aluno.telefone, curso = aluno.curso)
           conn = self.db.connect()
           conn.execute(insert_command)
           res = True
    
        except:

           res = False

        return res

    def atualizarProfessor(self, professor, registro, professor_tb):
    
        try:

           insert_command = aluno_tb.update().where(aluno_tb.c.matricula).values(nome = professor.nome, sobrenome = professor.sobrenome, registro = professor.registro, email = professor.email, senha = professor.senha, nascimento = professor.nascimento, telefone = professor.telefone, unidade = professor.unidade)
           conn = self.db.connect()
           conn.execute(insert_command)
           res = True
    
        except:

           res = False

        return res

    def atualizarCoordenador(self, coordenador, registro, coordenador_tb):
    
        try:

           insert_command = aluno_tb.update().where(aluno_tb.c.matricula).values(nome = coordenador.nome, sobrenome = coordenador.sobrenome, registro = coordenador.registro, email = coordenador.email, senha = coordenador.senha, nascimento = coordenador.nascimento, telefone = coordenador.telefone, curso = coordenador.curso)
           conn = self.db.connect()
           conn.execute(insert_command)
           res = True
    
        except:

           res = False

        return res

    def atualizarMatricula(self, id_matricula, matricula, codigo, nota, faltas, matricula_tb):
    
        try:

           insert_command = matricula_tb.update().where(matricula_tb.c.id_matricula == id_matricula).values(aluno = matricula, disciplina = codigo, faltas = faltas, nota = nota)
           conn = self.db.connect()
           conn.execute(insert_command)
           res = True
    
        except:

           res = False

        return res

    def obterAluno(self, aluno, aluno_tb):
    
        try:

           insert_command = aluno_tb.select().where(aluno_tb.c.matricula == aluno.matricula)
           conn = self.db.connect()
           res = conn.execute(insert_command)
         
        except:

           res = False

        return res

    def obterProfessor(self, professor, professor_tb):
    
        try:

           insert_command = professor_tb.select().where(professor_tb.c.registro == professor.registro)
           conn = self.db.connect()
           res = conn.execute(insert_command)
         
        except:

           res = False

        return res

    def obterCoordenador(self, coordenador, coordenador_tb):
    
        try:

           insert_command = coordenador_tb.select().where(coordenador_tb.c.registro == coordenador.registro)
           conn = self.db.connect()
           res = conn.execute(insert_command)
         
        except:

           res = False

        return res

    def obterDisciplina(self, disciplina, disciplina_tb):
    
        try:

           insert_command = disciplina_tb.select().where(disciplina_tb.c.codigo == disciplina)
           conn = self.db.connect()
           res = conn.execute(insert_command)
         
        except:

           res = False

        return res

    def obterDisciplinaProfessor(self, disciplina, disciplina_tb):
    
        try:

           insert_command = disciplina_tb.select().where(disciplina_tb.c.registro_professor == disciplina.registro_professor)
           conn = self.db.connect()
           res = conn.execute(insert_command)
         
        except:

           res = False

        return res

    def obterTodasDisciplinas(self, disciplina_tb):
    
        try:

           insert_command = disciplina_tb.select()
           conn = self.db.connect()
           res = conn.execute(insert_command)
         
        except:

           res = False

        return res

    def obterMatricula(self, disciplina_selecionada, matricula_tb):
    
        try:

           insert_command = matricula_tb.select().where(matricula_tb.c.disciplina == disciplina_selecionada)
           conn = self.db.connect()
           res = conn.execute(insert_command)
         
        except:

           res = False

        return res

    def obterRequisicao(self, coordenador, requisicao_tb):
    
        try:

           insert_command = requisicao_tb.select().where(requisicao_tb.c.coordenador == coordenador)
           conn = self.db.connect()
           res = conn.execute(insert_command)
         
        except:

           res = False

        return res

    def obterTodasRequisicao(self, requisicao_tb):
    
        try:

           insert_command = requisicao_tb.select()
           conn = self.db.connect()
           res = conn.execute(insert_command)
         
        except:
           
           res = False

        return res

    def deletarRequisicao(self, id_requisicao, requisicao_tb):
    
        try:

           insert_command = requisicao_tb.delete().where(requisicao_tb.c.id_requisicao == id_requisicao)
           conn = self.db.connect()
           res = conn.execute(insert_command)
         
        except:

           res = False

        return res

    def obterMatriculaAluno(self, matricula, matricula_tb):
    
        try:

           insert_command = matricula_tb.select().where(matricula_tb.c.aluno == matricula)
           conn = self.db.connect()
           res = conn.execute(insert_command)
         
        except:

           res = False

        return res

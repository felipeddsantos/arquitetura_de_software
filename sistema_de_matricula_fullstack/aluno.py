'''

Arquitetura de Software - Sistema de Matrícula FullStack (Classe Aluno)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

class Aluno:

    nome = None
    sobrenome = None
    matricula = None 
    email = None
    senha = None
    nascimento = None
    telefone = None
    curso = None

    def __init__(self, nome, sobrenome, matricula, email, senha, nascimento, telefone, curso):

        self.nome = nome
        self.sobrenome = sobrenome
        self.matricula = matricula
        self.email = email
        self.senha = senha
        self.nascimento = nascimento
        self.telefone = telefone
        self.curso = curso

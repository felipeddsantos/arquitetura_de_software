'''

Arquitetura de Software - Sistema de Matrícula FullStack (Classe Professor)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

class Professor:

    nome = None
    sobrenome = None
    registro = None
    email = None
    senha = None
    nascimento = None 
    telefone = None
    unidade = None

    def __init__(self, nome, sobrenome, registro, email, senha, nascimento, telefone, unidade):

        self.nome = nome
        self.sobrenome = sobrenome
        self.registro = registro
        self.email = email
        self.senha = senha
        self.nascimento = nascimento
        self.telefone = telefone
        self.unidade = unidade

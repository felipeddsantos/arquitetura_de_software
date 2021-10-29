'''

Arquitetura de Software - Sistema de Matrícula (Classe Disciplina)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

class Disciplina:

    nome = None
    codigo = None
    horario = None
    unidade = None
    registro_professor = None
    registro_coordenador = None

    def __init__(self, nome, codigo, horario, unidade, registro_professor, registro_coordenador):

        self.nome = nome
        self.codigo = codigo
        self.horario = horario
        self.unidade = unidade
        self.registro_professor = registro_professor
        self.registro_coordenador = registro_coordenador

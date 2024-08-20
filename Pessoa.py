#CLASSE ENDERECO
from datetime import date


class Endereco:
    def __init__(self, logradouro="", numero="", endereco_Comercial=False):
        # Inicializar os nossos atributos com valores padrao
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_Comercial = endereco_Comercial#CLASSE PESSOA

class Pessoa:
    def __init__(self, nome="", rendimento=0.0, endereco=None) :
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco

    def calcular_imposto(self, rendimento):
        return rendimento

#CLASSE PESSOA FISICA
    #Inicializar os atributos que foram herdados e os proprios atributos da classe
class PessoaFisica(Pessoa):
    def __init__ (self, nome="", rendimento=0.0, endereco=None, cpf="", dataNascimento=None):
        if endereco is None:
            # Se nenhum endereco for fornecido, cria um objeto de endereco padrao
            endereco = Endereco()

        if dataNascimento is None:
            dataNascimento = date.today()

            super().__init__(nome, rendimento, endereco) 
            #Chama o construtor da superclasse Pessoa para inicializar os atributos herdados


        #Atributos da propria classe
        self.cpf = cpf
        self.dataNascimento = dataNascimento

    def calcular_imposto(self, rendimento: float) -> float:
        # Sem imposto para rendimento entre 1500 e 3500
        if rendimento <= 1500:
            return 0
        #2% de imposto para rendimento entre 1500 e 3500
        elif 1500 < rendimento <= 3500:
            return(rendimento / 100) * 2
        #3.5% de imposto para rendimentos entre 3500 e 6000
        elif 3000 < rendimento <= 6000:
            return (rendimento/ 100) * 3.5
        #5% de impostos para rendimentos acima de 6000
        else:
            return rendimento * 5

#CLASSE PESSOA JURIDICA

class PessoaJuridica(Pessoa):
    pass

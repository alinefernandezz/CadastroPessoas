# 1 - Pessoa Fisica / 2 - Pessoa Juridica /3 - Sair
# 1 - Cadastrar Pessoa Fisica / 2- Listar Pessoa Física / 3 - Sair
# 1 - Cadastrar Pessoa Juridica / 2 - Listar Pessoa Juridica / 3 - Sair

from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica


def main():
    lista_pf = []
    while True:
        opcao = int(input('Escolha uma opcao: 1 - Pessoa Física / 2 - Pessoa Jurídica / 0 - Sair'))

        if opcao == 1:
            while True:
                opcao_pf = int(input('Escolha uma opcao: 1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 3 - Voltar ao menu anterior'))

                #1 Cadastrar uma Pessoa Fisica
                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input('Digite o nome da pessoa física: ')
                    novapf.cpf = input('Digite o CPF: ')
                    novapf.rendimento = float(input('Digite o rendimento mensal (Digite somente números): '))
                    

                    data_nascimento = input('Digite a data de Nascimento (dd/MM/aaaa): ') #Solicita a data de nascimento
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365 #Calcula idade da pessoa

                    if idade > 17:
                        print('A pessoa tem mais de 18 anos')
                    else:
                        print('A pessoa tem menos de 18 anos. Retorne ao menu...')
                        continue #Retornar ao inicio do loop

                    #CADASTRO DE ENDERECO
                    novo_end_pf.logradouro = input('Digite o logradouro: ')
                    novo_end_pf.numero = input('Digite o número: ')
                    end_comercial = input ('Este endereco é comercial: S/N: ') #Solicitar se o endereco é comercial
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == 'S' 

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)



                    print('Cadastro realizado com sucesso!!')
                #LISTAR PESSOA FISICA   
                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f'Nome: {cada_pf.nome}')
                            print(f'CPF: {cada_pf.cpf}')
                            print(f'Endereco: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}')
                            print(f'Data Nascimento: {cada_pf.dataNascimento.strftime('%d/%m/%Y')}')
                            print(f'Imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}')
                            print('Digite 0 para sair')

                            input()
                    else:
                        print('Lista Vazia')
            
                #SAIA DO MENU ATUAL
                elif opcao_pf == 0:
                    print('Voltando ao menu anterior')
                    break

                else:
                    print('Opcao invalida, por favor digite uma das opcoes indicadas: ')

        elif opcao == 2:
            print('Funcionalidade para pessoa jurídica nao implementadas')
            break
    
        elif opcao == 0:
            print('Obrigada por utilizar o nosso sistema! Valeu!')
            break

        else:
            print('Opcao invalida, por favor digite uma das opcoes válidas')
    
if __name__ == '__main__':
    main() #Chama funcao principal

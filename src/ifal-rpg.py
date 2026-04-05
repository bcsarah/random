import os
from time import sleep

#  GLOBALS   #
dia_semana = 1
dia = 4
mês = 3


#  FUNÇÕES  #
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def title(título, descrição, opções):
    while True:
        clear()
        print(f'#  {título}  #')
        print(f'  {descrição}\n')
        for index, item in enumerate(opções):
            print(f'{index + 1} - {item}')

        try:
            uinput = int(input('>> '))
            if 1 <= uinput <= len(opções):
                return uinput
            else:
                print('\nDigite uma instância correta.')
                sleep(2.5)
        except ValueError:
            print('\nDigite uma instância correta. Digite um número inteiro.')
            sleep(2.5)

def dia_da_semana():
    match dia_semana:
        case 1:
            return 'Segunda'
        case 2:
            return 'Terça'
        case 3:
            return 'Quarta'
        case 4:
            return 'Quinta'
        case 5:
            return 'Sexta'
        case 6:
            return 'Sábado'
        case 7:
            return 'Domingo'    

# IFAL RPG #
def menu():
    menu = title('IFAL RPG', 'Bem-vindo ao RPG do IFAL!', ['Jogar', 'Sair'])
    match menu:
        case 1:
            casa()
        case 2:
            exit()

def casa():
    energia = 100
    felicidade = 5
    tempo = 30
    estado = 'Com fome'

    título_energia   = f'Enegia: {energia}/100'
    título_feliciade = f'Felicidade: {felicidade}/10'
    junção = f'{dia_da_semana()}, {dia}/{mês}\n\n  {título_energia}\n  {título_feliciade}\n  Estado: {estado}\n\n  Você precisa ir para escola em {tempo} minutos.\n'
    while True:
        casa = title('CASA', junção, ['Comer        (-5 minutos)', 'Banho        (-20 minutos)', 'Fazer lanche (-10 minutos)', 'Ir pegar o ônibus'])
        match casa:
            case 1:
                tempo -= 20
                if tempo <= 0:
                    print('Você não tem tempo para fazer isso.')
                    tempo 
                estado = 'Normal'
                energia += 20
                if energia >= 100:
                    energia = 100
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass

def escola():
    pass

# MAIN #
def main():
    menu()
    casa()
    escola()

main()
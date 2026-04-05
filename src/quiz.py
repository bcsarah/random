from os import system
from random import randint

golias = 0
nessa = 0
bongo = 0

# FUNÇÕES
def perguntar(prompt, perguntas):
    global golias, nessa, bongo

    while True:
        system('cls')
        print(f"#  QUIZZ FODA DO MEU AMIGÃOZÃO  #")
        i = 1
        for pergunta in perguntas:
            print(f"{i} - {pergunta}")
            i += 1
    
        print()
        print(prompt)
        uinput = int(input('>> '))
        if uinput >= 1 and uinput <= len(perguntas):
            break
        else:
            pass

    if uinput == 1:
        golias += 1
    elif uinput == 2:
        nessa += 1
    elif uinput == 3:
        bongo += 1
        
# MAIN  
def main():
    perguntar('Você é mais oq?', ['Besta', 'Delicada', 'Aventureiro'])
    perguntar('Qual sua cor preferida??', ['Azul', 'Rosa', 'Verde'])
    perguntar('Qual o seu maior medo?', ['Escuro', 'Ser deixada de lado pelos outros', 'Trovões'])
    if golias > nessa and golias > bongo:
        system('cls')
        print('VC É O GOLIAS!!11!11!1')
        input()
    elif nessa > golias and nessa > bongo:
        system('cls')
        print('VC É A NESSA!!11!11!1')
        input()
    elif bongo > golias and bongo > nessa:
        system('cls')
        print('VC É O BONGO!!11!11!1')
        input()
    elif golias == nessa == bongo:
        escolha = randint(1, 3)
        if escolha == 1:
            system('cls')
            print('VC É O GOLIAS!!11!11!1')
            input()
        elif escolha == 2:
            system('cls')
            print('VC É A NESSA!!11!11!1')
            input()
        elif escolha == 3:
            system('cls')
            print('VC É O BONGO!!11!11!1')
            input()
        
main()
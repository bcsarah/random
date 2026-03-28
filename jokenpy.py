from random import choice
from time import sleep
import os

pontuação = 0
sua_escolha = None
bot_escolha = None

# -- Funções --
def seu_turno():
    global sua_escolha
    
    while True:
        os.system('cls')
        print('JoKenPy')
        print(f'Pontuação: {pontuação}\n')
        print('Pedra\nPapel\nTesoura')
        
        sua_escolha = input('-- ')
        sua_escolha = sua_escolha.capitalize()
        if sua_escolha in ('Pedra', 'Papel', 'Tesoura'):
            break
        else:
            print('\nEscolha um corretamente.')
            print('Voltando para a seleção...')
            sleep(2.5)
            
    print(f'\nCerto! Você escolheu {sua_escolha}!')
    print('...\n')
    sleep(2.5)
    
def bot_turno():
    global bot_escolha
    
    bot_escolha = choice(['Pedra', 'Papel', 'Tesoura'])
    print(f'Seu adversário escolheu {bot_escolha}!')
    print('...\n')
    sleep(2.5)
    
def verifica_se_ganhou():
    global pontuação
    
    if sua_escolha == bot_escolha:
        print('Empate!')
        print('Você não recebeu pontos!')
    elif (sua_escolha == 'Pedra' and bot_escolha == 'Tesoura') or (sua_escolha == 'Papel' and bot_escolha == 'Pedra') or (sua_escolha == 'Tesoura' and bot_escolha == 'Papel'):
        print('Você venceu essa rodada!')
        print('Você recebeu 1 ponto!')
        pontuação += 1
    elif (sua_escolha == 'Pedra' and bot_escolha == 'Papel') or (sua_escolha == 'Papel' and bot_escolha == 'Tesoura') or (sua_escolha == 'Tesoura' and bot_escolha == 'Pedra'):
        print('Você perdeu essa rodada!')
        print('Você perdeu 1 ponto!')
        pontuação -= 1
    print('...\n')
    sleep(2.5)

def jogo():
    while True:
        seu_turno()
        bot_turno()
        verifica_se_ganhou()

# -- Main --
def main():
    jogo()
    
main()
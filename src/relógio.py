from time import sleep
from datetime import datetime
from os import system

def main():
    while True:
        agora = datetime.now()
        dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        semana = datetime.today().weekday()

        system('cls')
        print(agora.strftime(f'\n{dias[semana]} | %H:%M:%S {'PM' if datetime.today().hour >= 12 else 'AM'} | %d/%m/%Y'))
        sleep(0.75)

main()
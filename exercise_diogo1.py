from os import system


# Funções
def calcular_média(notas:list) -> float:
    return sum(notas) / len(notas)

def validar_nome(texto:str) -> str:
    while True:
        nome = input(texto).strip().capitalize()
        if nome == '':
            print('\nDigite uma entrada válida. Digite um nome.')
        else:
            return nome

def validar_nota(texto:str) -> float:
    while True:
        try:
            nota = float(input(texto).replace(',', '.'))
            if nota <= 10:
                return nota
            else:
                print('\nDigite uma entrada válida. Digite um número de 1 à 10.')
        except ValueError:
            print('\nDigite uma entrada válida. Digite um número de 1 à 10.')

def verificar_aprovação(aluno:str, média:float) -> None:
    print(f'\nA média do aluno foi {média}.')
    if média >= 7:
        print(f'{aluno} está Aprovado(a)!')
    elif média >= 4:
        print(f'{aluno} está em Recuperação!')
    else:
        print(f'{aluno} está Reprovado(a)!')


# Main
def main():
    system('clear')
    print('#  Análise de Alunos  #\n')
    aluno = validar_nome('Nome: ')
    nota1 = validar_nota('Nota 1° Bim.: ')
    nota2 = validar_nota('Nota 2° Bim.: ')
    nota3 = validar_nota('Nota 3° Bim.: ')
    nota4 = validar_nota('Nota 4° Bim.: ')

    notas = [nota1, nota2, nota3, nota4]
    média = calcular_média(notas)
    verificar_aprovação(aluno, média)


main()

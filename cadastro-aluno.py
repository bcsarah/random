def média(notas: list) -> float:
    return sum(notas) / len(notas)

alunos = {
    'Nome': {
        '1º Bimestre': float,
        '2º Bimestre': float,
        '3º Bimestre': float,
        '4º Bimestre': float,
        'Desempenho': str
    }
}

def desempenho_aluno():
    pass

def add_aluno(nome, n1, n2, n3, n4):
    alunos[nome] = {
            '1° Bimestre': n1,
            '2° Bimestre': n2,
            '3° Bimestre': n3,
            '4° Bimestre': n4,
            'Desempenho': desempenho_aluno()
    }

def main():
    while True:
        print('Cadastro de Aluno')
        nome =  input('Nome:  ')
        notas = input('Notas: ')
        try:
            n1, n2, n3, n4 = notas.split(', ')
        except:
            input('digite 4 poha')
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        n4 = int(n4)
        print(f'{nome} - {n1}, {n2}, {n3}, {n4} ({média([n1, n2, n3, n4])})')
        input()

main()
#!/usr/bin/python3
# Conceitos   Notas
# A          De 10,0 a 9,1
# A-         De 9,0 a 8,1
# B          De 8,0 a 7,1
# B-         De 7,0 a 6,1
# C          De 6,0 a 5,1
# C-         De 5,0 a 4,1
# D          De 4,0 a 3,1
# D-         De 3,0 a 2,1
# E          De 2,0 a 1,1
# E-         De 1,0 a -1

# Para notas maiores que 10 e menores que 0 será impresso "Nota inválida"


def calculo_nota(nota):
    try:
        if nota > 10:
            return 'Nota inválida'
        elif nota == 10:
            return 'A+'
        elif nota >= 9.1:
            return 'A'
        elif nota >= 8.1:
            return 'A-'
        elif nota >= 7.1:
            return 'B'
        elif nota >= 6.1:
            return 'B-'
        elif nota >= 5.1:
            return 'C'
        elif nota >= 4.1:
            return 'C-'
        elif nota >= 3.1:
            return 'D'
        elif nota >= 2.1:
            return 'D-'
        elif nota >= 1.1:
            return 'E'
        elif nota >= 1:
            return 'E-'
        else:
            return 'Nota inválida'
    except:
        return 'Nota inválida'


if __name__ == '__main__':
    nota = float(input("Informe a nota: "))
    print(calculo_nota(nota))

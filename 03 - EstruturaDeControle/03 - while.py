from random import randint

numero_informado = -1
numero = randint(0, 9)

while numero_informado != numero:
    try:
        numero_informado = int(input('Informe um numero: '))
        if numero_informado != numero:
            print('Numero errado, tente novamente')
        else:
            print('Numero correto')
    except:
        print(f'Numero correto {numero_informado}')


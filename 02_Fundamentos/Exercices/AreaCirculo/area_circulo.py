import math


# v1 | calculo simples
pi = math.pi
raio = 15.3
circulo = pi * raio ** 2
print('Área do círculo', round(circulo, 2), 'v3')


# v2 | calculo simples com o usuario informando o valor
raio2 = int(input('Informe o raio: '))
calculo = round(raio2 * pi ** 2, 2)
print('Área do círculo', calculo, 'v2')

# v3 | clculo simples só que utilizando def


def calculo_circulo(raio):
    pi = math.pi
    calculo = round(raio * pi ** 2)
    print('Área do círculo', calculo, 'v3')


calculo_circulo(13)

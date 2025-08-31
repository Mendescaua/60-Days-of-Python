# Utilizando o range

def faixa_etaria(idade):
    try:
        if 0 <= idade < 18:
            return 'Menor de idade'
        elif idade in range(18, 65):
            return 'Adulto'
        elif idade in range(65, 100):
            return 'Melhor idade'
        elif idade >= 100:
            return 'Centenário'
        else:
            return 'Idade inválida'
    except:
        return 'Idade inválida'
    

if __name__ == '__main__':
    for idade in (-1, 0, 17, 18, 'B', 65, 99, 100, 101):
        print(f'{idade} : {faixa_etaria(idade)}')
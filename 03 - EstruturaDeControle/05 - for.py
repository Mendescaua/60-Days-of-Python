palavra = 'paralelepípedo'

for letra in palavra:
    print(letra)

nomes = ['Caua', 'Micaela', 'Scooby\n']
for nome in nomes:
    print(nome)

frutas = ('Banana', 'Pera', 'Laranja\n')
for fruta in frutas:
    print(fruta)

pessoas = {'Nome': 'Caua', 'Idade': 19, 'Cursos': ['Py', 'Dart', 'EN']}

#percorre as chaves
for chaves in pessoas:
    print(chaves)

#percorre os valores
for values in pessoas.values():
    print(values)

#percorre as chaves e os valores
for chaves, values in pessoas.items():
    print(chaves, '=', values)
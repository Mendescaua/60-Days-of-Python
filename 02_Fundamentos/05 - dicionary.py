pessoa = {'Name': 'Caua', 'Age': 19, 'cursos': ['Python', 'Inglês', 'Flutter']}


print(pessoa.keys())  # Chaves do dicionário
print(pessoa.values())  # Valores do dicionário

print(pessoa['Name'])  # Acessar um valor do dicionário
print(pessoa['cursos'][1])  # Acessar um valor do dicionário com lista
pessoa.update({'Name': 'Caua Mendes'})  # Atualiza um valor
pessoa['cursos'].remove('Inglês')  # remove um dado da lista
print(f"pessoas: {pessoa}")

# Programa para adicionar pessoas a um dicionário
pessoa2 = [{'Name': 'Pedro', 'Age': 23,
            'cursos': ['Python', 'Inglês', 'Flutter']}]

name = input("Digite o nome do pessoa: ")

pessoa2.append({'Name': name, 'Age': 36, 'cursos': ['Adm', 'office', 'Rh']})
print(f"{name} foi adicionado com sucesso!")
print("Lista de pessoas atualizada:")
print(pessoa2)

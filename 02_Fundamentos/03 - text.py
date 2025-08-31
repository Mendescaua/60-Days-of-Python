nome = "Caua Mendes"
print(nome)  # Imprime o nome
print(nome[0])  # Imprime a primeira letra do nome


faturamento = 1000
custo = 700
lucro = faturamento - custo
# Format
print(f"O lucro da empresa foi de {lucro}, com um custo de: {custo}, e um faturamento de: {faturamento}")
print("O lucro da empresa foi de {}, com um custo de: {}, e um faturamento de: {}".format(
    lucro, custo, faturamento))


client_email = "exemplo@gmail.com"
print(client_email.upper())  # Maiscula
print(client_email.lower())  # Minuscula
print(client_email.title())  # Primeira letra Maiuscula
print(client_email.split("@"))  # Dividir por @
print(client_email.find("@"))  # Posição do @
print(client_email.replace("gmail", "outlook"))  # Substituir
print(len(client_email))  # Tamanho da string


email = "caua@gmail"
print(email[4:])  # Acessar parte da string após o índice 4

# pega o primeiro nome
primeiro_nome = "Caua Mendes"
posicao_espaco = primeiro_nome.find(" ") + 1
print(primeiro_nome[:posicao_espaco])

# pega o sobrenome
sobrenome = "Caua Mendes"
posicao_espaco = sobrenome.find(" ") + 1
print(sobrenome[posicao_espaco:])

# inverte a string
textos = "1234567890"
print(textos[::-1])

# Separando strings
api = "caua;pedro;joao;maria;luan;ana;luiza;marcos"
print(api.split(";"))  # Divide a string em uma lista de nomes

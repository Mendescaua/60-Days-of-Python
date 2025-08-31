# lists

vendas = [10, 42, 3, 54, 5, 26, 447, 8, 90, 10]
nomes = ["Caua", "Mendes", "Joao", "Maria", "Luan", "Ana", "Luiza", "Marcos"]
# soma de vendas
total_venda = sum(vendas)
print(f"Vendas: {total_venda}")

# ordenações
vendas.sort()  # Ordenar a lista
nomes.sort()  # Ordenar a lista de nomes
print(f"Vendas ordenadas: {vendas}")
print(f"Nomes ordenados: {nomes}")


# index do elemento
print(nomes.index("Caua"))  # Posição do elemento Ana

# tamanho da lista
total_venda = len(vendas)
print(f"Tamanho da lista: {total_venda}")

# maior e menor
print(max(vendas))
print(min(vendas))

# Pegar posição
print(vendas[0])  # Primeira posição
print(vendas[-1])  # Ultima posição
print(vendas[4])  # Quarta posição

# adicionar e remover
produtos = ["Notebook", "Smartphone", "Mouse", "Teclado"]
produtos.append("Monitor")
print(produtos)
produtos.remove("Smartphone")
print(produtos)

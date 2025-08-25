import os
restaurants = [{'name': 'Mcdonalds', 'category': 'Fast-food', 'active': True}, {'name': 'Habibs', 'category': 'Arabe', 'active': True}, {'name': 'Bob\'s', 'category': 'Ice cream', 'active': False}]


def header():
    print("𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n")
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")


def invalid_option():
    print('Opção inválida, informe uma opção de 1 a 4!')
    input('Digite uma tecla para voltar ao menu: ')
    main()


def exit():
    title("Finalizando app...")


def menu():
    input('Digite uma tecla para voltar ao menu principal: ')
    main()


def title(title):
    os.system('cls')
    print(f'{title}\n')


def register():
    title('Cadastrar restaurante')
    name = input('Digite o nome do restaurante: ')
    category = input('Digite a categoria do restaurante: ')
    restaurants.append({'name': name, 'category': category, 'active': True})
    print(f'\nRestaurante {name} cadastrado com sucesso!')
    menu()


def list_restaurant():
    title('Lista de restaurantes')
    print('NOME'.ljust(20), '| CATEGORIA'.ljust(20), '| ATIVO')
    for i in restaurants:
        active = 'Ativado' if i['active'] else 'Desativado'
        print(f'{i['name'].ljust(20)} | {i['category'].ljust(18)} | {active}')
    menu()


def active_restaurant():
    title('Ativar restaurante\n')
    name = input("Escolha o restaurante que deseja alterar o estado: ")
    restaurant_finded = False
    for i in restaurants:
      if name == i['name']:
          restaurant_finded = True
          i['active'] = not i['active']
          print(f'O restaurante {name} foi ativado com sucesso' if i['active'] else f'O restaurante {name} foi desativado com sucesso')
    if not restaurant_finded:
        print(f'O restaurante {name} não foi encontrado!')
        menu()
    menu()


def options():
    try:
        option = int(input('Escolha uma opção: '))
        if option == 1:
            register()
        elif option == 2:
            list_restaurant()
        elif option == 3:
            active_restaurant()
        elif option == 4:
            exit()
        else:
            invalid_option()
    except:
        invalid_option()


def main():
    os.system('cls')
    header()
    options()


if __name__ == '__main__':
    main()
from restaurant import Restaurant

def show_restaurants():
  res1 = Restaurant('Pizzaria Uirapuru', 'Pizza')
  res1.active_restaurant()
  Restaurant.restaurant_list()


def main():
  show_restaurants()


if __name__ == '__main__':
  main()
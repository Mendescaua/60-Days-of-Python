class Restaurant:
  restaurants = []
  def __init__(self, name, category):
    self._name = name.title()
    self._category = category.upper()
    self._active = False
    Restaurant.restaurants.append(self)

  def __str__(self):
    return f'Restaurante: {self._name} | Categoria: {self._category} | Ativo: {self._active}'
  
  def restaurant_list():
    for i in Restaurant.restaurants:
      print(f'{i._name} | {i._category} | {i._active}')

  @property
  def active(self):
    return 'Ativado' if self._active else "Desativado"
  
  def active_restaurant(self):
    self._active = not self._active
    

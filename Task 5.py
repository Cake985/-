class Soda:
    def __init__(self, drink, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
            self.drink = drink
        else:
            self.drink = drink
            self.ingredient = None



    def show_my_drink(self):
        if self.ingredient:
            print('Газировка и ' + self.ingredient)
        else:
            print('Обычная газировка')

drink1 = Soda("Соль")
drink2 = Soda('малина')
drink3 = Soda(5)

drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()

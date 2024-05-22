class Food:
    def __init__(self,name,price,food_type):
        self.name = name
        self.price = price
        self.type = type



class Burger(Food):
    def __init__(self, name, price,food_type,mid_layer,size):
        super().__init__(name, price, food_type)
        self.mid_layer = mid_layer
        self.size = size


class Pizza(Food):
    def __init__(self, name, price, food_type,size,catagory):
        super().__init__(name, price, food_type)
        self.size = size
        self.catagory = catagory



class Drinks(Food):
    def __init__(self, name, price, food_type,amount,is_Hot):
        super().__init__(name, price, food_type)
        self.amount = amount
        self.is_Hot = is_Hot


class Menu:
    def __init__(self) -> None:
        self.burgers = []
        self.pizzas = []
        self.drinks = []


    def show_menu(self):
        print('Burger:')
        for burger in self.burgers:
            print(f"Name:{burger.name},Price:{burger.price}, Size:{burger.size},Layer:{burger.mid_layer}")


        print('Pizzas:')
        for pizza in self.pizzas:
            print(f"Name:{pizza.name},Price:{pizza.price}, Size:{pizza.size},Catagory:{pizza.catagory}")



        print('Drinks:')
        for drinks in self.drinks:
            print(f"Name:{drinks.name},Price:{drinks.price}, Size:{drinks.amount},Hot:{drinks.is_Hot}")

    


    def add_menu_item(self,item,item_type):
        if item_type == 'burger':
            self.burgers.append(item)

        elif item_type == 'pizza':
            self.pizzas.append(item)

        elif item_type == 'drinks':
            self.drinks.append(item)

        else:
            print("You entered wrong type.Please enter pizza , burger, drinks")
    
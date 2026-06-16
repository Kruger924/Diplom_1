from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

BUN = {'name': 'Булка', 'price': 50.0}
INGREDIENT = {'ingredient_type': 'Начинка', 'name': 'Котлетка', 'price': 100.0}

BUNS_DATA = [('bun', 100), ('bagel', 200), ('roll', 300)]
INGREDIENTS_DATA = [
    (INGREDIENT_TYPE_SAUCE, 'ketchup', 100),
    (INGREDIENT_TYPE_SAUCE, 'barbecue', 200),
    (INGREDIENT_TYPE_SAUCE, 'tabasco', 300),
    (INGREDIENT_TYPE_FILLING, 'hum', 100),
    (INGREDIENT_TYPE_FILLING, 'fish', 200),
    (INGREDIENT_TYPE_FILLING, 'dolphin', 300)
]

STR_BUN = '(==== {bun_name} ====)'
STR_INGREDIENT = '= {ingredient_type} {ingredient_name} ='
STR_PRICE = '\nPrice: {price}'
RECEIPT_TEMPLATE = '\n'.join([STR_BUN, STR_INGREDIENT, STR_BUN, STR_PRICE])
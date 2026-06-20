import praktikum.ingredient_types


from unittest.mock import Mock
from praktikum.burger import Burger, Bun
from praktikum.database import Database


class TestBurger:

    """ Тест на установку булок """
    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Test_bun', 100.0)
        burger.set_buns(bun)
        assert burger.bun == bun

    """ Тест на добавление ингредиента """
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Test_bun'
        mock_ingredient.get_price.return_value = 5.0
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_price() == 5.0
        assert burger.ingredients[0].get_name() == 'Test_bun'
        assert burger.ingredients[0].get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_FILLING

    """ Тест на удаление ингредиента """
    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    """ Тест на получение цены бургера"""
    def test_get_price(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[1])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[4])
        assert burger.get_price() == 700.0

    """ Тест на получение чека """
    def test_get_receipt(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[1])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[4])
        expected_receipt = "(==== white bun ====)\n"\
                           "= sauce hot sauce =\n"\
                           "= filling dinosaur =\n"\
                           "(==== white bun ====)\n\n"\
                           "Price: 700"
        assert expected_receipt == burger.get_receipt()
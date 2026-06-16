from unittest.mock import Mock, patch

import pytest

from data import BUN, BUNS_DATA, INGREDIENT, INGREDIENT_DATA
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient

@pytest.fixture(scope='session')
def mock():
    return Mock()

@pytest.fixture(scope='session')
def mock_bun(mock):
    '''Мок для создания класса Bun'''
    mock.configure_mock(**BUN)
    mock.get_name.return_value = mock.name
    mock.get_price.return_value = mock.price
    return mock

@pytest.fixture(scope='session')
def mock_ingredient(mock):
    '''Мок для создания класса Ingredient'''
    mock.configure_mock(**INGREDIENT)
    mock.get_name.return_value = mock.name
    mock.get_price.return_value = mock.price
    mock.get_type.return_value = mock.type
    return mock

@pytest.fixture(scope='session')
def mock_buns_db(mock):
    '''Мок для создания набора булок для формирования базы данных'''
    buns = []
    for name, price in BUNS_DATA:
        mock = Mock()
        mock.configure_mock(name=name, price=price)
        mock.get_name.return_value = mock.name
        mock.get_price.return_value = mock.price
        buns.append(mock)
    return buns

@pytest.fixture(scope='session')
def mock_ingredients_db():
    '''Мок для создания набора ингредиентов для формирования базы данных'''
    ingredients = []
    for _type, name, price in INGREDIENT_DATA:
        mock = Mock()
        mock.configure_mock(type=_type, name=name, price=price)
        mock.get_type.return_value = mock.type
        mock.get_name.return_value = mock.name
        mock.get_price.return_value = mock.price
        ingredients.append(mock)
    return ingredients

@pytest.fixture(scope='session')
def test_bun():
    '''Мок для создания объекта класса Bun'''
    return Bun(**BUN)

@pytest.fixture(scope='session')
def test_burger():
    '''Мок для создания объекта класса Burger'''
    return Burger()

@pytest.fixture(scope='session')
def test_ingredient():
    '''Мок для создания объекта класса Ingredient'''
    return Ingredient(**INGREDIENT)

@pytest.fixture(scope='session')
@patch('praktikum.database.Ingredient')
@patch('praktikum.database.Bun')
def test_database(
        mock_bun_init, mock_ingredient_init, mock_buns_db, mock_ingredients_db
   ):
    '''Мок для создания объекта класса Database'''
    mock_bun_init.side_effect = mock_buns_db
    mock_ingredient_init.side_effect = mock_ingredients_db
    return Database()
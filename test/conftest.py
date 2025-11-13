import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

# =========================
# Мок-фикстуры для тестов
# =========================

@pytest.fixture
def mock_bun():
    """
    Мок объекта булочки.
    Возвращает объект с методами get_name и get_price
    """
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100.0
    return bun

@pytest.fixture
def mock_ingredient_sauce():
    """
    Мок объекта соуса.
    Возвращает объект с методами get_type, get_name, get_price
    """
    ingredient = Mock()
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 50.0
    return ingredient

@pytest.fixture
def mock_ingredient_filling():
    """
    Мок объекта начинки.
    Возвращает объект с методами get_type, get_name, get_price
    """
    ingredient = Mock()
    ingredient.get_type.return_value = "FILLING"
    ingredient.get_name.return_value = "cutlet"
    ingredient.get_price.return_value = 80.0
    return ingredient

# =========================
# Фикстуры для состояния бургера
# =========================

@pytest.fixture
def empty_burger():
    """
    Создает новый пустой бургер
    """
    return Burger()

@pytest.fixture
def burger_with_bun(mock_bun):
    """
    Создает бургер с установленной булочкой
    """
    burger = Burger()
    burger.set_buns(mock_bun)
    return burger

@pytest.fixture
def burger_with_ingredients(mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    """
    Создает бургер с булочкой и несколькими ингредиентами
    """
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)
    return burger
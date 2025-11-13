from praktikum.burger import Burger


class TestBurger:
    """Набор тестов для класса Burger"""

    # === Тесты инициализации ===
    def test_burger_initialization(self):
        """
        Проверка: при создании бургер инициализируется с пустой булочкой и пустым списком ингредиентов
        """
        empty_burger = Burger()
        assert empty_burger.bun is None, "У нового бургера булочка должна быть None"
        assert empty_burger.ingredients == [], "У нового бургера список ингредиентов должен быть пустым"

    # === Установка булочки ===
    def test_set_buns(self, empty_burger, mock_bun):
        """
        Проверка: установка булочки в бургер через метод `set_buns`
        """
        empty_burger.set_buns(mock_bun)
        assert empty_burger.bun == mock_bun, "Булочка должна быть установлена правильно"

    # === Добавление ингредиентов ===
    def test_add_ingredient_to_empty_burger(self, empty_burger, mock_ingredient_sauce):
        """
        Проверка: добавление первого ингредиента в пустой бургер
        """
        empty_burger.add_ingredient(mock_ingredient_sauce)
        assert len(empty_burger.ingredients) == 1, "Должен быть добавлен один ингредиент"
        assert empty_burger.ingredients[0] == mock_ingredient_sauce, "Ингредиент в списке некорректен"

    def test_add_multiple_ingredients(self, burger_with_bun, mock_ingredient_sauce, mock_ingredient_filling):
        """
        Проверка: добавление нескольких ингредиентов
        """
        burger_with_bun.add_ingredient(mock_ingredient_sauce)
        burger_with_bun.add_ingredient(mock_ingredient_filling)
        assert len(burger_with_bun.ingredients) == 2, "Должно быть два добавленных ингредиента"
        assert burger_with_bun.ingredients[0] == mock_ingredient_sauce
        assert burger_with_bun.ingredients[1] == mock_ingredient_filling

    # === Удаление ингредиентов ===
    def test_remove_ingredient(self, burger_with_ingredients):
        """
        Проверка: удаление ингредиента по индексу
        """
        initial_count = len(burger_with_ingredients.ingredients)
        first_ingredient = burger_with_ingredients.ingredients[0]

        burger_with_ingredients.remove_ingredient(0)

        assert len(burger_with_ingredients.ingredients) == initial_count - 1, "Ингредиент не был удален"
        assert first_ingredient not in burger_with_ingredients.ingredients, "Удаленный ингредиет все ещё в списке"

    # === Тесты перемещения ингредиентов ===
    def test_move_ingredient(self, burger_with_ingredients):
        """
        Проверка: перемещение ингредиента внутри списка.
        """
        first_before = burger_with_ingredients.ingredients[0]
        second_before = burger_with_ingredients.ingredients[1]

        burger_with_ingredients.move_ingredient(0, 1)

        # После перемещения
        assert burger_with_ingredients.ingredients[0] == second_before, "Первый элемент не переместился правильно"
        assert burger_with_ingredients.ingredients[1] == first_before, "Второй элемент не переместился правильно"

    # === Расчет стоимости ===
    def test_get_price_with_ingredients(self, burger_with_ingredients, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        """
        Проверка: подсчет стоимости бургера с булочкой и ингредиентами
        """
        expected_price = (
            mock_bun.get_price() * 2 +  # цена булочки (обе половинки)
            mock_ingredient_sauce.get_price() +
            mock_ingredient_filling.get_price()
        )
        actual_price = burger_with_ingredients.get_price()

        assert actual_price == expected_price, "Некорректная подсчитанная цена бургера"

    # === Генерация чека ===
    def test_get_receipt_with_ingredients(self, burger_with_ingredients, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        """
        Проверка: корректность формирования текста чека
        """
        expected_price = mock_bun.get_price() * 2 + mock_ingredient_sauce.get_price() + mock_ingredient_filling.get_price()
        expected_receipt = (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"= {mock_ingredient_sauce.get_type().lower()} {mock_ingredient_sauce.get_name()} =\n"
            f"= {mock_ingredient_filling.get_type().lower()} {mock_ingredient_filling.get_name()} =\n"
            f"(==== {mock_bun.get_name()} ====)\n"
            f"\n"
            f"Price: {expected_price}"
        )

        actual_receipt = burger_with_ingredients.get_receipt()

        assert actual_receipt == expected_receipt, "Некорректный формат или содержание чека"
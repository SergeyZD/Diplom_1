import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_get_type(self):
        ingredient = Ingredient('Начинка', 'Говяжий метеорит (отбивная)', 3000)
        assert ingredient.get_type() == 'Начинка'

    def test_get_name(self):
        ingredient = Ingredient('Начинка', 'Говяжий метеорит (отбивная)', 3000)
        assert ingredient.get_name() == 'Говяжий метеорит (отбивная)'

    def test_get_price(self):
        ingredient = Ingredient('Начинка', 'Говяжий метеорит (отбивная)', 3000)
        assert ingredient.get_price() == 3000

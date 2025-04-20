import pytest
from praktikum.bun import Bun


class TestBun:

    def test_bun_creation(self):
        bun = Bun("Соус Spice-X", 90)
        assert bun.name == "Соус Spice-X"
        assert bun.price == 90

    def test_get_name(self):
        bun = Bun('Краторная булка N-200i', 1255)
        assert bun.get_name() == 'Краторная булка N-200i'

    def test_get_price(self):
        bun = Bun('Краторная булка N-200i', 1255)
        assert bun.get_price() == 1255

from praktikum.bun import Bun


class TestBun:

    """ Тест на получение наименования """
    def test_get_correct_name(self):
        bun = Bun('Краторная булка N-200i', 1255)
        assert bun.get_name() == 'Краторная булка N-200i'

    """ Тест на получение стоимости """
    def test_get_correct_price(self):
        bun = Bun('Краторная булка N-200i', 1255)
        assert bun.get_price() == 1255
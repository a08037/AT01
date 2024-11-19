import unittest
from main import modulo

class TestModulo(unittest.TestCase):

    def test_modulo_success(self):
        # Проверяем корректную работу функции с разными числами
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(20, 5), 0)
        self.assertEqual(modulo(7, 2), 1)

    def test_modulo_by_zero(self):
        # Проверяем, что при делении на ноль выбрасывается исключение ValueError
        with self.assertRaises(ValueError):
            modulo(10, 0)

if __name__ == '__main__':
    unittest.main()

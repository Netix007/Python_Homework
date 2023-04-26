import unittest
import homework1 as a


class TestCircle(unittest.TestCase):

    def test_circle_length(self):
        self.assertEqual(a.Circle(1).circle_length(), 6.283185307179586)

    def test_circle_square(self):
        self.assertEqual(a.Circle(1).circle_square(), 3.141592653589793)

    def test_radius_type_error(self):
        with self.assertRaisesRegex(TypeError, 'Радиус должен быть числом'):
            a.Circle('123')

    def test_radius_value_error(self):
        with self.assertRaisesRegex(ValueError, 'Значение радиуса должно быть положительное'):
            a.Circle(-100)

    def test_print_circle(self):
        self.assertEqual('Окружность с радиусом 1', a.Circle(1).__str__())


if __name__ == '__main__':
    unittest.main()

import pytest
import homework1 as a


def test_circle_length():
    assert a.Circle(1).circle_length() == 6.283185307179586


def test_circle_square():
    assert a.Circle(1).circle_square() == 3.141592653589793


def test_type_error():
    with pytest.raises(TypeError, match='Радиус должен быть числом'):
        a.Circle('1')


def test_value_error():
    with pytest.raises(ValueError, match='Значение радиуса должно быть положительное'):
        a.Circle(-100)


def test_str_circle():
    assert a.Circle(1).__str__() == 'Окружность с радиусом 1'


if __name__ == '__main__':
    pytest.main(['-v'])

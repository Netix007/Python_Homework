# Создайте декоратор с параметром. Параметр - целое число, количество запусков декорируемой функции.

def decorator(count: int):
    def decorator2(func):
        def wrapper(*args, **kwargs):
            res = 0
            for _ in range(count):
                res += func(*args, **kwargs)
            return res
        return wrapper
    return decorator2


@decorator(10)
def fun():
    return 1


if __name__ == '__main__':
    print(fun())

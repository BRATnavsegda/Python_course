# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

number = 13


def next_fibonacci(n: int):

    a, b = 0, 1

    while True:
        if a == n:
            n = b
            yield b
        a, b = b, a + b


fib = next_fibonacci(number)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

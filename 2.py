"""Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
   Начиная с 1 и 2, первые 10 элементов будут:
   1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
   Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
   """


def fibonacci():
    a, b = 1, 1
    while a < 4000000:
        yield a
        a, b = b, a + b


fib_list = list(fibonacci())
fib_list_even = []

for elem in fib_list:
    if elem % 2 == 0:
        fib_list_even.append(elem)

print(sum(fib_list_even))

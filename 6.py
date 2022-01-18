"""Сумма квадратов первых десяти натуральных чисел равна
       1**2 + 2**2 + ... + 10**2 = 385
   Квадрат суммы первых десяти натуральных чисел равен
       (1 + 2 + ... + 10)**2 = 552 = 3025
   Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел
   составляет 3025 − 385 = 2640.
   Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
   """

print(abs((sum([i for i in range(1, 101)]) ** 2) - sum([i ** 2 for i in range(1, 101)])))

# a = sum([i**2 for i in range(1, 101)])
# b = sum([i for i in range(1, 101)])**2
# print(abs(b-a))

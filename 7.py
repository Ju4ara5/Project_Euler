# переделать!!!
"""Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
   Очевидно, что 6-е простое число - 13.
   Какое число является 10001-м простым числом?
   """

from math import log

n = 10001
x = 1

if n > 1:
    cont = int((log(n) + log(log(n)) - 0.5) * n) + 2 * n * (n < 26)
    # print(cont)

    A = [True] * cont
    k = 1

    while x < n:
        k += 2
        if A[k]:
            for m in range(k * k, cont, 2 * k):
                A[m] = False
            x += 1

else:
    k = 2

# print (x)
print(k)

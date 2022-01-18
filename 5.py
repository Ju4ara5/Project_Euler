#  додетать!!!

"""2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
   Какое самое маленькое число делится нацело на все числа от 1 до 20?
   """
#  scm = smallest_common_multiple - наименьшее общее кратное
#  gcd = greatest_common_divisor - наибольший общий делитель
#  scm( a ,   b ) = a ⋅ b : (a, b)=a·b:gcd( a ,   b )

# import math
# print(math.gcd(28, 64))

# gcd:
try:
    from math import gcd
except ImportError:
    from fractions import gcd
from functools import reduce

print(reduce(gcd, [36, 12, 144, 18]))

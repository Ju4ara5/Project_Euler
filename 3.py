"""Простые делители числа 13195 - это 5, 7, 13 и 29.
   Каков самый большой делитель числа 600851475143, являющийся простым числом?
   """

number = 600851475143
simple_list = []
simple_num = 2

while number > 1:
    if number % simple_num == 0:
        simple_list.append(simple_num)
        number = number / simple_num
    else:
        simple_num += 1

print(max(simple_list))

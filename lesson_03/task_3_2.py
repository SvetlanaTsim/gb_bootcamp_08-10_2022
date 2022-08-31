# Реализуйте проверку ввода на число.
# Программа должна выводить “Correct”, если введено целое или вещественное число (в качестве разделителя
# должна использоваться одна точка).
# Во всех остальных случаях должно выводиться “Wrong”.
# Для выполнения задания необходимо изучить методы строк
# Практическое задание
# 5 3.4 3.4.1 1a a3 -123 -5.321
# Correct Correct Wrong Wrong Wrong Correct Correct

import re

#используем ТОЛЬКО методы строки и списка
def number_check(num):
    if num.isdigit():
        return 'Correct'
    num_list = list(num)
    if num_list[0].isdigit() or (num_list[0] == '-' and num_list[1].isdigit()):
        points = num_list.count('.')
        minus = num_list.count('-')
        if (points == 0 or points == 1) and (minus == 0 or (minus == 1 and num_list.index('-') == 0)):
            num_cp = num_list.copy()
            if points:
                num_cp.remove('.')
            if minus:
                num_cp.remove('-')
            for a in num_cp:
                if not a.isdigit():
                    return 'Wrong'
            return 'Correct'
        else:
            return 'Wrong'
    else:
        return 'Wrong'


#используем try except
def number_check_var2(num):
    if num.find('.'):
        try:
            float(num)
        except:
            return 'Wrong'
        else:
            return 'Correct'
    else:
        try:
            int(num)
        except:
            return 'Wrong'
        else:
            return 'Correct'


#используем try except проще
def number_check_var3(num):
    try:
        float(num)
    except:
        return 'Wrong'
    else:
        return 'Correct'


#используем регулярные выражения
def number_check_var4(num):
    RE_DIGIT = re.compile(r'^[-]?\d+[.]?\d*$')
    result = RE_DIGIT.match(num)
    if result:
        return 'Correct'
    return 'Wrong'

check_list = ['5', '3.4', '3.4.1', '1a', 'a3', '-123', '-5.321', 'aaa', '67.3', '-102.45', '102.-67']
for i in check_list:
    print(number_check(i))

print('-*-' * 20)

for i in check_list:
    print(number_check_var2(i))

print('-*-' * 20)

for i in check_list:
    print(number_check_var3(i))

print('-*-' * 20)

for i in check_list:
    print(number_check_var4(i))

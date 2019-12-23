#Задачи на циклы и оператор условия------
#----------------------------------------
'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

print('Goal 1')
i = 0
while i < 5:
    i += 1
    print('String', i, 'is 0')

print('')

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

print('Goal 2')
sum = 0
for i in range(10):
    answer = int(input('Напишите любую цифру: '))
    if answer == 5:
        sum += 1

print('Количество пятёрок равно', sum)
print('')

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

print('Goal 3')
sum = 0
for i in range(1,101):
    sum+=i
print(sum)
print('')

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

print('Goal 4')
multiply = 1
for i in range(1,11):
    multiply *= i

print(multiply)
print('')

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

print('Goal 5')
integer_number = 2129
# print(integer_number%10,integer_number//10)
while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10
print('')

'''
Задача 6
Найти сумму цифр числа.
'''

print('Goal 6')
integer_number = 123321
sum = 0
while integer_number>0:
    sum += integer_number%10
    integer_number = integer_number//10
print(sum)
print('')

'''
Задача 7
Найти произведение цифр числа.
'''

print('Goal 7')
integer_number = 25352
mult = 1
while integer_number>0:
    mult *= integer_number%10
    integer_number = integer_number//10
print(mult)
print('')

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''

print('Goal 8')
integer_number = 21341315
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
print('')


'''
Задача 9
Найти максимальную цифру в числе
'''

print('Goal 9')
integer_number = 217341315
temp = 0
while integer_number>0:
    if integer_number%10 >= temp:
        temp = integer_number%10
    integer_number = integer_number//10
print(temp)
print('')

'''
Задача 10
Найти количество цифр 5 в числе
'''

print('Goal 10')
integer_number = 21734131
temp = 0
while integer_number>0:
    if integer_number%10 == 5:
        temp += 1
    integer_number = integer_number//10
print(temp)
print('')
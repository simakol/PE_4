#! Розгалудження

# user_number = int(input("Введіть ціле число: "))

'''
if умова1:
    тіло іфу, якщо умова1 є істинною(True)
elif умова2:
    тіло еліфу, якщо умова1 є хибною(False), а умова2 є істинною(True). Таких еліфів може бути скільки завгодно
else:
    тіло елсе, якщо ні одна умова не виконалась(False)

'''

# if user_number > 0:
#     print("Ваше число є додатнім")
# elif user_number < 0:
#     print("Ваше число є відʼємним")
# else:
#     print("Ваша цифра 0. Вона не є доданьою і не є відʼємною.")

'''
якщо ти зробив уроки:
    то, іди гуляти
інакше, якщо ти помив посуд:
    то, можеш пограти в ігри
інашкше:
    прибери в квартирі

'''



'''
користувач вводить число і потрібно вивести повідомлення про те парне число чи ні
>> 5
>> Число 5 є непарним (odd)
>> 10
>> Число 10 є парним (even)
Ознака парності числа: ділиться на 2 без остачі
'''

# print(10 % 2) # 0 - парне
# print(11 % 2) # 1 - непарне
# print(0 % 2) # 0 - це не парна і не непарна цифра

# user_number = int(input("Введіть ціле число: "))

# if user_number == 0:
#     print("Ваша цифра 0. Ні парна, ні непарна.")
# elif user_number % 2 == 0:
#     print("Ваше число є парним.")
# else:
#     print("Ваше число не є парним.")


#! Логічні оператори

'''
- логічне І (and): повертає перший False зі списку, якщо не знайшло, повертає останній елемент
- логічне АБО (or): повертає перше True зі списку, якщо не знайшло, повертає останній елемент
- логічне НІ (not): змінює логічний тип на зворотній, якщо було True, то стане False і навпаки

'''
# print("hello" and True and 0 and 5) # 0
# print(-5 and "" and 0 and False) # ""
# print(-8 and " " and True and "0" and "False") # "False"

# print("" or 0 or "hello" or False) # "hello"
# print(False or None or "0" or 0 or 500) # "0"
# print(False or None or "" or 0 or not True) # False


'''
True: будь-яке число, крім 0(і додатнє і відʼємне і дробове), будь-яка строка з символами

False: 0, пуста строка(""), None
'''

# print(not False) # True
# print(not 0) # True
# print(not "") # True
# print(not " ") # False


# user_number = int(input("Введіть число в діапазоні від 0 до 100: "))

# if user_number >= 0 and user_number <= 100: 
#     print("Ваше число підходить!")
# else:
#     print("Ваше число не входить в наш діапазон")

'''
1. користувач вводить 3 числа з консолі і нам потрібно вивести найбільше число
>> 5
>> 9
>> 4
>> Число 9 найбільше
'''

print("Введіть три числа:")

a = int(input())
b = int(input())
c = int(input())

biggestNumber = a

if a > b and a > c:
    biggestNumber = a
elif b > a and b > c:
    biggestNumber = b
elif c > a and c > b:
    biggestNumber = c
else:
    print("Визначити неможливо. Всі числа рівні")

print("Найбільше число:", biggestNumber)


'''
ДЗ:


1. написати консольний калькулятор: користувач вводить 1 число, 2 число і знак операції(+, -, *, /) і йому повертається результат розрахунку
>> Введіть 1 число: 10
>> Введіть 2 число: 4
>> Введіть знак операції: *
>> Результат: 40

=================================================================================

2. Написати кофе машину
Користувач вносить кошти і вибирає напій (1 - Лате(25 грн), 2 - Капучино(50 грн), 3 - Чай (10 грн)). Програма повинна видати йому напій і повернути решту, якщо коштів не вистачає - сказати про це.

>> Внесіть кошти: 15
>> Виберіть напій (1 - Лате(25 грн), 2 - Капучино(50 грн), 3 - Чай (10 грн)): 3
>> Ось ваш чай, ваша решта - 5 грн

>> Внесіть кошти: 30
>> Виберіть напій (1 - Лате(25 грн), 2 - Капучино(50 грн), 3 - Чай (10 грн)): 2
>> На жаль, недостатнько коштів, заберіть решту.
'''
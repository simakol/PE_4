'''
цикл for запускається на якусь кількість ітерацій(ітерація це одне виконання циклу).
index - це змінна в яку зберігається значення того, що ми перебираємо.
в даному прикладі ми перебираємо діапазон цифр від 1 до 11(не включно, тобто, до 10) [1, 11)
і на кожній ітерації можемо писати будь-який код, який нам потрібно виконати 10 разів

range(start, end, step)
- start - звідки починаємо(включно)
- end - де закінчуємо (не включно)
- step - крок циклу (на скільки ми будемо додавати на кожній ітерації)
'''
# for index in range(1, 11, 4):
#     print(index)

'''
напишіть цикл, який виведе в консоль всі парні числа від 1 до 100 включно
'''

# for index in range(2, 101, 2):
#     print(index)

'''
- continue: це оператор, який може пропустити одну ітерацію і перейти на наступну
- break: це оператор, який може повністю зупинити виконання циклу

'''

# for index in range(1, 101):
#     if index % 5 == 0:
#         continue
#     print(index)

# for index in range(1, 101):
#     if index % 5 == 0:
#         break
#     print(index)

'''
else в циклі: спрацьовує тоді, коли в циклі не спрацював оператор break
'''
# print("Start")

# for index in range(1, 11):
#     if index == 3:
#         break
#     print(index)
# else:
#     print("В цьому циклі не спрацював оператор break")

# print("End")


'''
розшифруй повідомлення прибравши всі цифри. Для завдання використовуй цикл та функцію для перевірки символа на число (.isdigit() - повертає True, якщо значення є числом)
'''

# sentence = "5i 1l56o3v3e9 1p4yt6ho7n8" # i love python
# result = ""

# for char in sentence:
#     if not char.isdigit():
#         result += char

# print(result)

'''
користувач вводить слово і букву, яку він хоче знайти
якщо ця буква є у слові - сказати, що вона є, 
якщо ж букви у слові немає - сказати, що такої букви немає
Цю задачу можна зробити з використанням циклів та без циклу, спробуйте зробити двома способами
'''
# "HeLlO".lower() -> "hello"
# word = input("Введіть слово: ").lower()
# letter = input("Введіть букву, яку хочете знайти: ").lower()

# ! Цикл
# for char in word:
#     if char == letter:
#         print("Буква", letter, "є у слові", word)
#         break
# else:
#     print("Букви", letter, "у слові", word, "не існує")

# ! Без циклу

# if letter in word:
#     print("Буква", letter, "є у слові", word)
# else:
#     print("Букви", letter, "у слові", word, "не існує")

'''
1 варіант через цикл
    1. запитати у користувача слово і букву
    2. запускаємо цикл на перебір слова
    3. перевіряємо, якщо поточний символ слова рівний букві, яку ми шукаємо, то зупиняємо цикл і кажемо користувачу, що така буква є!
    4. інакше - виводимо, що такої букви немає

2 варіант без циклу
    1. запитати у користувача слово і букву
    2. відразу перевіряємо чи є буква у слові використовуючи оператор in
'''


'''
користувач вводить слово і букву. Програма повинна порахувати скільки таких букв є у слові.
Наприкдал, якщо я введу слово rabbit і буду шукати букву b, то програма покаже мені цифру 2, тому що у слову rabbit є 2 букви b
'''

# word = input("Введіть слово: ").lower()
# letter = input("Введіть букву, яку хочете підрахувати: ").lower()
# amount = 0

# for char in word:
#     if char == letter:
#         amount += 1

# if amount == 0:
#     print("Такої букви немає")
# else:
#     print("Буква зустрічається", amount, "раз(и)")
     

'''
ДЗ:
Виведіть в консоль перші 200 непарних чисел, які при цьому не є кратними 5 (тобто вони не діляться на 5)
1
3
7
9
11
13
17
19
21
...
'''
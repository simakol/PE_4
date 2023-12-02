import tkinter as tk # ми імпортуємо(підключаємо) бібліотеку текінтер, але називаємо її tk щоб менше писати слів
import random

def get_randon_int(min, max):
    return random.randint(min, max) # фукнція, яка генерує псевдовипадкове число в діапазоні від мінімального до максимального

def change_number():
  min = int(minValue.get())
  max = int(maxValue.get())
  if min > max:
    greeting["text"] = "Неправильні дані"
  else:
     greeting["text"] = get_randon_int(min, max)


window = tk.Tk() # це створення головного елементу інтерфейсу, а саме - вікна програми

window.title("Це заголовок моєї програми!") # створює заголовок вікна програми

window.geometry("400x200+150+50") # керування розміром і позицією нашого вікна. 400 це ширина, 200 - висота, 450 - це відступ зліва, а 300 - це відступ зверху

window.configure(bg="blue") # змінює колір фону вікна

greeting = tk.Label(text="Hello world!", bg="green", fg="black", font="Arial 50 bold") # це створення віджету для звичайного тексту

greeting.pack()  # це відображення віджета тексту у вікні

minValue = tk.StringVar() # це контейнер для збереженого тексту
minEntry = tk.Entry(textvariable=minValue) #поле для вводу інформації

maxValue = tk.StringVar() # це контейнер для збереженого тексту
maxEntry = tk.Entry(textvariable=maxValue)

minEntry.pack()
maxEntry.pack()

button = tk.Button(text="Click me", command=change_number, bg="black", fg="green", font="Arial 30 bold", bd=0, padx="10", pady="8")

button.pack()

window.resizable(0, 0) # це заборона на зміну розміру екрану користувачеві



window.mainloop() # це нескінченний цикл, який не дає нашому вікну закритись
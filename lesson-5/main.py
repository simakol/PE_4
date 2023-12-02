import tkinter as tk # ми імпортуємо(підключаємо) бібліотеку текінтер, але називаємо її tk щоб менше писати слів
import random

def get_randon_int(min, max):
    return random.randint(min, max) # фукнція, яка генерує псевдовипадкове число в діапазоні від мінімального до максимального

def print_msg():
    print("You clicked")
    greeting["text"] = "You already clicked!"


window = tk.Tk() # це створення головного елементу інтерфейсу, а саме - вікна програми

window.title("Це заголовок моєї програми!") # створює заголовок вікна програми

window.geometry("400x200+450+300") # керування розміром і позицією нашого вікна. 400 це ширина, 200 - висота, 450 - це відступ зліва, а 300 - це відступ зверху

window.configure(bg="blue") # змінює колір фону вікна

greeting = tk.Label(text="Hello world!", bg="green", fg="black", font="Arial 50 bold") # це створення віджету для звичайного тексту

greeting.pack()  # це відображення віджета тексту у вікні

button = tk.Button(text="Click me", command=print_msg, bg="black", fg="green", font="Arial 30 bold", bd=0, padx="10", pady="8")

button.pack()

window.resizable(0, 0) # це заборона на зміну розміру екрану користувачеві



window.mainloop() # це нескінченний цикл, який не дає нашому вікну закритись
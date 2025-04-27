import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter.scrolledtext import ScrolledText
from tkinter import colorchooser
from tkinter import Toplevel
from PIL import Image, ImageTk
import random
import pygame

pygame.mixer.init()

sound4 = pygame.mixer.Sound('sound.mp3')
button_click_sound = pygame.mixer.Sound('minecraft_click.mp3')
scrimer = pygame.mixer.Sound('cave1_gqB8CwT.mp3')
root = tk.Tk()
root.title("Счетчик кликов")
root.geometry("400x300") 
root.resizable(False, False)

count = 0
    
a = 0.5



def play_sound():
    button_click_sound.play()

def play_sound2():
    scrimer.play()

def random_color():
    return "#{:02x}{:02x}{:02x}".format(
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255)
    )

def on_button_click():
    global count
    global a
    count += a
    label.config(text=f"Кликов: {count}")
    play_sound()
    new_color = random_color()
    root.config(bg=new_color)
    # меняем фон метки и кнопки, чтобы была гармония или эпилепсия
    label.config(bg=new_color)
    button.config(bg=new_color)

# Метка для отображения текста
label = tk.Label(root, text="Кликов: 0", font=("Comic Sans MS pixel rus eng", 24))
label.pack(pady=20)

# Кнопка
button = tk.Button(root, text="Нажми меня", font=("Comic Sans MS pixel rus eng", 16), command=on_button_click)
button.pack(pady=10)

def click():
    play_sound()
    window = Tk()
    window.title("магазин")
    window.geometry("300x820")
    window.resizable(False, False)
    window["bg"] = "green"

    def one_upgrade():
        play_sound()
        global a
        global count
        if count >= 30:
            count -= 30
            a += 0.5
            label.config(text=f"Кликов: {count}")  # Обновляем метку в основном окне
        else:
            sound4.play()
            showerror(title="Предупреждение", message="Недостаточно кликов")

    button2 = tk.Button(window, text="улучшение на 0.5 за 30", font=("Comic Sans MS pixel rus eng", 16), command=one_upgrade)
    button2.pack(pady=5)

    def two_upgrade():
        play_sound()
        global a
        global count
        if count >= 100:
            count -= 100
            a += 2
            label.config(text=f"Кликов: {count}")  # Обновляем метку в основном окне
        else:
            sound4.play()
            showerror(title="Предупреждение", message="Недостаточно кликов")

    button3 = tk.Button(window, text="улучшение на 2 за 100", font=("Comic Sans MS pixel rus eng", 16), command=two_upgrade)
    button3.pack(pady=10)
    
    def three_upgrade():
        play_sound()
        global a
        global count
        if count >= 1000:
            count -= 1000
            a += 5
            label.config(text=f"Кликов: {count}")  # Обновляем метку в основном окне
        else:
            sound4.play()
            showerror(title="Предупреждение", message="Недостаточно кликов")

    button4 = tk.Button(window, text="улучшение на 5 за 1000", font=("Comic Sans MS pixel rus eng", 16), command=three_upgrade)
    button4.pack(pady=10)

    def four_upgrade():
        play_sound()
        global a
        global count
        if count >= 5000:
            count -= 5000
            a += 25
            label.config(text=f"Кликов: {count}")  # Обновляем метку в основном окне
        else:
            sound4.play()
            showerror(title="Предупреждение", message="Недостаточно кликов")

    button5 = tk.Button(window, text="улучшение на 25 за 5000", font=("Comic Sans MS pixel rus eng", 16), command=four_upgrade)
    button5.pack(pady=10)

    def five_upgrade():
        play_sound()
        global a
        global count
        if count >= 10000:
            count -= 10000
            a += 50
            label.config(text=f"Кликов: {count}")  # Обновляем метку в основном окне
        else:
            sound4.play()
            showerror(title="Предупреждение", message="Недостаточно кликов")

    button6 = tk.Button(window, text="улучшение на 50 за 10000", font=("Comic Sans MS pixel rus eng", 16), command=five_upgrade)
    button6.pack(pady=10)

    def six_upgrade():
        play_sound()
        global a
        global count
        if count >= 15000:
            count -= 15000
            a += 100
            label.config(text=f"Кликов: {count}")  # Обновляем метку в основном окне
        else:
            sound4.play()
            showerror(title="Предупреждение", message="Недостаточно кликов")

    button7 = tk.Button(window, text="улучшение на 100 за 15000", font=("Comic Sans MS pixel rus eng", 16), command=six_upgrade)
    button7.pack(pady=10)

    def seven_upgrade():
        play_sound()
        global a
        global count
        if count >= 20000:
            count -= 20000
            a += 200
            label.config(text=f"Кликов: {count}")  # Обновляем метку в основном окне
        else:
            sound4.play()
            showerror(title="Предупреждение", message="Недостаточно кликов")

    button8 = tk.Button(window, text="улучшение на 200 за 20000", font=("Comic Sans MS pixel rus eng", 16), command=seven_upgrade)
    button8.pack(pady=10)

    def eight_upgrade():
        play_sound()
        global a
        global count
        if count >= 25000:
            count -= 25000
            a += 300
            label.config(text=f"Кликов: {count}")  # Обновляем метку в основном окне
        else:
            sound4.play()
            showerror(title="Предупреждение", message="Недостаточно кликов")

    button9 = tk.Button(window, text="улучшение на 300 за 25000", font=("Comic Sans MS pixel rus eng", 16), command=eight_upgrade)
    button9.pack(pady=10)

    def nine_upgrade():
        play_sound()
        global a
        global count
        if count >= 40000:
            count -= 40000
            a += 500
            label.config(text=f"Кликов: {count}")  # Обновляем метку в основном окне
        else:
            sound4.play()
            showerror(title="Предупреждение", message="Недостаточно кликов")

    button10 = tk.Button(window, text="улучшение на 500 за 40000", font=("Comic Sans MS pixel rus eng", 16), command=nine_upgrade)
    button10.pack(pady=10)

    def ten_upgrade():
        play_sound()
        global a
        global count
        if count >= 50000:
            count -= 50000
            a += 700
            label.config(text=f"Кликов: {count}")  # Обновляем метку в основном окне
        else:
            sound4.play()
            showerror(title="Предупреждение", message="Недостаточно кликов")

    button11 = tk.Button(window, text="улучшение на 700 за 50000", font=("Comic Sans MS pixel rus eng", 16), command=ten_upgrade)
    button11.pack(pady=10)

    def eleven_upgrade():
        play_sound()
        global a
        global count
        if count >= 70000:
            count -= 70000
            a += 1000
            label.config(text=f"Кликов: {count}")  # Обновляем метку в основном окне
        else:
            sound4.play()
            showerror(title="Предупреждение", message="Недостаточно кликов")

    button12 = tk.Button(window, text="улучшение на 1000 за 70000", font=("Comic Sans MS pixel rus eng", 16), command=eleven_upgrade)
    button12.pack(pady=10)

    def twelve_upgrade():
        play_sound()
        global a
        global count
        if count >= 100000:
            count -= 100000
            a += 1500
            label.config(text=f"Кликов: {count}")  # Обновляем метку в основном окне
        else:
            sound4.play()
            showerror(title="Предупреждение", message="Недостаточно кликов")

    button13 = tk.Button(window, text="улучшение на 1500 за 100000", font=("Comic Sans MS pixel rus eng", 16), command=twelve_upgrade)
    button13.pack(pady=10)

    def thirteen_upgrade():
        play_sound()
        global a
        global count
        if count >= 150000:
            count -= 150000
            a += 3000
            label.config(text=f"Кликов: {count}")  # Обновляем метку в основном окне
        else:
            sound4.play()
            showerror(title="Предупреждение", message="Недостаточно кликов")

    button14 = tk.Button(window, text="улучшение на 3000 за 150000", font=("Comic Sans MS pixel rus eng", 16), command=thirteen_upgrade)
    button14.pack(pady=10)

    def fifteen_upgrade():
        play_sound()
        global a
        global count
        if count >= 300000:
            count -= 300000
            a += 6000
            label.config(text=f"Кликов: {count}")  # Обновляем метку в основном окне
        else:
            sound4.play()
            showerror(title="Предупреждение", message="Недостаточно кликов")

    button15 = tk.Button(window, text="улучшение на 6000 за 300000", font=("Comic Sans MS pixel rus eng", 16), command=fifteen_upgrade)
    button15.pack(pady=10)


def click2():
    play_sound()
    window = Tk()
    window.title("настройки")
    window.geometry("300x400")
    window.resizable(False, False)
    window["bg"] = "green"

    style = ttk.Style()
    ttk.Style().theme_use("classic")
    style.configure("TButton", font=("Comic Sans MS pixel rus eng", 20))


    def open_second_window():
        play_sound2()
        second_window = Toplevel(root)
        second_window.title("я предупреждал")
        window.resizable(False, False)
        window["bg"] = "green"


        image = Image.open("mt.png")  
        photo = ImageTk.PhotoImage(image)

        label_image = tk.Label(second_window, image=photo)
        label_image.image = photo  
        label_image.pack()

    button8 = ttk.Button(window, text="не нажимай", command=open_second_window, style="TButton")
    button8.pack(anchor=tk.CENTER, expand=True)

style = ttk.Style()
ttk.Style().theme_use("classic")
style.configure("TButton", font=("Comic Sans MS pixel rus eng", 16))

button = ttk.Button(root, text="настройки", command=click2, style="TButton")
button.pack(anchor=CENTER, expand=1)



button = ttk.Button(root, text="магазин", command=click, style="TButton")
button.pack(anchor=CENTER, expand=1)

def open_warning(): 
    sound4.play()
    showerror(title="Предупреждение", message="в разработке")

warning_button = ttk.Button(text="2 проект", command=open_warning)
warning_button.pack(anchor="center", expand=2)

root.mainloop()

pygame.quit()
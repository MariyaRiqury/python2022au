import tkinter as tk
import genetic_alg
from tkinter import messagebox as mb
root = tk.Tk()


def btn_clicked():
    str2 = str1.get()
    i = int(genetic_alg.the_evolution_of_a_string(str2))
    # s = str(i)
    if i == -1:
        mb.showerror(
            title='ошибка',
            message='введеная строка не получена, убедитесь, что данные корректны')
    else:
        s = 'введеная строка найдена на итерации номер ' + str(i)
        mb.showinfo(title='готово', message=s)


root['bg'] = '#fafafa'
root.title('genetic algorithm')
root.geometry('400x350')
root.resizable(width=False, height=False)

frame = tk.Frame(root, bg='black')
frame.place(relwidth=1, relheigh=1)

title = tk.Label(
    frame,
    text='Введите небольшую строку на латинице',
    bg='gray',
    font=40)
title.pack()
str1 = tk.Entry(frame, bg='white')
str1.pack()
btn = tk.Button(frame, text='Начать', bg='gray', command=btn_clicked)
btn.pack()

root.mainloop()

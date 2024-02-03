#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk


def sum_():
    try:
        x = float(entry_1.get())
        y = float(entry_2.get())
        res = x + y
        result['text'] = str(res)
    except ValueError:
        result['text'] = "Ошибка"


def sub():
    try:
        x = float(entry_1.get())
        y = float(entry_2.get())
        res = x - y
        result['text'] = str(res)
    except ValueError:
        result['text'] = "Ошибка"


def div():
    try:
        x = float(entry_1.get())
        y = float(entry_2.get())
        res = x / y
        result['text'] = str(res)
    except ValueError:
        result['text'] = "Ошибка"


def mult():
    try:
        x = float(entry_1.get())
        y = float(entry_2.get())
        res = x * y
        result['text'] = str(res)
    except ValueError:
        result['text'] = "Ошибка"


if __name__ == '__main__':
    # Создание главного окна
    root = tk.Tk()
    root.title("Калькулятор")

    # Текстовые поля для ввода чисел
    entry_1 = tk.Entry(root)
    entry_2 = tk.Entry(root)
    result = tk.Label()

    # Кнопки операций
    but_sum = tk.Button(text="+", command=sum_)
    but_sub = tk.Button(text="-", command=sub)
    but_mult = tk.Button(text="*", command=mult)
    but_div = tk.Button(text="/", command=div)

    # Размещение элементов с использованием grid
    entry_1.grid(row=0, column=0)
    entry_2.grid(row=0, column=1)
    but_sum.grid(row=2, column=0)
    but_sub.grid(row=2, column=1)
    but_mult.grid(row=3, column=0)
    but_div.grid(row=3, column=1)
    result.grid(row=4, column=0, columnspan=2)

    root.mainloop()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import *


def change():
    selected_name = names[var.get()]
    label['text'] = f"Телефон: {phonebook[selected_name]}"


if __name__ == '__main__':
    root = Tk()

    var = IntVar()
    var.set(-1)

    names = ["Иван", "Мария", "Алексей"]
    phonebook = {"Иван": "+79124235613", "Мария": "+79215543210", "Алексей": "+79091234567"}

    person1 = Radiobutton(indicatoron=0, text=names[0],
                          variable=var, value=0,
                          command=change, width=10)
    person2 = Radiobutton(indicatoron=0, text=names[1],
                          variable=var, value=1,
                          command=change, width=10)
    person3 = Radiobutton(indicatoron=0, text=names[2],
                          variable=var, value=2,
                          command=change, width=10)

    label = Label(width=20, height=5)

    person1.pack()
    person2.pack()
    person3.pack()
    label.pack()

    root.mainloop()

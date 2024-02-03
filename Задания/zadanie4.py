#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox


def open_file():
    file_path = entry_filename.get()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            text_field.delete(1.0, tk.END)
            text_field.insert(tk.END, content)
    except FileNotFoundError:
        messagebox.showerror("Error", "Файл не найден")


def save_file():
    try:
        file_path = entry_filename.get()
        data = text_field.get(1.0, tk.END)
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(data)
        messagebox.showinfo("Сохранено", "Файл сохранен")
    except:
        messagebox.showerror("Error", "Не удалось сохранить файл")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Текстовый редактор")

    entry_filename = tk.Entry(root, width=30)
    text_field = tk.Text(root, wrap=tk.WORD, height=10, width=40)

    btn_open = tk.Button(root, text="Открыть", command=open_file)
    btn_save = tk.Button(root, text="Сохранить", command=save_file)

    entry_filename.pack(pady=5)
    btn_open.pack(pady=5)
    btn_save.pack(pady=5)
    text_field.pack(pady=5)

    root.mainloop()

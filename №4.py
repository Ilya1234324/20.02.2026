import tkinter as tk
from tkinter import messagebox
import re

def determine_time_period():
    time_str = entry_time.get().strip()
    
    if not re.match(r'^([0-1][0-9]|2[0-3]):[0-5][0-9]$', time_str):
        messagebox.showerror("Ошибка", "Введите время в формате HH:MM (00:00 - 23:59)")
        return
    
    hours = int(time_str.split(':')[0])
    
    if 6 <= hours < 12:
        period = "УТРО (с 6 утра до 12 дня)"
        color = "#FFD700"
    elif 12 <= hours < 18:
        period = "ДЕНЬ (с 12 дня до 6 вечера)"
        color = "#FFA500"
    elif 18 <= hours < 24:
        period = "ВЕЧЕР (с 6 вечера до 12 ночи)"
        color = "#FF8C00"
    else:
        period = "НОЧЬ (с 12 ночи до 6 утра)"
        color = "#4B0082"
    
    label_result.config(text=f"Время суток: {period}", fg=color, font=("Arial", 14, "bold"))

def clear_all():
    entry_time.delete(0, tk.END)
    label_result.config(text="")

root = tk.Tk()
root.title("Определение времени суток")
root.geometry("500x300")
root.resizable(False, False)

main_frame = tk.Frame(root, padx=30, pady=30)
main_frame.pack(fill=tk.BOTH, expand=True)

title_label = tk.Label(main_frame, text="Введите время в формате HH:MM", font=("Arial", 12))
title_label.pack(pady=(0, 20))

input_frame = tk.Frame(main_frame)
input_frame.pack(pady=10)

entry_time = tk.Entry(input_frame, width=10, font=("Arial", 14), justify="center")
entry_time.pack(side=tk.LEFT, padx=5)

btn_check = tk.Button(input_frame, text="Определить", command=determine_time_period, bg="#2196F3", fg="white", font=("Arial", 11))
btn_check.pack(side=tk.LEFT, padx=5)

info_frame = tk.Frame(main_frame, bg="#f0f0f0", relief=tk.GROOVE, bd=2)
info_frame.pack(fill=tk.BOTH, expand=True, pady=20)

label_result = tk.Label(info_frame, text="", font=("Arial", 14), bg="#f0f0f0", height=3)
label_result.pack(expand=True)

time_rules = tk.Label(main_frame, text="Утро: 06:00 - 11:59\nДень: 12:00 - 17:59\nВечер: 18:00 - 23:59\nНочь: 00:00 - 05:59", 
                     font=("Arial", 10), justify=tk.LEFT, bd=1, relief=tk.SUNKEN, padx=10, pady=5)
time_rules.pack(pady=10)

btn_clear = tk.Button(main_frame, text="Очистить", command=clear_all, bg="#f44336", fg="white", font=("Arial", 11))
btn_clear.pack()

entry_time.bind("<Return>", lambda event: determine_time_period())

root.mainloop()
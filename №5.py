import tkinter as tk
from tkinter import messagebox
import os

RESULTS_FILE = "planets.txt"

def save_to_file():
    planets_earth_like = ["Меркурий", "Венера", "Земля", "Марс"]
    planets_gas_giants = ["Юпитер", "Сатурн", "Уран", "Нептун"]
    
    content = "Планеты-Землеподобные | Газовые гиганты\n"
    content += "-" * 40 + "\n"
    
    for i in range(4):
        content += f"{planets_earth_like[i]:20} | {planets_gas_giants[i]}\n"
    
    try:
        with open(RESULTS_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("Сохранение", f"Планеты распределены в файл '{RESULTS_FILE}'")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{e}")

def clear_file():
    try:
        open(RESULTS_FILE, "w", encoding="utf-8").close()
        messagebox.showinfo("Очистка", f"Файл '{RESULTS_FILE}' очищен")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось очистить файл:\n{e}")

root = tk.Tk()
root.title("Классификация планет")
root.geometry("600x400")
root.resizable(False, False)

main_frame = tk.Frame(root, padx=30, pady=30)
main_frame.pack(fill=tk.BOTH, expand=True)

title_label = tk.Label(main_frame, text="Классификация планет Солнечной системы", font=("Arial", 16, "bold"))
title_label.pack(pady=(0, 20))

planets_frame = tk.Frame(main_frame)
planets_frame.pack(fill=tk.BOTH, expand=True)

earth_like_frame = tk.Frame(planets_frame, relief=tk.GROOVE, bd=2, padx=10, pady=10)
earth_like_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

gas_giants_frame = tk.Frame(planets_frame, relief=tk.GROOVE, bd=2, padx=10, pady=10)
gas_giants_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)

earth_like_label = tk.Label(earth_like_frame, text="Планеты-Землеподобные", font=("Arial", 12, "bold"), fg="green")
earth_like_label.pack(pady=(0, 10))

gas_giants_label = tk.Label(gas_giants_frame, text="Газовые гиганты", font=("Arial", 12, "bold"), fg="blue")
gas_giants_label.pack(pady=(0, 10))

planets_earth_like = ["Меркурий", "Венера", "Земля", "Марс"]
planets_gas_giants = ["Юпитер", "Сатурн", "Уран", "Нептун"]

for planet in planets_earth_like:
    label = tk.Label(earth_like_frame, text=f"• {planet}", font=("Arial", 11))
    label.pack(anchor=tk.W, pady=2)

for planet in planets_gas_giants:
    label = tk.Label(gas_giants_frame, text=f"• {planet}", font=("Arial", 11))
    label.pack(anchor=tk.W, pady=2)

info_label = tk.Label(main_frame, text="Первые 4 планеты - землеподобные, остальные 4 - газовые гиганты", 
                     font=("Arial", 10, "italic"), fg="gray")
info_label.pack(pady=10)

button_frame = tk.Frame(main_frame)
button_frame.pack(pady=10)

btn_save = tk.Button(button_frame, text="Сохранить в файл", command=save_to_file, 
                    bg="#4CAF50", fg="white", font=("Arial", 11), width=15)
btn_save.grid(row=0, column=0, padx=5)

btn_clear = tk.Button(button_frame, text="Очистить файл", command=clear_file, 
                     bg="#f44336", fg="white", font=("Arial", 11), width=15)
btn_clear.grid(row=0, column=1, padx=5)

root.mainloop()
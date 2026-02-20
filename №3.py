import tkinter as tk
from tkinter import messagebox
import os

RESULTS_FILE = "receipt.txt"
prices = []

def add_price():
    try:
        price = float(entry_price.get())
        if price <= 0:
            messagebox.showerror("Ошибка", "Цена должна быть положительным числом")
            return
        prices.append(price)
        listbox_prices.insert(tk.END, f"{len(prices)}. {price:.2f} руб.")
        entry_price.delete(0, tk.END)
        label_total.config(text="")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число")

def calculate_total():
    if not prices:
        messagebox.showwarning("Предупреждение", "Нет добавленных товаров")
        return
    total = sum(prices)
    label_total.config(text=f"ИТОГО: {total:.2f} руб.")

def save_to_file():
    if not prices:
        messagebox.showwarning("Предупреждение", "Нет данных для сохранения")
        return
    
    total = sum(prices)
    content = "ЧЕК ПОКУПКИ\n"
    content += "-" * 30 + "\n"
    for i, price in enumerate(prices, 1):
        content += f"{i}. {price:.2f} руб.\n"
    content += "-" * 30 + "\n"
    content += f"ИТОГО: {total:.2f} руб.\n"
    content += f"Количество товаров: {len(prices)}\n"
    
    try:
        with open(RESULTS_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("Сохранение", f"Чек сохранен в файл '{RESULTS_FILE}'")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{e}")

def clear_all():
    global prices
    prices.clear()
    listbox_prices.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    label_total.config(text="")
    
    try:
        open(RESULTS_FILE, "w", encoding="utf-8").close()
        messagebox.showinfo("Очистка", f"Файл '{RESULTS_FILE}' очищен")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось очистить файл:\n{e}")

def clear_file_only():
    try:
        open(RESULTS_FILE, "w", encoding="utf-8").close()
        messagebox.showinfo("Очистка", f"Файл '{RESULTS_FILE}' очищен")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось очистить файл:\n{e}")

root = tk.Tk()
root.title("Калькулятор стоимости покупки")
root.geometry("500x500")
root.resizable(False, False)

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

input_frame = tk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=(0, 10))

label_price = tk.Label(input_frame, text="Цена товара:", font=("Arial", 12))
label_price.pack(side=tk.LEFT)

entry_price = tk.Entry(input_frame, width=15, font=("Arial", 12))
entry_price.pack(side=tk.LEFT, padx=10)

btn_add = tk.Button(input_frame, text="+", command=add_price, bg="#4CAF50", fg="white", font=("Arial", 12), width=3)
btn_add.pack(side=tk.LEFT)

listbox_frame = tk.Frame(main_frame)
listbox_frame.pack(fill=tk.BOTH, expand=True, pady=10)

scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_prices = tk.Listbox(listbox_frame, yscrollcommand=scrollbar.set, font=("Courier", 11), height=12)
listbox_prices.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=listbox_prices.yview)

label_total = tk.Label(main_frame, text="", font=("Arial", 16, "bold"), fg="blue")
label_total.pack(pady=10)

button_frame = tk.Frame(main_frame)
button_frame.pack(pady=10)

btn_total = tk.Button(button_frame, text="ИТОГО", command=calculate_total, bg="#2196F3", fg="white", font=("Arial", 11), width=12)
btn_total.grid(row=0, column=0, padx=5)

btn_save = tk.Button(button_frame, text="Сохранить", command=save_to_file, bg="#4CAF50", fg="white", font=("Arial", 11), width=12)
btn_save.grid(row=0, column=1, padx=5)

btn_clear = tk.Button(button_frame, text="Очистить всё", command=clear_all, bg="#f44336", fg="white", font=("Arial", 11), width=12)
btn_clear.grid(row=1, column=0, padx=5, pady=5)

btn_clear_file = tk.Button(button_frame, text="Очистить файл", command=clear_file_only, bg="#FF9800", fg="white", font=("Arial", 11), width=12)
btn_clear_file.grid(row=1, column=1, padx=5, pady=5)

entry_price.bind("<Return>", lambda event: add_price())

root.mainloop()
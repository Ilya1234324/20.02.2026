import tkinter as tk
from tkinter import messagebox
import os

RESULTS_FILE = "results.txt"

def calculate():
    try:
        a_val = float(entry_a.get())
        b_val = float(entry_b.get())

        sum_sq = (a_val + b_val) ** 2
        diff_sq = (a_val - b_val) ** 2

        sum_formula = f"{a_val}² + 2*{a_val}*{b_val} + {b_val}²"
        diff_formula = f"{a_val}² - 2*{a_val}*{b_val} + {b_val}²"

        result_text = (
            f"a = {a_val}, b = {b_val}\n"
            f"(a + b)² = {sum_sq:.4f}  ({sum_formula})\n"
            f"(a – b)² = {diff_sq:.4f}  ({diff_formula})\n"
            + "-" * 40 + "\n"
        )

        text_result.insert(tk.END, result_text)
        text_result.see(tk.END)

    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные числа.")

def save_to_file():
    content = text_result.get("1.0", tk.END).strip()
    if not content:
        messagebox.showwarning("Нет данных", "Нечего сохранять. Сначала выполните расчет.")
        return

    try:
        with open(RESULTS_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("Сохранение", f"Результаты сохранены в файл '{RESULTS_FILE}'.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{e}")

def clear_file():
    text_result.delete("1.0", tk.END)

    try:
        open(RESULTS_FILE, "w", encoding="utf-8").close()
        messagebox.showinfo("Очистка", f"Файл '{RESULTS_FILE}' очищен.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось очистить файл:\n{e}")

def clear_all():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    text_result.delete("1.0", tk.END)

root = tk.Tk()
root.title("Калькулятор квадратов суммы и разности")
root.geometry("600x550")
root.resizable(True, True)

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_a = tk.Label(frame_input, text="a =", font=("Arial", 12))
label_a.grid(row=0, column=0, padx=5)

entry_a = tk.Entry(frame_input, width=15, font=("Arial", 12))
entry_a.grid(row=0, column=1, padx=5)

label_b = tk.Label(frame_input, text="b =", font=("Arial", 12))
label_b.grid(row=0, column=2, padx=5)

entry_b = tk.Entry(frame_input, width=15, font=("Arial", 12))
entry_b.grid(row=0, column=3, padx=5)

btn_calc = tk.Button(root, text="Вычислить", command=calculate,
                     bg="#4CAF50", fg="white", font=("Arial", 11), padx=20)
btn_calc.pack(pady=10)

text_result = tk.Text(root, wrap=tk.WORD, width=70, height=15,
                      font=("Courier", 10), borderwidth=2, relief="sunken")
text_result.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_save = tk.Button(frame_buttons, text="Сохранить", command=save_to_file,
                     bg="#2196F3", fg="white", font=("Arial", 11), width=12)
btn_save.grid(row=0, column=0, padx=5)

btn_clear_input = tk.Button(frame_buttons, text="Очистить поля", command=clear_all,
                            bg="#FF9800", fg="white", font=("Arial", 11), width=12)
btn_clear_input.grid(row=0, column=1, padx=5)

btn_clear_file = tk.Button(frame_buttons, text="Очистить файл", command=clear_file,
                           bg="#f44336", fg="white", font=("Arial", 11), width=12)
btn_clear_file.grid(row=0, column=2, padx=5)

if os.path.exists(RESULTS_FILE):
    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as f:
            previous = f.read()
            if previous.strip():
                text_result.insert(tk.END, previous)
                text_result.insert(tk.END, "\n(Загружено из файла)\n")
    except Exception as e:
        pass

root.mainloop()
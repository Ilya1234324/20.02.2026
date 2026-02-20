import tkinter as tk
from tkinter import messagebox
import os

class PriceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор стоимости покупки")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.prices = []

        self.create_widgets()
        
    def create_widgets(self):
        title_label = tk.Label(self.root, text="Калькулятор покупок", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Цена товара:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
        self.price_entry = tk.Entry(input_frame, font=("Arial", 12), width=15)
        self.price_entry.grid(row=0, column=1, padx=5)

        self.add_button = tk.Button(self.root, text="+ Добавить товар", 
                                   command=self.add_price, 
                                   bg="#4CAF50", fg="white", 
                                   font=("Arial", 10), padx=10)
        self.add_button.pack(pady=5)

        info_frame = tk.Frame(self.root)
        info_frame.pack(pady=10)

        tk.Label(info_frame, text="Добавленные товары:", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

        self.items_list = tk.Text(info_frame, width=40, height=5, state="disabled")
        self.items_list.grid(row=1, column=0, columnspan=2, pady=5)

        tk.Label(info_frame, text="Общая сумма:", font=("Arial", 12)).grid(row=2, column=0, pady=5, sticky="w")
        self.total_label = tk.Label(info_frame, text="0.00 руб.", font=("Arial", 12, "bold"), fg="blue")
        self.total_label.grid(row=2, column=1, pady=5, sticky="e")

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.total_button = tk.Button(button_frame, text="Итого", 
                                     command=self.calculate_total,
                                     bg="#2196F3", fg="white", 
                                     font=("Arial", 10), width=10)
        self.total_button.grid(row=0, column=0, padx=5)

        self.save_button = tk.Button(button_frame, text="Сохранить", 
                                    command=self.save_to_file,
                                    bg="#FF9800", fg="white", 
                                    font=("Arial", 10), width=10)
        self.save_button.grid(row=0, column=1, padx=5)

        self.clear_button = tk.Button(button_frame, text="Очистить", 
                                     command=self.clear_file,
                                     bg="#f44336", fg="white", 
                                     font=("Arial", 10), width=10)
        self.clear_button.grid(row=0, column=2, padx=5)

        self.reset_button = tk.Button(self.root, text="Сбросить все товары", 
                                     command=self.reset_prices,
                                     bg="#9E9E9E", fg="white", 
                                     font=("Arial", 10))
        self.reset_button.pack(pady=5)

        self.price_entry.bind("<Return>", lambda event: self.add_price())
        
    def add_price(self):
        "Добавление цены товара в список"
        try:
            price = float(self.price_entry.get())
            if price <= 0:
                messagebox.showwarning("Предупреждение", "Цена должна быть положительным числом!")
                return
            
            self.prices.append(price)
            self.update_items_list()
            self.price_entry.delete(0, tk.END)
            self.price_entry.focus()
            
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число!")
            
    def update_items_list(self):
        "Обновление отображения списка товаров"
        self.items_list.config(state="normal")
        self.items_list.delete(1.0, tk.END)
        
        for i, price in enumerate(self.prices, 1):
            self.items_list.insert(tk.END, f"{i}. {price:.2f} руб.\n")
            
        self.items_list.config(state="disabled")
        
    def calculate_total(self):
        "Расчет общей суммы покупки"
        if not self.prices:
            messagebox.showinfo("Информация", "Список товаров пуст!")
            return
            
        total = sum(self.prices)
        self.total_label.config(text=f"{total:.2f} руб.")
        
    def save_to_file(self):
        "Сохранение результатов в файл"
        if not self.prices:
            messagebox.showwarning("Предупреждение", "Нет данных для сохранения!")
            return
            
        total = sum(self.prices)
        
        try:
            with open("purchase.txt", "a", encoding="utf-8") as file:
                file.write("=" * 40 + "\n")
                file.write(f"Дата и время: {tk.datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("Список товаров:\n")
                for i, price in enumerate(self.prices, 1):
                    file.write(f"  {i}. {price:.2f} руб.\n")
                file.write(f"ИТОГО: {total:.2f} руб.\n")
                file.write("=" * 40 + "\n\n")
                
            messagebox.showinfo("Успех", "Результаты сохранены в файл 'purchase.txt'!")
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")
            
    def clear_file(self):
        "Очистка содержимого файла"
        try:
            if os.path.exists("purchase.txt"):
                open("purchase.txt", "w", encoding="utf-8").close()
                messagebox.showinfo("Успех", "Файл 'purchase.txt' очищен!")
            else:
                messagebox.showinfo("Информация", "Файл 'purchase.txt' не существует!")
                
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось очистить файл: {e}")
            
    def reset_prices(self):
        "Сброс всех добавленных товаров"
        if self.prices:
            self.prices.clear()
            self.update_items_list()
            self.total_label.config(text="0.00 руб.")
            messagebox.showinfo("Информация", "Список товаров очищен!")
        else:
            messagebox.showinfo("Информация", "Список товаров уже пуст!")

if __name__ == "__main__":
    import datetime as tk_datetime
    tk.datetime = tk_datetime
    
    root = tk.Tk()
    app = PriceCalculator(root)
    root.mainloop()
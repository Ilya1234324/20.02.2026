# Калькулятор стоимости покупок 
## Основной код программы:
добавление библиотек и создание главного окна
```bash
import tkinter as tk
from tkinter import messagebox
import os

class PriceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор стоимости покупки")
        self.root.geometry("400x500")
        self.root.resizable(False, False)  # Запрещаем изменение размера окна
        
        self.prices = []  # Список для хранения цен
        self.create_widgets()  # Создаем интерфейс
```
## Логика добавления цен:
```bash
def add_price(self):
    """Добавление цены товара в список"""
    try:
        price = float(self.price_entry.get()) 
        if price <= 0:  
            messagebox.showwarning("Предупреждение", "Цена должна быть положительным числом!")
            return
        
        self.prices.append(price)  # Добавляем в список
        self.update_items_list()   # Обновляем отображение
        self.price_entry.delete(0, tk.END)  # Очищаем поле ввода
        
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число!")
```
## Сохранение в файл:
```bash
def save_to_file(self):
    """Сохранение результатов в файл"""
    total = sum(self.prices)  # Считаем сумму
    
    with open("purchase.txt", "a", encoding="utf-8") as file:
        file.write("=" * 40 + "\n")
        file.write(f"Дата: {datetime.datetime.now()}\n")
        for i, price in enumerate(self.prices, 1):
            file.write(f"  {i}. {price:.2f} руб.\n")
        file.write(f"ИТОГО: {total:.2f} руб.\n")
```

# заключение
Основные функции своего кода я показал




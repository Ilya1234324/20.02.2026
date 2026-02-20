import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title('44')
root.geometry('400x300')
root.configure(bg='pink')


def save_data():
    name = name_entry.get()
    surname = surname_entry.get()
    class_num = class_entry.get()
    group = group_entry.get()

    if not all([name, surname, class_num, group]):
        messagebox.showwarning("Предупреждение", "Заполните все поля!")
        return

    data_line = (f"Имя: {name}, Фамилия: {surname}, Класс: {class_num}, Группа: {group}\n")

    with open("students_data.txt", "a", encoding="utf-8") as file:
        file.write(data_line)

    messagebox.showinfo("Успех", "Данные успешно сохранены!")
    clear_fields()


def delete_bd():
    try:
        open("students_data.txt", "w", encoding="utf-8").close()
        messagebox.showinfo("Успех", "Содержимое файла очищено!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


def clear_fields():
    name_entry.delete(0, tk.END)
    surname_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)
    group_entry.delete(0, tk.END)


name_entry = tk.Entry(root, width=30)
name_entry.place(x=110, y=30)

surname_entry = tk.Entry(root, width=30)
surname_entry.place(x=110, y=80)

class_entry = tk.Entry(root, width=30)
class_entry.place(x=110, y=130)

group_entry = tk.Entry(root, width=30)
group_entry.place(x=110, y=180)


label_name = tk.Label(root, text="Имя:", bg='pink')
label_name.place(x=70, y=30)

label_surname = tk.Label(root, text="Фамилия:", bg='pink')
label_surname.place(x=45, y=80)

label_class = tk.Label(root, text="Класс:", bg='pink')
label_class.place(x=62, y=130)

label_group = tk.Label(root, text="Группа:", bg='pink')
label_group.place(x=57, y=180)


save_button = tk.Button(root, text="Сохранить", command=save_data)
save_button.place(x=240, y=230)

clear_button = tk.Button(root, text="Очистить поля ввода", command=clear_fields)
clear_button.place(x=70, y=230)

clear_button = tk.Button(root, text="Очистить бд", command=delete_bd)
clear_button.place(x=160, y=270)

root.mainloop()
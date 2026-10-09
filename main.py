
import tkinter as tk
from tkinter import ttk

# Формулы конвертации
CONVERSIONS = {
    "Километры → мили": lambda value: value * 0.621371,
    "Килограммы → фунты": lambda value: value * 2.20462,
    "°C → °F": lambda value: value * 9 / 5 + 32
}

# Функция конвертации
def convert():
    try:
        value = float(value_entry.get().replace(",", "."))
    except ValueError:
        result_label.config(text="Введите число, например 12.5")
        return

    conversion_name = conversion_box.get()
    converted = CONVERSIONS[conversion_name](value)

    result_label.config(text=f"Результат: {converted:.2f}")


# Создаём окно
root = tk.Tk()
root.title("Конвертер единиц")
root.geometry("380x260")
root.resizable(False, False)

# Заголовок
heading = ttk.Label(
    root,
    text="Мой конвертер",
    font=("Arial", 16, "bold")
)
heading.pack(pady=15)

# Поле ввода
ttk.Label(root, text="Введите значение:").pack()

value_entry = ttk.Entry(root, width=30)
value_entry.pack(pady=6)

# Выбор конвертации
conversion_box = ttk.Combobox(
    root,
    values=list(CONVERSIONS.keys()),
    state="readonly",
    width=27
)
conversion_box.current(0)
conversion_box.pack(pady=8)

# Кнопка
convert_button = ttk.Button(
    root,
    text="Конвертировать",
    command=convert
)
convert_button.pack(pady=8)

# Результат
result_label = ttk.Label(
    root,
    text="Результат появится здесь"
)
result_label.pack(pady=10)

# Запуск приложения
root.mainloop()

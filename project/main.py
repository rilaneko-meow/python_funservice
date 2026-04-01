import tkinter as tk
from tkinter import ttk
import math


def update_label_text(slider_var, value_label):
    """Обновляет значение под слайдером"""
    value_label.config(text=str(max(0,255 - math.floor(int(slider_var.get()) * 2.56))))


def update_text(*args):
    """Обновляет текст в прямоугольнике при изменении слайдеров"""
    values = [f'{max(0,255 - math.floor(int(v.get()) * 2.56)):02x}' for v in slider_vars]
    col = f"#{''.join(values)}"
    text_var.set(col)
    text_label.config(bg=col)


# Главное окно
root = tk.Tk()
root.title("Подборщик цвета")
root.geometry("780x420")
root.resizable(False, False)

# Главный фрейм с 2 колонками
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

# ЛЕВЫЙ СТОЛБЕЦ - ПРЯМОУГОЛЬНИК
left_frame = ttk.Frame(main_frame)
left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 20))

text_var = tk.StringVar(value="#808080")
text_label = tk.Label(
    left_frame,
    textvariable=text_var,
    bg="#808080",
    fg="white",
    font=("Arial", 14, "bold"),
    relief="solid",
    bd=3,
    height=10,
    width=18,
    anchor="center",
)
text_label.pack(pady=30)

# ПРАВЫЙ СТОЛБЕЦ - СЛАЙДЕРЫ
right_frame = ttk.Frame(main_frame)
right_frame.grid(row=0, column=1, sticky="nsew")

slider_vars = [tk.DoubleVar(value=50) for _ in range(3)]
colors = ['Красный', 'Зеленый', 'Синий']
colors_bg = ['#ff0000', '#00ff00', '#0000ff']

# Фрейм для слайдеров в ряд
sliders_container = ttk.Frame(right_frame)
sliders_container.pack(pady=20)

for i, var in enumerate(slider_vars):
    slider_col = ttk.Frame(sliders_container)
    slider_col.pack(side="left", padx=20)

    # Название цвета
    ttk.Label(slider_col, text=colors[i],
              font=("Arial", 11, "bold")).pack(pady=(0, 8))

    # Значение ПОД слайдером
    value_label = ttk.Label(slider_col, text="50" , font=("Arial", 12, "bold"))
    value_label.config(background=colors_bg[i])
    value_label.pack(pady=(0, 8))

    # Вертикальный слайдер
    scale = ttk.Scale(
        slider_col,  # ← В slider_col!

        to=100,
        orient="vertical",
        variable=var,
        length=160,

    )
    scale.pack()

    # Трассировка для значения + цвета
    var.trace('w', lambda *a, v=var, l=value_label: update_label_text(v, l))
    var.trace('w', update_text)

# Настройка растягивания колонок
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)

# Инициализация
update_text()

root.mainloop()

import tkinter as tk
from tkinter import messagebox


class RoomAreaCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Площадь комнаты")
        self.root.resizable(False, False)  # Размер окна нельзя менять

        # Создание элементов интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        title_label = tk.Label(
            self.root, text="Площадь комнаты", font=("Arial", 12, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=5)

        # Длина
        tk.Label(self.root, text="Длина =").grid(row=1, column=0, padx=5, pady=5)
        self.length_entry = tk.Entry(self.root, width=10)
        self.length_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.root, text="м").grid(row=1, column=2, padx=5, pady=5)

        # Ширина
        tk.Label(self.root, text="Ширина =").grid(row=2, column=0, padx=5, pady=5)
        self.width_entry = tk.Entry(self.root, width=10)
        self.width_entry.grid(row=2, column=1, padx=5, pady=5)
        tk.Label(self.root, text="м").grid(row=2, column=2, padx=5, pady=5)

        # Площадь (результат)
        tk.Label(self.root, text="Площадь =").grid(row=3, column=0, padx=5, pady=5)
        self.area_label = tk.Label(self.root, text="? кв. м", font=("Arial", 10, "bold"))
        self.area_label.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

        # Обработка изменений в полях ввода
        self.length_entry.bind("<KeyRelease>", self.calculate_area)
        self.width_entry.bind("<KeyRelease>", self.calculate_area)

        # Кнопка закрытия с подтверждением
        close_button = tk.Button(
            self.root, text="Закрыть", command=self.confirm_exit
        )
        close_button.grid(row=4, column=1, pady=10)

    def calculate_area(self, event):
        try:
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())

            # Проверка на отрицательные значения
            if length < 0 or width < 0:
                self.area_label.config(text="? кв. м")
                return

            area = length * width
            self.area_label.config(text=f"{area:.2f} кв. м")

        except ValueError:
            # Если введённые значения не являются числами
            self.area_label.config(text="? кв. м")

    def confirm_exit(self):
        if messagebox.askyesno("Подтверждение", "Действительно хотите закрыть программу?"):
            self.root.destroy()


# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = RoomAreaCalculator(root)
    root.mainloop()

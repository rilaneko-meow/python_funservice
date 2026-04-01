import tkinter as tk
from tkinter import messagebox, filedialog


class WallpaperCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Расчёт обоев")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        tk.Label(self.root, text="Расчёт обоев", font=("Arial", 12, "bold")).grid(
            row=0, column=0, columnspan=3, pady=5
        )

        # Ввод параметров комнаты
        tk.Label(self.root, text="Длина =").grid(row=1, column=0, padx=5, pady=5)
        self.length_entry = tk.Entry(self.root, width=10)
        self.length_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.root, text="м").grid(row=1, column=2, padx=5, pady=5)

        tk.Label(self.root, text="Ширина =").grid(row=2, column=0, padx=5, pady=5)
        self.width_entry = tk.Entry(self.root, width=10)
        self.width_entry.grid(row=2, column=1, padx=5, pady=5)
        tk.Label(self.root, text="м").grid(row=2, column=2, padx=5, pady=5)

        tk.Label(self.root, text="Высота =").grid(row=3, column=0, padx=5, pady=5)
        self.height_entry = tk.Entry(self.root, width=10)
        self.height_entry.grid(row=3, column=1, padx=5, pady=5)
        tk.Label(self.root, text="м").grid(row=3, column=2, padx=5, pady=5)

        # Ввод площади одного рулона
        tk.Label(self.root, text="В рулоне =").grid(row=4, column=0, padx=5, pady=5)
        self.roll_area_entry = tk.Entry(self.root, width=10)
        self.roll_area_entry.grid(row=4, column=1, padx=5, pady=5)
        tk.Label(self.root, text="кв. м").grid(row=4, column=2, padx=5, pady=5)

        # Результаты расчёта
        tk.Label(self.root, text="Площадь стен =").grid(row=5, column=0, padx=5, pady=5)
        self.wall_area_label = tk.Label(self.root, text="? кв. м", font=("Arial", 10, "bold"))
        self.wall_area_label.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

        tk.Label(self.root, text="Нужно рулонов =").grid(row=6, column=0, padx=5, pady=5)
        self.rolls_needed_label = tk.Label(self.root, text="? шт.", font=("Arial", 10, "bold"))
        self.rolls_needed_label.grid(row=6, column=1, columnspan=2, padx=5, pady=5)

        # Привязка к событиям ввода
        self.length_entry.bind("<KeyRelease>", self.calculate)
        self.width_entry.bind("<KeyRelease>", self.calculate)
        self.height_entry.bind("<KeyRelease>", self.calculate)
        self.roll_area_entry.bind("<KeyRelease>", self.calculate)

        # Кнопка закрытия с подтверждением
        tk.Button(
            self.root, text="Закрыть", command=self.confirm_exit
        ).grid(row=7, column=1, pady=10)

        # Кнопки "Сохранить" и "Загрузить"
        save_btn = tk.Button(self.root, text="Сохранить", command=self.save_data)
        save_btn.grid(row=8, column=1, pady=5)

        load_btn = tk.Button(self.root, text="Загрузить", command=self.load_data)
        load_btn.grid(row=8, column=2, pady=5)

    def calculate(self, event):
        try:
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            height = float(self.height_entry.get())
            roll_area = float(self.roll_area_entry.get())

            # Проверка на отрицательные значения
            if length < 0 or width < 0 or height < 0 or roll_area <= 0:
                self.wall_area_label.config(text="? кв. м")
                self.rolls_needed_label.config(text="? шт.")
                return

            # Расчёт площади стен (периметр × высота)
            wall_area = 2 * (length + width) * height
            self.wall_area_label.config(text=f"{wall_area:.2f} кв. м")

            # Расчёт количества рулонов (округление вверх до целого числа)
            rolls_needed = int(wall_area / roll_area) + (1 if wall_area % roll_area > 0 else 0)
            self.rolls_needed_label.config(text=f"{rolls_needed} шт.")

        except ValueError:
            # Если введённые значения не являются числами
            self.wall_area_label.config(text="? кв. м")
            self.rolls_needed_label.config(text="? шт.")

    def confirm_exit(self):
        if messagebox.askyesno("Подтверждение", "Действительно хотите закрыть программу?"):
            self.root.destroy()

    def save_data(self):
        """Сохранение данных в файл .dat"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".dat",
            filetypes=[("Data files", "*.dat")],
            title="Сохранить данные"
        )
        if not file_path:
            return  # Если пользователь отменил выбор файла

        # Собираем данные из полей ввода
        data = {
            "length": self.length_entry.get(),
            "width": self.width_entry.get(),
            "height": self.height_entry.get(),
            "roll_area": self.roll_area_entry.get()
        }

        # Записываем данные в файл
        with open(file_path, 'w') as f:
            for key, value in data.items():
                f.write(f"{key}={value}\n")

        messagebox.showinfo("Успех", "Данные сохранены!")

    def load_data(self):
        """Загрузка данных из файла .dat"""
        file_path = filedialog.askopenfilename(
            defaultextension=".dat",
            filetypes=[("Data files", "*.dat")],
            title="Загрузить данные"
        )
        if not file_path:
            return  # Если пользователь отменил выбор файла

        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()

            # Парсим данные из файла
            data = {}
            for line in lines:
                key, value = line.strip().split('=')
                data[key] = value

            # Заполняем поля ввода
            self.length_entry.delete(0, tk.END)
            self.length_entry.insert(0, data["length"])

            self.width_entry.delete(0, tk.END)
            self.width_entry.insert(0, data["width"])

            self.height_entry.delete(0, tk.END)
            self.height_entry.insert(0, data["height"])

            self.roll_area_entry.delete(0, tk.END)
            self.roll_area_entry.insert(0, data["roll_area"])

            # Пересчитываем площадь и рулоны
            self.calculate(None)

            messagebox.showinfo("Успех", "Данные загружены!")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные: {e}")


# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = WallpaperCalculator(root)
    root.mainloop()

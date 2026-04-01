import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("325x350")
        self.root.resizable(False, False)

        self.expression = ""  # Строка с выражением
        self.result = ""      # Результат вычисления

        self.create_widgets()

    def create_widgets(self):
        # Поле для ввода выражения (верхнее)
        self.entry = tk.Entry(
            self.root,
            font=("Courier", 12),
            borderwidth=2,
            relief="sunken",
            width=30
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Поле для вывода результата (нижнее)
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Courier", 12),
            height=2,
            anchor="w"
        )
        self.result_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        # Кнопки цифр и операций
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row, col = 2, 0
        for btn_text in buttons:
            btn = tk.Button(
                self.root,
                text=btn_text,
                font=("Arial", 10),
                width=5,
                height=2,
                command=lambda x=btn_text: self.on_button_click(x)
            )
            btn.grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Кнопка очистки
        clear_btn = tk.Button(
            self.root,
            text="C",
            font=("Arial", 10),
            width=5,
            height=2,
            command=self.clear
        )
        clear_btn.grid(row=row, column=0, padx=2, pady=2)

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        elif char == 'C':
            self.clear()
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)

    def calculate(self):
        try:
            # Вычисляем выражение с помощью eval
            result = eval(self.expression)
            self.result = f"{self.expression}={result}"
            self.result_label.config(text=self.result)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Некорректное выражение: {e}")
            self.clear()

    def clear(self):
        self.expression = ""
        self.result = ""
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")


# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

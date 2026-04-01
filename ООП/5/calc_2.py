import tkinter as tk
from tkinter import font as tkfont

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calc")
        self.root.geometry("270x230")
        self.root.resizable(False, False)

        # Шрифт для кнопок и поля ввода
        self.button_font = tkfont.Font(family="Arial", size=12, weight="bold")
        self.entry_font = tkfont.Font(family="Arial", size=16)

        # Поле ввода (дисплей калькулятора)
        self.entry = tk.Entry(
            root,
            font=self.entry_font,
            justify="right",
            bd=5,
            relief="sunken",
            width=20
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

        # Кнопки калькулятора (создаём в виде сетки 4x4)
        buttons = [
            '7', '8', '9', 'C',
            '4', '5', '6', '/',
            '1', '2', '3', '*',
            '0', '=', '+', '-'
        ]

        for i, btn_text in enumerate(buttons):
            row = i // 4 + 1  # строка (1-4)
            col = i % 4       # столбец (0-3)

            btn = tk.Button(
                root,
                text=btn_text,
                font=self.button_font,
                width=2,
                height=1,
                bg='lightgray',
                command=lambda t=btn_text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, padx=10, pady=2, sticky="nsew")

    def on_button_click(self, char):
        current = self.entry.get()

        if char == 'C':
            # Очистка поля
            self.entry.delete(0, tk.END)
        elif char == '=':
            # Вычисление результата
            try:
                result = str(eval(current))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Ошибка")
        else:
            # Добавление символа в поле
            self.entry.insert(tk.END, char)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

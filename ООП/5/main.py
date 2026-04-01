from modell import Calc  # предполагаем, что функция Calc определена в модуле model
from tkinter import Tk, ttk, Listbox, StringVar, messagebox

# Создание приложения
app = Tk()
app.title("Калькулятор")
app.geometry("200x150")

# Компонент TComboBox (выпадающий список для ввода выражений)
input_var = StringVar()
input_var.set("2.5+3.7")  # начальное значение с вещественными числами
Input = ttk.Combobox(app, textvariable=input_var, values=[], height=1)
Input.pack(fill='x', padx=5, pady=5)  # аналог align="top"
Input.bind('<Return>', lambda event: calculate_expression())  # обработка Enter

# Компонент TListBox (список для вывода результатов)
Answers = Listbox(app)
Answers.pack(fill='both', expand=True, padx=5, pady=5)  # аналог align="client"

# Список для хранения истории выражений (для TComboBox)
history = []

# Функция вычисления выражения
def calculate_expression():
    expression = Input.get().strip()
    
    if not expression:
        return

    try:
        # Вычисляем выражение с помощью функции Calc из модуля model
        result = Calc(expression)
        
        # Округление результата до 10 знаков после запятой (для избежания проблем с float)
        result_rounded = round(float(result), 10)
        
        # Добавляем результат в начало списка Answers
        Answers.insert(0, f"{expression} = {result_rounded}")
        
        # Если выражение ещё не в истории, добавляем его
        if expression not in history:
            history.append(expression)
            Input['values'] = history  # обновляем выпадающий список
            
    except ValueError as e:
        Answers.insert(0, f"Ошибка: некорректное число в выражении — {e}")
    except ZeroDivisionError:
        Answers.insert(0, "Ошибка: деление на ноль!")
    except SyntaxError:
        Answers.insert(0, "Ошибка: синтаксис выражения некорректен!")
    except Exception as e:
        Answers.insert(0, f"Ошибка при вычислении: {e}")

# Запуск главного цикла приложения
app.mainloop()

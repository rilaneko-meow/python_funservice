class LogicGate:
    def __init__(self):
        self.input_a = 0
        self.input_b = 0
        self.output = 0

    def set_inputs(self, a, b):
        self.input_a = a
        self.input_b = b

    def get_output(self):
        raise NotImplementedError("Метод должен быть переопределён в наследниках.")


class TXor(LogicGate):
    def get_output(self):
        return int(self.input_a != self.input_b)


class TImp(LogicGate):
    def get_output(self):
        if self.input_a == 1 and self.input_b == 0:
            return 0
        else:
            return 1


def build_truth_tables():
    txor = TXor()
    timp = TImp()

    # Таблица для XOR
    #print("Таблица истинности для «исключающее ИЛИ» (TXor):")
    print()
    print("A | B | A xor B")
    print("-" * 15)
    for a in [0, 1]:
        for b in [0, 1]:
            txor.set_inputs(a, b)
            result = txor.get_output()
            print(f"{a} | {b} | {result}")

    # Таблица для импликации
    #print("\nТаблица истинности для «импликация» (TImp):")
    print()
    print("A | B | A -> B")
    print("-" * 15)
    for a in [0, 1]:
        for b in [0, 1]:
            timp.set_inputs(a, b)
            result = timp.get_output()
            print(f"{a} | {b} | {result}")


if __name__ == "__main__":
    build_truth_tables()

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


class AndGate(LogicGate):
    def get_output(self):
        return int(self.input_a and self.input_b)


class OrGate(LogicGate):
    def get_output(self):
        return int(self.input_a or self.input_b)


class NotGate(LogicGate):
    def __init__(self):
        super().__init__()
        self.input_single = 0

    def set_input(self, value):
        self.input_single = value

    def get_output(self):
        return int(not self.input_single)


class TNAnd(LogicGate):
    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()

    def get_output(self):
        self.and_gate.set_inputs(self.input_a, self.input_b)
        and_result = self.and_gate.get_output()
        self.not_gate.set_input(and_result)
        return self.not_gate.get_output()


class TNOr(LogicGate):
    def __init__(self):
        self.or_gate = OrGate()
        self.not_gate = NotGate()

    def get_output(self):
        self.or_gate.set_inputs(self.input_a, self.input_b)
        or_result = self.or_gate.get_output()
        self.not_gate.set_input(or_result)
        return self.not_gate.get_output()


def build_truth_tables():
    tnand = TNAnd()
    tnor = TNOr()

    #print("Таблица истинности для «И-НЕ» (TNAnd):")
    print()
    print("A | B | A nand B")
    print("-" * 15)
    for a in [0, 1]:
        for b in [0, 1]:
            tnand.set_inputs(a, b)
            result = tnand.get_output()
            print(f"{a} | {b} | {result}")

    #print("\nТаблица истинности для «ИЛИ-НЕ» (TNOr):")
    print()
    print("A | B | A nor B")
    print("-" * 15)
    for a in [0, 1]:
        for b in [0, 1]:
            tnor.set_inputs(a, b)
            result = tnor.get_output()
            print(f"{a} | {b} | {result}")


if __name__ == "__main__":
    build_truth_tables()

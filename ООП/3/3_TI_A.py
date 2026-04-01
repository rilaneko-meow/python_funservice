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


class OrNotCircuit:
    def __init__(self):
        self.or_gate = OrGate()
        self.not_gate = NotGate()

    def calculate(self, a, b):
        self.or_gate.set_inputs(a, b)
        or_result = self.or_gate.get_output()
        self.not_gate.set_input(or_result)
        return self.not_gate.get_output()


def build_truth_table():
    circuit = OrNotCircuit()
    print("A | B | not(A + B)")
    print("-" * 15)
    for a in [0, 1]:
        for b in [0, 1]:
            result = circuit.calculate(a, b)
            print(f"{a} | {b} | {result}")


if __name__ == "__main__":
    build_truth_table()

class LampRow:
    def __init__(self, num_lamp = 6):
        # начальное состояние — все лампочки выключены
        self._num_lamps = num_lamp
        self._state = '0' * num_lamp

    def get_state(self):
        return self._state

    def set_state(self, value):
        if len(value) == self._num_lamps and all(c in "01" for c in value):
            self._state = value
        else:
            # Если условия не выполнены — сбрасываем состояние к "000...0" (все выключены)
            print('ошибка')
            self._state = "0" * self._num_lamps

    def show(self):
        #Выводит на экран состояние лампочек: 0 → '-', 1 → '*'.
        display = ''.join('*' if c == '1' else '-' for c in self._state)
        print(display)

        
lamps = LampRow(6)
lamps.show()

lamps.set_state("101010")
print(lamps.get_state()) 
lamps.show()

lamps.set_state("10101010")
print(lamps.get_state()) 
lamps.show()

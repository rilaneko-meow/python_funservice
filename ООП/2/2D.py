class LampRow:
    def __init__(self, num_lamp):
        # начальное состояние — все лампочки выключены
        self._num_lamps = num_lamp
        self._state = 0

    def get_state(self):
        # Преобразуем целое число в строку с нулями слева (до нужной длины)
        if self._state == 0:
            self._state = str(self._state) * self._num_lamps
        else:
            self._state = str(self._state)
        return self._state

    def set_state(self, value):
        if len(value) != self._num_lamps or not all(c in "012" for c in value):
            print('ошибка')
            self._state = 0
        else:
            self._state = int(value)

    state = property(get_state, set_state)

    def show(self):
        s = ""
        if self._state == 0:
            s = '-' * self._num_lamps
        else:
            for i in str(self._state):
                if i == '1':
                    s += "*"  # Красный цвет
                elif i == '2':
                    s += "o"  # Зелёный цвет
                else:
                    s += "-"  # Выключено
        print(s)

        
lamps = LampRow(6)
lamps.show()

lamps.set_state("102102")
print(lamps.get_state()) 
lamps.show()

lamps.set_state("10201010")
print(lamps.get_state()) 
lamps.show()

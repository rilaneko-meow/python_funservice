class LampRow:
    def __init__(self):
        # начальное состояние — все лампочки выключены
        self.state = '00000000'  

    def get_state(self):
        #Возвращает текущее состояние ряда лампочек.
        return self.state

    def show(self):
        #Выводит на экран состояние лампочек: 0 → '-', 1 → '*'.
        display = ''.join('*' if c == '1' else '-' for c in self.state)
        print(display)

        
lamps = LampRow()
lamps.show()   
lamps.state = "10101010"
print( lamps.state ) 
lamps.show()            

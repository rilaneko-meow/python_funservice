class TTrigger:
    def __init__(self, initial_q):
        self.q = initial_q

    def next_state(self, a, b):
       
        if a == 0 and b == 0:
            return self.q
        elif a == 0 and b == 1:
            return 0
        elif a == 1 and b == 0:
         
            return 1
        elif a == 1 and b == 1:
           
            return 1

    def build_truth_table(self):
        print()
        print(f"При Q = {self.q}:")
        print("A | B | Q")
        print("---------")

        for a in [0, 1]:
            for b in [0, 1]:
                new_q = self.next_state(a, b)
                print(f"{a} | {b} | {new_q}")
        print()  



if __name__ == "__main__":
   
    trigger_q0 = TTrigger(initial_q=0)
    trigger_q0.build_truth_table()

    trigger_q1 = TTrigger(initial_q=1)
    trigger_q1.build_truth_table()

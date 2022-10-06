'''
class Complexno:
    def __init__(self,i=0,j=0):
        self.real = i
        self.imag = j
    def get_data(self):
        print(f'{self.real}+{self.imag}')

a = Complexno(2,3)
a.get_data()
'''
class TakeInputs:
    def __init__(self,no_of_inputs):
        self.n = no_of_inputs
        self.no = [int(input("Enter the inputs"+str(i+1)+" = "))for i in range(self.n)]
        print(self.no)
    def Print_inputs(self):
        for i in range(self.n):
            print("The entred inputs is", i+1 , "is", self.no[i])
    def Calculate_Sum(self):
        z = 0
        for i in range(self.n):
            z = z + self.no[i]
        print("sum = ", z)
a = TakeInputs(4)
a.Print_inputs()
a.Calculate_Sum()

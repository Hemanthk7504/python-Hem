class main():
    def __init__(self):
        self.name = "Hemanth"
class main1:
    def main1(self):
        self.Id = 202207
class main2():
    def main2(self):
        self.salary = 8000.00
class main3(main,main1,main2):
    def main4(self):
        super().main1()
        super().main2()
        super().__init__() 
        print(self.name,self.Id,self.salary)

obj = main3()
obj.main4()


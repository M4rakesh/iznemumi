class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def saskaitisana(self):
        return self.num1 + self.num2
    def atnemsana(self):
        return self.num1 - self.num2
    def reizinasana(self):
        return self.num1 * self.num2
    def dalisana(self):
        try:
            return self.num1 / self.num2
            
        except ZeroDivisionError:
            print("Kļūda: Dalīšāna ar nulli nav atļauta")  
        except ValueError:
            print("Kļūda:Ievadiet, derīgus skaitļus")
        except Exception as e:
            print(f"Radās nepazedzēta kļūda: {e}")
        finally:
            print("Darbība pabeigta")
def get_valid_number(Calculator):
    while True:
        try:
            return float(input(Calculator))
        except ValueError:
            print("Kļūda :ievadiet derigu skaitli ") 
def main():
    print("Laipni lūdzam kalkulatora programma!")  
    pirm = get_valid_number("Ievadiet pirmo skaitli: ")
    otr= get_valid_number("Ievadiet otro skaitli: ")

    calc = Calculator(pirm,otr)
    print(f"Saskaitisana: {calc.saskaitisana()}")
    print(f"Atnemsana: {calc.atnemsana()}")
    print(f"Reizinasana: {calc.reizinasana()}")
    print(f"Dalisana: {calc.dalisana()}")

main() 
'''p1=Calculator(10,5) 
p1.saskaitisana()
print(p1.saskaitisana)
p1.atnemsana()
print(p1.atnemsana)
p1.reizinasana()
print(p1.reizinasana)
p1.dalisana()
print(p1.dalisana)'''

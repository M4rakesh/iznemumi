class Rectangle:

    def __init__(self,height,width):
        self.height= height
        self.width = width
    def perimetrs(self):
        p=self.height * 2 + self.width *2
        print(f"Perimetrs ir:{p}")
        return p
    def area(self):
        a=self.height * self.width
        print(f"Laukums ir:{a}")
        return a
    
def req_int():
    while True:
        try:
            skaitlis = int(input("Ievadiet veselu skaitli platumu: "))
            print(f"Paldie!Jūs ievadījāt:{skaitlis}")
            skaitlis2 = int(input("Ievadiet veselu skaitli augstumu: "))
            print(f"Paldie!Jūs ievadījāt:{skaitlis2}")
            rect1=Rectangle(skaitlis,skaitlis2)
            print(f"Perimetrs ir: {skaitlis * 2 + skaitlis2 * 2},Laukums ir: {skaitlis*skaitlis2}")
            break
        except ValueError:
            print("Kļūda:Lūdzu, ievadiet derīgu veselu skaitli")
        except Exception as e:
            print(f"Radās kļūda; {e}")
        print("Programma")
req_int()
r1=Rectangle(10,4)
r1.perimetrs()
r1.area()

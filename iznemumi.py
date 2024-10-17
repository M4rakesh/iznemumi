def divide_numbers():
    try:
        num1=float(input("Ievadiet pirmo skaitli: "))
        num2=float(input("Ievadiet otro skaitli: "))
        result=num1 / num2
        print(f"Rezultāts:{result}")
    except ZeroDivisionError:
        print("Kļūda: Dalīšāna ar nulli nav atļauta")  
divide_numbers()   
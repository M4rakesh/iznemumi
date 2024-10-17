def read_file():
    try:
        filename=input("Ievadiet faila nosaukumu: ")
        with open(filename,'r') as file:
            content = file.read()
            print("Faila saturs:")
            print(content)
    except FileNotFoundError:
        print(f"Kļūda Fails'{filename}'netika atrasts")
    except PermissionError:
        print(f"Kļūda:Nav piekļuges tiesābu failam'{filename}'")
    except Exception as e:
        print(f"Radās kļūda: {e}")
    finally:
        print("Faila apstrāde pabeigta")

read_file()
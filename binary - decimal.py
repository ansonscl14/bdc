def r():
    def b(): 
        try:
            b = input("Enter a binary number: ")
            d = int(b, 2)
            h = hex(d)
            print(f"Binary: {b}")
            print(f"Decimal: {d}")
            print(f"Hexadecimal: {h[2:].upper()}")
            b()
        except ValueError:
            print("That is not a valid binary number!")
            r()
    def d(): 
        try:
            d = int(input("Enter a decimal number: "))
            b = bin(d)
            h = hex(d)
            print(f"Binary: {b[2:]}")
            print(f"Decimal: {d}")
            print(f"Hexadecimal: {h[2:].upper()}")
            d()
        except ValueError:
            print("That is not a valid decimal number!")
            r()

    def h(): 
        try:
            h = input("Enter a hexadecimal number: ")
            d = int(h, 16)
            b = bin(d)
            print(f"Binary: {b[2:]}")
            print(f"Decimal: {dl}")
            print(f"Hexadecimal: {h.upper()}")
            h()
        except ValueError:
            print("That is not a valid hexadecimal number!")
            r()
    
    try:
        print("Welcome to Binary - Decimal - Hexadecimal converter") 
        i = int(input("Choose your input format. Press 1 for Binary, 2 for Decimal, and 3 for Hexadecimal. "))
        if i == 1:
            while True:
                b()
        elif i == 2:
            while True: 
                d()
        elif i == 3:
            while True: 
                h()
        else: 
            print("Invalid Choice")
            r()
    except ValueError:
        print("Enter a valid value")
        r()

r()

print("Welcome to Binary - Decimal converter") 

def r():
    def bd(): 
        try:
            binary = input("Enter a binary number: ")
            decimal = int(binary, 2)
            print(f"The decimal value of {binary} is {decimal}")
        except ValueError:
            print("That is not a valid binary number!")
    def db(): 
        try:
            d = int(input("Enter a decimal number: "))
            b = bin(d)[2:]
            print(f"The binary value of {d} is {b}")
        except ValueError:
            print("That is not a valid decimal number!")

    
    try:
        way = int(input("Enter 1 for Binary to Decimal. Enter 2 for Decimal to Binary. "))
        if way == 1:
            while True:
                bd()
        elif way ==2:
            while True: 
                db()
    except ValueError:
        print("Enter a valid value")
        r()

r()

def add(input_1, input_2):
    """Adds two numbers and returns the sum."""
    return input_1 + input_2

def subtract(input_1, input_2):
    """Subtracts the second number from the first and returns the difference."""
    return input_1 - input_2

def divide(input_1, input_2):
    """
    Divides the first number by the second.
    Handles division by zero by returning an error message.
    """
    if input_2 == 0:
        while True:
            try:
                second = float(input("Please type a non-zero number: "))
                if second == 0:
                    print("You typed zero. Please enter a number other than zero.")
                else:
                    return input_1 / second
        
            except ValueError:
                print("Please enter a valid number.")

    return input_1 / input_2      

def multiply(input_1, input_2):
    """Multiplies two numbers and returns the product."""
    return input_1 * input_2

operators = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

def calculate():
    calculate_more = True
    input_1 = float(input("Type in the first number\n"))

    while calculate_more:
        for sign in operators:
            print(sign)
        operator_sign = input("Type in an operator\n")

        input_2 = float(input("Type in the second number\n"))
        
        answer = operators[operator_sign](input_1, input_2)

        print(f"{input_1} {operator_sign} {input_2} = {answer}")

        option = input(f"Type 'y' to calculate with {answer}, or type 'n' for new calculation\n or simply 'x' to exit the calculator\n").lower()

        if option == "y":
            input_1 = answer
        elif option == "x":
            break
        else:
            calculate_more = False
           
            calculate()


calculate()

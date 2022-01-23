from art import logo


# ADD
def add(n1, n2):
    return n1 + n2


# SUBTRACT
def subtract(n1, n2):
    return n1 - n2


# MULTIPLY
def multiply(n1, n2):
    return n1 * n2


# DIVIDE
def divide(n1, n2):
    return n1 / n2


# MODULO
def modulo(n1, n2):
    return n1 % n2


# DICT
operations = {
    "+": add,
    "-": subtract, 
    "*": multiply, 
    "/": divide,
    "%": modulo,
    }


# CALCULATOR
def calculator():
    """Erlaubt das Berechnen von zwei Zahlen mit einer von 5 Rechenarten"""
    print(logo)
    ops = []
    num1 = float(input("Wie lautet deine erste Zahl? "))
    for op in operations:
        ops += op
    ops = " ".join(ops)

    # Loop
    end = False
    while not end:
        print(ops)
        op = input("Wähle eines der Rechensymbole: ")
        num2 = float(input("Wie lautet deine zweite Zahl? "))

        # Calc
        answer = operations[op](num1, num2)
        print(f"\n{num1} {op} {num2} = {answer}\n")

        con = input("Möchtest du eine weitere Berechnung vornehmen oder eine neue starten?\n"
                    "Wähle: 'j'a/ 'n'ein/ n'e'u: ").lower()
        if  con == "j":
            num1 = answer
        elif con == "e":
            end = True
            calculator()
        else:
            end = True

    # END MSG
    print("\nMathe ❤")


calculator()

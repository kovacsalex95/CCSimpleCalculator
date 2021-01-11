def is_number(num):
    return num.isnumeric()

def is_valid_operator(operator):
    if (operator == '+'):
        return True
    if (operator == '-'):
        return True
    if (operator == '*'):
        return True
    if (operator == '/'):
        return True
    return False

def ask_for_a_number(force_valid_input = False):
    inp = input('Please provide a number!')

    if (force_valid_input):
        while is_number(inp) == False:
            inp = input('Please provide a number!')
    elif (is_number(inp) == False):
        inp = None

    return inp;

def ask_for_an_operator(force_valid_input = False):
    inp = input('Please provide an operator (one of +, -, *, /)!')

    if (force_valid_input):
        while is_valid_operator(inp) == False:
            inp = input('Please provide an operator (one of +, -, *, /)!')
    elif (is_valid_operator(inp) == False):
        inp = None

    return inp;

def calc(operator, num1, num2):
    if (operator == '+'):
        return float(num1) + float(num2)
    if (operator == '-'):
        return float(num1) - float(num2)
    if (operator == '*'):
        return float(num1) * float(num2)
    if (operator == '/' and num2 == '0'):
        return None
    if (operator == '/'):
        return float(num1) / float(num2)
    return None

def simple_calculator():
    num1 = ask_for_a_number(True)
    op = ask_for_an_operator(True)
    num2 = ask_for_a_number(True)

    result = calc(op, num1, num2)

    if (result != None):
        print(result)

    else:
        print('You should not divide something with zero :(')

simple_calculator()
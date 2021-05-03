def simple_calculator():

    add = lambda a, b : a + b

    sub = lambda a, b : a - b

    mul = lambda a, b : a * b

    float_div = lambda a, b : a / b

    int_div = lambda a, b : int(a // b)
    
    rem = lambda a, b : a % b

    exp = lambda a, b : a ** b

    eq = lambda a, b : float(float(a) == float(b))

    signs = {
        "+" : add,
        "-" : sub,
        "*" : mul,
        "/" : float_div,
        "//" : int_div,
        "%" : rem,
        "**" : exp,
        "^" : exp,
        "=" : eq,
        "==" : eq
    }

    line = input("Enter expression like 'x op y', '=' to quit.:\n").split()

    if "=" == line[0]:
        exit()

    sign = line[1]

    if sign not in signs.keys():
        print("Enter valid operation!")

    try:

        total = signs[sign](float(line[0]), float(line[2]))

        while True:

            print(f"{total:g} ", end="")

            line = input().split()
            sign = line[0]

            if sign == "=":
                print(f"Total:\t {total:g}")
                exit()

            if sign not in signs.keys():
                print("Enter valid operation!")
                continue
            
            total = signs[sign](total, float(line[1]))

    except ZeroDivisionError as e:
        print("You can't divide by 0!")
        simple_calculator()


if __name__ == "__main__":
    simple_calculator()

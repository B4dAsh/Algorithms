def simple_calculator():

    methods = {
        "+" : lambda a, b : a + b,
        "-" : lambda a, b : a - b,
        "*" : lambda a, b : a * b,
        "/" : lambda a, b : a / b,
        "//" : lambda a, b : int(a // b),
        "%" : lambda a, b : a % b,
        "**" : lambda a, b : a ** b,
        "^" : lambda a, b : a ** b,
        "=" : lambda a, b : float(float(a) == float(b)),
        "==" : lambda a, b : float(float(a) == float(b))
    }

    line = input("Enter expression like 'x op y', '=' to quit:\n").split()

    if "=" == line[0]:
        exit()

    method = line[1]

    if method not in methods.keys():
        print("Enter valid operation!")

    try:

        total = methods[method](float(line[0]), float(line[2]))

        while True:

            print(f"{total:g} ", end="")

            line = input().split()
            method = line[0]

            if method == "=":
                print(f"Total:\t {total:g}")
                exit()

            if method not in methods.keys():
                print("Enter valid operation!")
                continue

            total = methods[method](total, float(line[1]))

    except ZeroDivisionError as e:
        print("You can't divide by 0!")
        simple_calculator()


if __name__ == "__main__":
    simple_calculator()

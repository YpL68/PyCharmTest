result = None
operand = None
operator = None
wait_for_number = True
operators_list = ("+", "-", "/", "*")

while True:
    input_str = input(">> ")
    if input_str == "=":
        if result:
            print(f"Result: {result}")
        break
    if wait_for_number:
        if not input_str.isnumeric():
            try:
                operand = float(input_str)
            except ValueError:
                print(f"{input_str} is not a number. Try again.")
                continue
        else:
            operand = int(input_str)

        if operator:
            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "*":
                result *= operand
            else:
                try:
                    result /= operand
                except ZeroDivisionError:
                    print("ZeroDivisionError. Try again.")
                    continue
        else:
            result = operand
    else:
        if input_str in operators_list:
            operator = input_str
        else:
            print(f"{input_str} is not '+' or '-' or '/' or '*'. Try again")
            continue

    wait_for_number = not wait_for_number

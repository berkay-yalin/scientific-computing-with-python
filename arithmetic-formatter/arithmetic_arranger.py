def arithmetic_arranger(problems, display = False):
    DATA = [i.split(' ') for i in problems]

    if len(problems) > 5:
        return "Error: Too many problems."
    for num1, sign, num2 in DATA:
        if sign not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        if not num1.isnumeric() or not num2.isnumeric():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

    lines = [[], [], [], []]
    for num1, sign, num2 in DATA:
        width = len(max([num1, num2], key=len)) + 2
        result = int(num1) + int(num2) if sign == '+' else int(num1) - int(num2)
        lines[0].append(num1.rjust(width))
        lines[1].append(num2.rjust(width).replace(' ', sign, 1))
        lines[2].append('-' * width)
        lines[3].append(str(result).rjust(width))

    output = ['    '.join(i) for i in lines]
    return '\n'.join(output if display else output[:-1])


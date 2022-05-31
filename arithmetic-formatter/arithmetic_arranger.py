import operator
from re import findall

def arithmetic_arranger(problems, display = False):
    def validateEquations(operators, operands, other):
        if len(problems) > 5:
            return "Error: Too many problems."
        elif any(not i for i in operators):
            return "Error: Operator must be '+' or '-'."
        elif any(i for i in other):
            return "Error: Numbers must only contain digits."
        elif any(len(j) > 4 for i in operands for j in i):
            return "Error: Numbers cannot be more than four digits."
        else:
            return True

    def formatEquation(num1, sign, num2):
        ops = {'+': operator.add, '-': operator.sub}
        length = len(max([num1, num2], key = len)) + 1 + 1
        return [
            num1.rjust(length, ' '),
            num2.rjust(length, ' ').replace(' ', sign, 1),
            '-' * length,
            str(ops[sign](int(num1),int(num2))).rjust(length, ' ')
        ]

    def displayEquations(display):
        array = [formatEquation(*i.split(' ')) for i in problems]
        array = ['    '.join(i) for i in [list(i) for i in zip(*array)]]

        if display == True:
            return '\n'.join(array)
        else:
            return '\n'.join(array[:len(array) - 1])

    ### PARENT FUNCTION ###
    test = validateEquations(
        list(map(lambda x: findall(r'[+-]', x), problems)),
        list(map(lambda x: findall(r'\d+', x), problems)),
        list(map(lambda x: findall(r'[^\d\s+-]', x), problems))
    )
    return displayEquations(display) if test == True else test

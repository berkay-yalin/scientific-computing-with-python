import operator
ops = {'+':operator.add, '-':operator.sub}

def arithmetic_arranger(*args):
    problems = args[0]

    for i in problems: #input validation
        if len(problems) > 5:
            return "Error: Too many problems."

        if i.split()[1] not in ['+','-']:
            return "Error: Operator must be '+' or '-'."

        try:
            int(i.split()[0])
            int(i.split()[2])
        except:
            return "Error: Numbers must only contain digits."

        if len(i.split()[0]) > 4 or len(i.split()[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

    rows = [] #ordering problems into a printable format
    for count, value in enumerate(i.split() for i in problems):
        num1, sign, num2 = value[0], value[1], value[2]
        maxlen = len( str( max( [int(num1),int(num2)] ) ) )
        result = str( ops[sign](int(num1),int(num2)) )

        rows.append([ (' ' * 2) + (' ' * (maxlen-len(num1))) + num1,
                      (sign + ' ') + (' ' * (maxlen-len(num2))) + num2,
                      '-' * (2 + maxlen),
                      ' ' * (maxlen + 2 - len(result)) + result ])

    if len(args) == 1:
        return '{}\n{}\n{}'.format(
            '    '.join(i[0] for i in rows),
            '    '.join(i[1] for i in rows),
            '    '.join(i[2] for i in rows) )
    else:
        return '{}\n{}\n{}\n{}'.format(
            '    '.join(i[0] for i in rows),
            '    '.join(i[1] for i in rows),
            '    '.join(i[2] for i in rows),
            '    '.join(i[3] for i in rows) )

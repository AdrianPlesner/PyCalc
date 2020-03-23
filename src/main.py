from curses.ascii import isdigit

print('Welcome to the Python Calculator\n'
      'Please enter your calculation :)\n')
calc = input()

print('Result = ' + calc)
i = 0
result = 0
operands = []
operators = []
op = ''
while i < len(calc):
    c = calc[i]

    if isdigit(c):
        op += c
    else:
        operands.append(int(op))
        operators.append(c)
        op = ''
    i += 1
operands.append(int(op))


#print('Operands: ')
#print(operands)
#print('operators: ')
#print(operators)


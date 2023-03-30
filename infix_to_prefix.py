# Python3 program to convert infix to prefix.


def isOperator(c):
    return not ('a' <= c <= 'z') and not ('0' <= c <= '9') and not ('A' <= c <= 'Z')


# Function to find priority
# of given operator.
def getPriority(C):
    if C == '-' or C == '+':
        return 1
    elif C == '*' or C == '/':
        return 2
    elif C == '^':
        return 3
    return 0


# Function that converts infix
# expression to prefix expression.
def infixToPrefix(infix):
    # stack for operators.
    operators = []

    # stack for operands.
    operands = []

    for i in range(len(infix)):

        if infix[i] == '(':
            operators.append(infix[i])

        elif infix[i] == ')':
            while len(operators) != 0 and operators[-1] != '(':
                op1 = operands[-1]
                operands.pop()

                op2 = operands[-1]
                operands.pop()

                op = operators[-1]
                operators.pop()

                tmp = op + op2 + op1
                operands.append(tmp)

            operators.pop()


        elif (not isOperator(infix[i])):
            operands.append(infix[i] + "")


        else:
            while len(operators) != 0 and getPriority(infix[i]) <= getPriority(operators[-1]):
                op1 = operands[-1]
                operands.pop()

                op2 = operands[-1]
                operands.pop()

                op = operators[-1]
                operators.pop()

                tmp = op + op2 + op1
                operands.append(tmp)
            operators.append(infix[i])

    while len(operators) != 0:
        op1 = operands[-1]
        operands.pop()

        op2 = operands[-1]
        operands.pop()

        op = operators[-1]
        operators.pop()

        tmp = op + op2 + op1
        operands.append(tmp)

    return operands[-1]


s = "x-y*z"
print(infixToPrefix(s))

def eval_expr(line):
    line = '(' + line + ')'
    stack = []
    i = 0
    while i < len(line):
        if ord('0') <= ord(line[i]) <= ord('9'):
            number = line[i]
            i += 1
            while i < len(line) and ord('0') <= ord(line[i]) <= ord('9'):
                number += line[i]
                i += 1
            if i < len(line) and line[i] == '.':
                number += line[i]
                i += 1
                while i < len(line) and ord('0') <= ord(line[i]) <= ord('9'):
                    number += line[i]
                    i += 1
                number = float(number)
            else:
                number = int(number)
            if stack and stack[-1] == '*':
                stack.pop()
                stack[-1] *= number
            elif stack and stack[-1] == '/':
                stack.pop()
                stack[-1] /= number
            else:
                stack.append(number)
        elif line[i] == ')':
            while stack[-2] != '(':
                number = stack.pop()
                if stack[-1] == '+':
                    stack.pop()
                    stack[-1] += number
                elif stack[-1] == '-':
                    stack.pop()
                    stack[-1] -= number
            number = stack.pop()
            stack.pop()
            if stack and stack[-1] == '*':
                stack.pop()
                stack[-1] *= number
            elif stack and stack[-1] == '/':
                stack.pop()
                stack[-1] /= number
            else:
                stack.append(number)
            i += 1
        else:
            stack.append(line[i])
            i += 1
    return stack.pop()


import sys

exec(sys.stdin.read())

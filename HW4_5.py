def seq(max_length, current_length, opened_parentheses, opened_brackets, *last_opened):
    if current_length + 1 == max_length:
        yield ')' if opened_parentheses else ']'
    else:
        options = [1] * 4  # ([)]
        if max_length - current_length == opened_parentheses + opened_brackets:
            options[0] = options[1] = 0
        if opened_parentheses == 0 or last_opened and last_opened[-1] == '[':
            options[2] = 0
        if opened_brackets == 0 or last_opened and last_opened[-1] == '(':
            options[3] = 0
        if options[0]:
            for row in seq(max_length, current_length + 1, opened_parentheses + 1, opened_brackets, *last_opened, '('):
                yield '(' + row
        if options[1]:
            for row in seq(max_length, current_length + 1, opened_parentheses, opened_brackets + 1, *last_opened, '['):
                yield '[' + row
        if options[2]:
            for row in seq(max_length, current_length + 1, opened_parentheses - 1, opened_brackets, *last_opened[:-1]):
                yield ')' + row
        if options[3]:
            for row in seq(max_length, current_length + 1, opened_parentheses, opened_brackets - 1, *last_opened[:-1]):
                yield ']' + row


n = int(input())
if n and not n % 2:
    for option in seq(n, 0, 0, 0):
        print(option)

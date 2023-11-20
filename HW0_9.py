book = dict((('(', 1), (')', -1), ('[', 2), (']', -2), ('{', 3), ('}', -3)))
deep = []
for symbol in input():
    if book[symbol] < 0 and deep:
        if deep.pop() != -book[symbol]:
            print('no')
            break
    else:
        deep.append(book[symbol])
else:
    if deep:
        print('no')
    else:
        print('yes')

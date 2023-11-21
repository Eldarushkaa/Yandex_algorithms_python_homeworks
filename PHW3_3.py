from collections import defaultdict


def client_balance(name):
    balance = 0
    for stock in clients[name][0]:
        balance += stocks[stock] * clients[name][0][stock]
    return round(balance)


clients = defaultdict(lambda: [defaultdict(lambda: 0), 0])
stocks = defaultdict(lambda: 1)
for i in range(int(input())):
    command = input().split()
    if len(command) == 2:
        print(client_balance(command[1]))
    elif command[0] == 'BUY':
        clients[command[1]][0][command[2]] += int(command[3])
        clients[command[1]][1] -= int(command[3]) * stocks[command[2]]
    elif command[0] == 'SELL':
        amount_to_sell = min(clients[command[1]][0][command[2]], int(command[3]))
        clients[command[1]][0][command[2]] -= amount_to_sell
        clients[command[1]][1] += amount_to_sell * stocks[command[2]]
    elif command[0] == 'PRICE_RAISE':
        stocks[command[1]] += stocks[command[1]] / 100 * float(command[2])
    elif command[0] == 'PRICE_FALL':
        stocks[command[1]] -= stocks[command[1]] / 100 * float(command[2])

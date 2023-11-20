import json


def deep(data):
    if not data:
        return 0
    return sum(map(lambda x: x if isinstance(x, int) else deep(x), data.values()))


fp = open('data.json')
data = json.load(fp)
print(deep(data))

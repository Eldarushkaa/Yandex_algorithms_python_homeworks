class Node:
    def __init__(self, val, weight):
        self.l = None
        self.r = None
        self.v = val
        self.w = weight


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val, weight):
        if not self.root:
            self.root = Node(val, weight)
        else:
            self._add(val, weight, self.root)

    def _add(self, val, weight, node):
        if val == node.v:
            node.w = min(node.w, weight)
        elif val < node.v:
            if node.l:
                self._add(val, weight, node.l)
            else:
                node.l = Node(val, weight)
        else:
            if node.r:
                self._add(val, weight, node.r)
            else:
                node.r = Node(val, weight)

    def find(self, val):
        if self.root:
            return self._find(val, self.root, float('inf'))

    def _find(self, val, node, prev_max):
        if not node:
            return prev_max
        elif val == node.v:
            return node.v
        elif val < node.v:
            return self._find(val, node.l, prev_max)
        elif val > node.v:
            return self._find(val, node.r, node.v)
        else:
            return prev_max

    def view_tree(self):
        if self.root:
            self._view_tree(self.root)

    def _view_tree(self, node):
        if node:
            self._view_tree(node.l)
            print((node.v, node.w), end = " ")
            self._view_tree(node.r)

    def check1(self, n):
        if n is not None:
            yield from self.check1(n.l)
            yield n.v
            yield from self.check1(n.r)

    def __iter__(self):
        yield from self.check1(self.root)


gag = Tree()
for i in range(1, 5):
    gag.add(2*i, i ** 2)
gag.view_tree()
print()

for v in gag:
    print(v)


def permutation(target, current_sum, *args):
    global shortest_path
    for i in range(len(args)):
        if current_sum + args[i] == target and 2 * len(lengths) - len(args) + 1 < shortest_path:
            shortest_path = 2 * len(lengths) - len(args) + 1
            yield str(args[i])
        elif current_sum + args[i] < target:
            for seq in permutation(target, current_sum + args[i], *args[:i], *args[i+1:]):
                yield str(args[i]) + ' ' + seq


n, m = map(int, input().split())
lengths = list(map(int, input().split()))
shortest_path = len(lengths) * 2 + 1
if sum(lengths) * 2 < n:
    print(-1)
else:
    option = ''
    for row in permutation(n, 0, *lengths, *lengths):
        option = row

    if shortest_path == len(lengths) * 2 + 1:
        print(0)
    else:
        print(shortest_path)
        print(option)

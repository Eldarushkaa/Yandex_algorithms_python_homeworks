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
            print((node.v, node.w), end=" ")
            self._view_tree(node.r)

    def check1(self, n):
        if n is not None:
            yield from self.check1(n.l)
            yield n.v
            yield from self.check1(n.r)

    def __iter__(self):
        yield from self.check1(self.root)


def search_insert(nums, target):
    if nums[0][0] > target:
        return -1
    if nums[-1][0] < target:
        return len(nums) - 1
    left = 0
    right = len(nums) - 1
    while left <= right:
        cur = (left + right) // 2
        if nums[cur][0] == target:
            return cur - 1
        elif nums[cur][0] < target < nums[cur + 1][0]:
            return cur
        elif nums[cur][0] < target:
            left = cur + 1
        elif nums[cur + 1][0] > target:
            right = cur


n, m = map(int, input().split())
cities = [dict() for i in range(n + 1)]
for i in range(m):
    a, b, t, w = map(int, input().split())
    cities[a][b] = (t, w)
    cities[b][a] = (t, w)
shortest_path = [Tree() for i in range(n + 1)]
shortest_path[1].add(0, float('inf'))
deep = [{1}]
while deep[-1]:
    deep.append(set())
    for start in deep[-2]:
        for dest in cities[start]:
            for dif_time in shortest_path[start]:
                if

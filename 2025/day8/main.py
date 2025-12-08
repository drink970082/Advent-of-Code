import heapq
import math


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.distinct = n

    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp != yp:
            if self.size[xp] < self.size[yp]:
                xp, yp = yp, xp
            self.parent[yp] = xp
            self.size[xp] += self.size[yp]
            self.distinct -= 1
            return True
        return False


def part1(input):
    nums = [[int(x) for x in line.split(",")] for line in input]
    n = len(nums)
    heap = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1 = nums[i]
            x2, y2, z2 = nums[j]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            heapq.heappush(heap, (dist, i, j))
    uf = UnionFind(n)
    PAIR = 1000
    for _ in range(PAIR):
        _, i, j = heapq.heappop(heap)
        uf.union(i, j)
    sizes = sorted(uf.size, reverse=True)[:3]
    return math.prod(sizes)


def part2(input):
    nums = [[int(x) for x in line.split(",")] for line in input]
    n = len(nums)
    heap = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1 = nums[i]
            x2, y2, z2 = nums[j]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            heapq.heappush(heap, (dist, i, j))
    uf = UnionFind(n)
    last_i, last_j = 0, 0
    while heap and uf.distinct > 1:
        _, i, j = heapq.heappop(heap)
        if uf.union(i, j):
            last_i, last_j = i, j
    return nums[i][0] * nums[j][0]

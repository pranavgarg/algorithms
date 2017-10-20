class QuickUnion:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    def root(self, i):
        while True:
            if i == self.id[i]:
                return i
            else:
                i = self.id[i]
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if (self.size[i] < self.size[j]):
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]
        print(self.id)
    def hashmap(self):
        hashmap = {}
        for i in self.id:
            root = self.root(i)
            if root in hashmap:
                hashmap[root] = hashmap[root] + 1
            else:
                hashmap[root] = 1
        return hashmap

#n,p = map(int, input().split(' '))
n,p=10,7
h = QuickUnion(n)
# for i in range(p):
#     i,m = map(int, input().split(' '))
h.union(0, 2)
h.union(1, 8)
h.union(1, 4)
h.union(2, 8)
h.union(2, 6)
h.union(3, 5)
h.union(6, 9)

hashmap = h.hashmap()

result = 0
totalsum = 0
for i in hashmap.values():
    result = result + totalsum *i
    totalsum = totalsum + i
print(result)



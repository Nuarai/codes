from itertools import combinations

n, k = map(int, input().split())
seg = []

for comb in combinations(range(1, n + 1), k):
    seg.append(comb[::-1])

for _ in sorted(seg):
    print(*list(_))


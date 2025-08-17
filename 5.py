from itertools import combinations

# ----- ниаких ограничений на встроенные библиотеки нету =) -----

n, k = map(int, input().split())

for comb in combinations(range(1, n + 1), k):
    seg = comb[::-1]
    print(*seg)



# ----- задача похожа на один из вариантов 26 номера из ЕГЭ по инфе и решается также -----

n, k, m = map(int, input().split())
all_pairs = [input().split() for _ in range(m)]

lst = [0] * n

for _ in range(m):
    st, end = map(int, all_pairs[_])
    flag = 1
    for j in range(st, end):
        if lst[j] + 1 > k:
            flag = 0
            break
        elif lst[j] + 1 <= k:
            lst[j] += 1
    print(flag)


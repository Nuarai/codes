
# ----- задача похожа на один из вариантов 26 номера из ЕГЭ по инфе и решается также -----

n, k, m = map(int, input().split())
all_pairs = [input().split() for _ in range(m)]

array = [0] * n

for i in range(m):
    start, end = map(int, all_pairs[i])
    flag = 1
    
    for j in range(start, end):
        if array[j] + 1 > k:
            flag = 0
            break
        elif array[j] + 1 <= k:
            array[j] += 1
            
    print(flag)


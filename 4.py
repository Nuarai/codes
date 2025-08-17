
# ----- просто и понятно -----

n = int(input())
lst = [int(_) for _ in input().split()]

lst_even = sorted([n for n in lst if n % 2 == 0])
lst_odd = sorted([n for n in lst if n % 2 != 0])

print(*lst_even, *lst_odd)

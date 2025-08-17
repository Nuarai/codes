
# ----- просто и понятно -----

n = int(input())
lst = [int(number) for number in input().split()]

lst_even = sorted([number for number in lst if n % 2 == 0])
lst_odd = sorted([number for number in lst if n % 2 != 0])

print(*lst_even, *lst_odd)

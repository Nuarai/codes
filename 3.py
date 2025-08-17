
# ----- можно сделать и в 3 строки, но так понятнее и проще менять -----

n = int(input())
lst_in = input().split()
lst_out = lst_in[:n//2][::-1] + lst_in[n//2:][::-1]

print(*lst_out)

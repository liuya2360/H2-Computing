from math import log10, floor
n = float(input())
n_req = int(input())
ans = round(n, n_req - int(floor(log10(abs(n)))) - 1)
print(ans)

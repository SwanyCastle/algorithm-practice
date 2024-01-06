# 6
h, m = map(int, input().split())
t = int(input())

t_h = int(t/60)
t_m = t%60

result_h = h + t_h
result_m = m + t_m

if result_m >= 60:
    result_m -= 60
    result_h += 1

if result_h >= 24:
    result_h -= 24

print(result_h, result_m)
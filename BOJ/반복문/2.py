# 2
case = int(input())
sum_list = []

for i in range(0, case):
    a, b = map(int, input().split())
    sum_list.append(a+b)

for i in sum_list:
    print(i)

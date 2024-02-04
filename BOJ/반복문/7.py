num:int = int(input())
sum_list: list = []
for _ in range(num):
    a, b = map(int, input().split())
    sum_list.append(a+b)

for i , s in enumerate(sum_list, 1):
    print(f"Case #{i}: {s}")
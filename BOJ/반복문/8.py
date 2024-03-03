n = int(input())
n_list = []

for i in range(n):
    a, b = map(int, input().split())
    n_list.append([a,b])

for i, n in enumerate(n_list, 1):
    print(f"Case #{i}: {n[0]} + {n[1]} = {sum(n)}")
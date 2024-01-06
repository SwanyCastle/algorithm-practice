# 10
a = int(input())
b = int(input())

b_str = str(b)

for i in b_str[::-1]:
    print(a*int(i))
print(a*b)
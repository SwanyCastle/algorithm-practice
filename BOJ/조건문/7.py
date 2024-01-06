# 7
a, b, c = map(int, input().split())

if a == b and b == c:
    print(10000 + (a * 1000))
elif a == b or b == c or a == c:
    if a == b:
        print(1000 + (a * 100))
    elif b == c:
        print(1000 + (b * 100))
    elif a == c:
        print(1000 + (c * 100))
else:
    num_list = [a, b, c]
    num_list.sort()
    print(num_list[-1] * 100)

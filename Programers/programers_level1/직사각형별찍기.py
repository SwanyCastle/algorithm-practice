# 내가 푼 문제
a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print("*" * a)

# 다른사람이 푼 문제 - 이야 잘한다이
answer = ('*'*a +'\n')*b
print(answer)
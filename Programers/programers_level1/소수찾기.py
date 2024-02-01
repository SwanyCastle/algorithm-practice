# 나의 풀이
def solution1(n) -> int:
    answer: int = 0
    for i in range(2, n+1):
        for j in range(2, int(n**0.5)+1):
            if i % j == 0 and i != j:
                break
        else:
            answer += 1
    return answer

# 다른 풀이 - 와 개똑똑하다...
def solution2(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

rt1 = solution1(10)
rt2 = solution2(5)

print(rt1)
print(rt2)
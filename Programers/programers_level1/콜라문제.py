def solution(a, b, n):
    answer = 0
    while n >= a:
        mod_n = n % a
        answer += int(n/a) * b
        n = (int(n/a) * b) + mod_n
    return answer

rt1 = solution(2, 1, 20)
rt2 = solution(3, 1, 20)

print(rt1)
print(rt2)
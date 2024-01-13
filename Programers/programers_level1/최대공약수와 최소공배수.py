# 내가 푼 문제
def solution(n, m):
    answer = []
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    else:
        answer.append(1)
    answer.append(n*m/answer[0])
    return answer

# 다른사람이 푼 문제
def gcdlcm(a, b):
    c,d = max(a, b), min(a, b)
    t = 1
    while t>0:
        t = c%d
        c, d = d, t
    answer = [ c, int (a*b/c)]
    return answer

rt = solution(16, 30)
print(rt)
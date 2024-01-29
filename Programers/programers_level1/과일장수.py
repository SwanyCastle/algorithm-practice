# 나의 풀이 ...
def solution(k, m, score) -> int:
    answer: int  = 0
    score.sort(reverse=True)
    result: list = []
    tmp: int = m
    for i in range(0, len(score), m):
        if tmp >= len(score):
           tmp = len(score)
        result.append(score[i:tmp])
        tmp += m
    for r in result:
        if len(r) < m:
            break
        answer += min(r) * m
    return answer

# 이건 뭐냐 ㄷㄷㄷㄷ
def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m

rt1 = solution(3, 4, [1, 2, 3, 1, 2, 3, 1])
rt2 = solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])

print(rt1)
print(rt2)
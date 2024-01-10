# 내가 푼 문제
def solution(n: int) -> str:
    answer: str = ''
    for i in range(1, n+1):
        if i%2 != 0:
            answer += '수'
        if i%2 == 0:
            answer += '박'
    return answer

# 다른 사람이 푼 문제 ㄷㄷ
def water_melon(n):
    str = "수박"*n
    return str[:n]
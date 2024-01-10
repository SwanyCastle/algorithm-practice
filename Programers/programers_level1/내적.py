# 내가 푼 문제
def solution(a, b):
    answer = 0
    for i , a_i in enumerate(a):
        answer += a[i]*b[i]
    return answer


# 다른 사람이 푼 문제 zip 을 왜 자꾸 생각 못하냐
def solution(a, b):

    return sum([x*y for x, y in zip(a,b)])
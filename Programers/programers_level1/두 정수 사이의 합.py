# 내가 푼 문제
def solution(a, b):
    answer = 0
    if a > b:
        temp = a
        a = b                   # a, b = b, a 이건 거의 처음봄
        b = temp
    for i in range(a, b + 1):   # sum 함수로 할 수 있었는데 생각 못했다.
        answer += i
    return answer

# 다른 사람이 푼 문제
def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))
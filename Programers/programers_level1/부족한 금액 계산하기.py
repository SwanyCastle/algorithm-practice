# 내가 푼 문제
def solution(price: int, money: int, count: int) -> int:
    answer: int = 0
    for i in range(1, count+1):
        answer += (price * i)
    return answer-money if answer > money else 0

# 다른사람이 푼 문제
def solution1(price, money, count):
    return max(0,price*(count+1)*count//2-money)

rt = solution1(3, 20, 4)
print(rt)
# 내가 푼 문제
def solution(left: int, right: int) -> int:
    sum:int = 0
    num_list: list = [num for num in range(left, right+1)]
    for num in num_list:
        cnt:int = 1
        for i in range(1, int(num/2)+1):
            if num % i == 0: 
                cnt += 1 
        if cnt % 2 == 0:
            sum += num
        if cnt % 2 != 0:
            sum -= num
    return sum

# 다른사람이 푼 문제 수학 ㄷㄷ
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
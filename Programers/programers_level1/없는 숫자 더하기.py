# 내가 푼 문제 
def solution(numbers):
    answer = []
    for i in range(0, 10):
        if i in numbers:
            continue
        else:
            answer.append(i)
    return sum(answer)

# 다른 사람이 푼 문제  -  개똑똑하네 ㄷㄷ
def solution(numbers):
    return 45 - sum(numbers)

# rt = solution([1,2,3,4,6,7,8,0])
# rt = solution([5, 8, 4, 0, 6, 7, 9])

# print(rt)
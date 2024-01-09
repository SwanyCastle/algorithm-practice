def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    if len(answer) == 0:        # if not answer: 이 조건 생각 못했다 ㅎ
        answer.append(-1)
    return answer

# result = solution([5, 9, 7, 10], 5)
result = solution([3, 2, 6], 10)

print(result)
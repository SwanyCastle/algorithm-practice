# 나의 풀이
def solution1(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if not numbers[i] + numbers[j] in answer:
                answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer

# 다른 풀이 - sorted(list(set(answer))) 이건 생각도 못햇ㄷ......
def solution2(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

rt1 = solution1([2,1,3,4,1])
rt2 = solution2([5,0,2,7])

print(rt1)
print(rt2)
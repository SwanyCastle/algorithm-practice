def solution(absolutes, signs):
    answer = 123456789
    for i, sign in enumerate(signs):
        if not sign:
            absolutes[i] *= -1
    answer = sum(absolutes)
    return answer

result = solution([4, 7, 12], [True, False, True])
print(result)
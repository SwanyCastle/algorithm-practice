# 내가 푼 문제
def solution(n):
    answer = 0
    n_list = list(map(str, str(n)))
    n_list.sort()
    n_list.reverse()
    answer_str = ''.join(n_list)
    answer = int(answer_str)
    return answer

# 다른사람이 푼 문제
def solution1(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

result = solution(118372)

print(result)

# 내가 푼 문제 - 갈길이 멀다...
# def solution(n):
#     answer = 0
#     mod = 0
#     mod_list = []
#     while n > 0:
#         if n % 3 == 0:
#             mod_list.append(0)
#         else:
#             mod = n % 3
#             mod_list.append(mod)
#         n = int(n/3)
#     mod_list.reverse()
#     for idx, item in enumerate(mod_list):
#         answer += item * (3**idx)
#     return answer

# 다른 사람이 푼 문제
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3
    # int(tmp, 진법 ex) 2, 3, 8, 10, 16)
    answer = int(tmp, 3)
    return answer

rt1 = solution(45)
rt2 = solution(125)

print(rt1)
print(rt2)
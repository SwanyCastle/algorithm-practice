# 내가 푼 코드
# def solution(t, p):
#     answer = 0
#     idx = 0
#     while idx < len(t):
#         last_idx = idx + len(p)
#         if last_idx > len(t):
#             break
#         if int(t[idx:last_idx]) <= int(p):
#             answer += 1 
#         idx += 1
#     return answer

# 좀더 간결한 코드
def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer

rt1 = solution("3141592", "271")
rt2 = solution("500220839878", "7")
rt3 = solution("10203", "15")

print(rt1)
print(rt2)
print(rt3)
# import math

# def solution(n):
#     answer = 0
#     sqrt_n= int(math.sqrt(n))
#     if sqrt_n * sqrt_n == n:
#         answer = (sqrt_n+1)**2
#     else:
#         answer = -1
#     return answer

# math 의 sqrt 안쓰고 풀면 이렇게 됨
def solution(n):
    answer = 0
    sqrt_n= int(n**(1/2))
    if sqrt_n * sqrt_n == n:
        answer = (sqrt_n+1)**2
    else:
        answer = -1
    return answer

result = solution(4)
print(result)
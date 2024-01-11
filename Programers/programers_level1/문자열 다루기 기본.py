# 내가 푼 문제
def solution(s: str) -> bool:
    return True if (len(s) == 4 or len(s) == 6) and s.isdigit() else False

# 다른사람이 푼 문제
def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]

rt: bool = solution("1234")
print(rt)


# 내가 푼 문제
def solution(s: str) -> str:
    if len(s) % 2 != 0:
        return s[int(len(s) / 2)]
    if len(s) % 2 == 0:
        return s[int(len(s)/2)-1] + s[int(len(s) / 2)]

# 다른 사람이 푼 문제
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]

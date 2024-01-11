# 내가 푼 문제
def solution1(s: str) -> str: 
    ascii_list: list = []
    s_dict: dict = {}
    for i in s:
        s_dict[ord(i)] = i
        ascii_list.append(ord(i))
    ascii_list.sort(reverse=True)

    answer_list: list = []
    for k in ascii_list:
        answer_list.append(s_dict[k])
    return ''.join(answer_list)

# 다른사람이 푼 문제       그냥 기본적으로 대문자가 소문자보다 작게 취급되는거였구만 ㄷㄷ
def solution2(s):
    return ''.join(sorted(s, reverse=True))

rt = solution2("Zbcdefg")
print(rt)
# 내가 푼 문제
def solution(phone_number):
    answer = ["*" for i in phone_number[:len(phone_number)-4]]
    answer_str = "".join(answer) + phone_number[len(phone_number)-4:len(phone_number)]
    return answer_str

# 다른사람이 푼 문제
def hide_numbers(s):
    return "*"*(len(s)-4)+s[-4:]
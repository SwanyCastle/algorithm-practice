def solution(seoul):
    if 'Kim' in seoul:
        return "김서방은 {0}에 있다".format(seoul.index('Kim'))

result = solution(["Jane", "Kim", "Kwak", "Park"])

print(result)
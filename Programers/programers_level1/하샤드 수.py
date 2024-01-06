def solution(x):
    str_x = str(x)
    answer = True
    list_n = list(map(int, str_x))
    list_sum = 0

    # for i in list_n:
    #     list_sum += i
    # for문보단 함수가 조금 빠른듯 하다
    list_sum = sum(list_n) 

    if x % list_sum == 0:
        answer = True
    else:
        answer = False 
    return answer

result = solution(18)
print(result)
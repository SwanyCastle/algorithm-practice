import timeit

# 반복문 실행 시간 측정
def solution_for():
    x = 123456
    str_x = "123456"
    answer = True
    list_n = list(map(int, str_x))
    list_sum = 0

    for i in list_n:
        list_sum += i
    # list_sum = sum(list_n)  # for문이 빠른가 함수가 빠른가

    if x % list_sum == 0:
        answer = True
    else:
        answer = False 
    return answer

loop_time = timeit.timeit(solution_for, number=1000)  # 1000번 반복하여 실행 시간 측정
print(f"Loop time: {loop_time} seconds")

# 함수 실행 시간 측정
def solution_function():
    x = 123456
    str_x = "123456"
    answer = True
    list_n = list(map(int, str_x))
    list_sum = 0

    # for i in list_n:
    #     list_sum += i
    list_sum = sum(list_n)  # for문이 빠른가 함수가 빠른가

    if x % list_sum == 0:
        answer = True
    else:
        answer = False 
    return answer

function_time = timeit.timeit(solution_function, number=1000)  # 1000번 반복하여 실행 시간 측정
print(f"Function time: {function_time} seconds")

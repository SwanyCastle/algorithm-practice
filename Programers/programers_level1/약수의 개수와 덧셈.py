def solution(left: int, right: int) -> int:
    sum:int = 0
    num_list: list = [num for num in range(left, right+1)]
    for num in num_list:
        cnt:int = 1
        for i in range(1, int(num/2)+1):
            if num % i == 0: 
                cnt += 1 
        if cnt % 2 == 0:
            sum += num
        if cnt % 2 != 0:
            sum -= num
    return sum

rt: int = solution(13, 17)
print(rt)
def solution(num):
    answer = 0
    cnt = 0
    while num > 1:
        if num % 2 == 0:
            num = int(num / 2)
            cnt += 1
        else:
            num = (num * 3) + 1
            cnt += 1

        if cnt >= 500:
            cnt = -1
            break
    answer = cnt
    return answer
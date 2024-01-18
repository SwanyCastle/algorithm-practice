# 내가 푼 방법
def solution1(food):
    answer = ''
    f_list = []

    for i, f in enumerate(food):
        # print(f)
        if f == 1:
            continue
        if f % 2 == 1:
            f_list.append(str(i) * int(f/2))
        if f % 2 == 0:
            f_list.append(str(i) * int(f/2))
    else:
        answer = ''.join(f_list)
        f_list.reverse()
        answer += '0'
        answer += ''.join(f_list)
    return answer

# 다른 풀이 중간에 1 있는지 비교 할 필요가 없었구만 ㄷㄷ 리스트 뒤집을 필요도 ㄷㄷ
def solution2(food):
    answer = ''
    for i,n in enumerate(food[1:], 1):
        answer += str(i) * (n//2)
    return answer + "0" + answer[::-1]

rt1 = solution2([1, 3, 4, 6])
rt2 = solution2([1, 7, 1, 2])

print(rt1)
print(rt2)
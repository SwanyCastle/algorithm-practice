# 나의 풀이
def solution1(array, commands):
    answer = []
    tmp_arr = []
    for i in commands:
        tmp_arr = array[i[0]-1:i[1]]
        tmp_arr.sort()
        answer.append(tmp_arr[i[2]-1])
    return answer

# 다른 풀이
def solution2(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

rt = solution1([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
print(rt)
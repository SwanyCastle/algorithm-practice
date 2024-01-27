# 나의 풀이
def solution(n: int, arr1: list, arr2: list) -> list:
    answer: list = []
    sum_or: list = [bin(a1|a2)[2:] for a1, a2 in zip(arr1, arr2)]
    for i in sum_or:
        if len(i) < n:
            i = ('0' * (n-len(i))) + i
        answer.append(''.join(['#'if j == '1' else ' ' for j in i]))
    return answer

# 다른 풀이 - rjust 는 뭐냐 ㄷㄷㄷㄷ
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer


rt1 = solution(5, [9,20,28,18,11], [30,1,21,17,28])
rt2 = solution(6, [46,33,33,22,31,50], [27,56,19,14,14,10])

print(rt1)
print(rt2)
# 내가 푼 문제
def solution(arr):
    if len(arr) == 1:
        return [-1]
    arr.pop(arr.index(min(arr)))
    return arr

# 다른사람이 푼 문제
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]
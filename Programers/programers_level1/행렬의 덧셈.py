# 내가 푼 문제 - 뭔가 많이 부족하다
def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[i]))] for i in range(len(arr1))]

# 다른사람이 푼 문제 
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer

result = solution([[1,2],[2,3]], [[3,4],[5,6]])
print(result)

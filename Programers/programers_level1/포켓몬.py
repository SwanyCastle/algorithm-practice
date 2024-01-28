# 나의 풀이 - 아직 한참 멀었다 ...
from itertools import combinations

def solution(nums) -> int:
    combi_list: list = list(set(nums))
    if len(combi_list) > int(len(nums)/2):
        for i in combinations(combi_list, int(len(nums)/2)):
            return len(i)
    return len(combi_list)

# 다른 풀이 - ㄷㄷ 이게 뭐냐 ..
def solution(ls):
    return min(len(ls)/2, len(set(ls)))

rt1 = solution([3,1,2,3])
rt2 = solution([3,3,3,2,2,4])
rt3 = solution([3,3,3,2,2,2])

print(rt1)
print(rt2)
print(rt3)
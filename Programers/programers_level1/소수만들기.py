from itertools import combinations

def solution(nums) -> int:
    combi_list: list = []
    for i in combinations(nums, 3):
        if sum(i) % 2 == 0:
            continue
        for j in range(3, sum(i)):
            if sum(i) % j == 0:
                break
        else:
            combi_list.append(i)
    return len(combi_list)

rt1 = solution([1,2,3,4])
rt2 = solution([1,2,7,6,4])

print(rt1)
print(rt2)
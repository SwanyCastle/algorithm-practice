def solution(strings, n):
    answer = []
    strings.sort()
    answer = sorted(strings, key=lambda x:x[n])
    return answer

rt1 = solution(["sun", "bed", "car"], 1)
rt2 = solution(["abce", "abcd", "cdx"], 2)

print(rt1)
print(rt2)
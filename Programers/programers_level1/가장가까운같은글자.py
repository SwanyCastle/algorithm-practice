# dict는 상상도 못했다 ....
def solution1(s):
    answer = []
    s = list(s)
    for i in range(len(s)):
        if i == 0:
            answer.append(-1)
            continue
        for idx, c in enumerate(s[i-1::-1], 1):
            if s[i] == c: 
                answer.append(idx)
                break
            else:
                continue
        else:
            answer.append(-1)
    return answer

# 깔끔하다 .....
def solution2(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer


rt1 = solution2('banana')
rt2 = solution2('foobar')
print(rt1)
print(rt2)
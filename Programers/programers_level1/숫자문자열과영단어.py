def solution(s):
    dict_num = {
        "zero" : 0,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
    for k, v in dict_num.items():
        if k in s:
            s = s.replace(k, str(v))
    return int(s)

rt1 = solution("one4seveneight")
rt2 = solution("23four5six7")
rt3 = solution("2three45sixseven")
rt4 = solution("123")

print(rt1)
print(rt2)
print(rt3)
print(rt4)
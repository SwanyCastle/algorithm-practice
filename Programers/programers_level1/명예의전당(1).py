# 나의 풀이
def solution1(k, score):
    answer = []
    top_k = []
    for i in score:
        if len(top_k) >= k:  # 이거 비교할거 없이 일단 넣어 놓고 top_k 길이 3 넘어가면 제일 작은거 빼거나 삭제하면 되는거였음
            if i > min(top_k):
                top_k.pop(top_k.index(min(top_k)))
                top_k.append(i)
        else:
            top_k.append(i)
        answer.append(min(top_k))
    return answer

# 다른 풀이 - 좀더 깔끔 하다
def solution2(k, score):
    q = []
    answer = []
    for s in score:
        q.append(s)
        if len(q) > k:
            q.remove(min(q))
        answer.append(min(q))
    return answer

rt1 = solution1(3, [10, 100, 20, 150, 1, 100, 200])
rt2 = solution2(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])

print(rt1)
print(rt2)
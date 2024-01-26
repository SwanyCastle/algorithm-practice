def solution(name: list, yearning: list, photo: list) -> list:
    answer: list = []
    yearning_dict: dict = dict(zip(name, yearning))
    for p in photo:
        score: int = 0
        for k, v in yearning_dict.items():
            if k in p:
                score += v
        answer.append(score)
    return answer

rt1 = solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])
rt2 = solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]])
rt3 = solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]])

print(rt1)
print(rt2)
print(rt3)
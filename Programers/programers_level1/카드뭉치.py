def solution(cards1, cards2, goal):
    for g in goal:
        if g in cards1 and cards1.index(g) == 0:
            cards1.pop(0)
        elif g in cards2 and cards2.index(g) == 0:
            cards2.pop(0)
        else:
            return 'No'
    else:
        return 'Yes'


rt1 = solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])
rt2 = solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])

print(rt1)
print(rt2)
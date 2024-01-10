# 내가 푼 문제  ㅎㅎ
def solution1(friends, gifts):
    gift_score = {}

    friends_gitf_score = {}
    for i in friends:
        friends_gitf_score[i] = 0
    
    # 선물지수 구하기
    for item in friends:
        gift_sum = 0
        for j in gifts:
            gifts_split = j.split()
            if item == gifts_split[0]:
                gift_sum += 1
            elif item == gifts_split[1]:
                gift_sum -= 1
        gift_score[item] = gift_sum

    # 선물 주고 받은 기록을 토대로 선물 받을 개 수 구하기
    for idx, item in enumerate(friends):
        if idx < len(friends):
            for i in range(idx, len(friends)):
                item_sum = 0
                friends_sum = 0
                # 선물을 주고 받은 기록 구하기
                if item == friends[i]:
                    continue
                else:
                    # 친구a 가 친구b 에게 선물을 줬으면 gift리스트 내의 친구a 가 친구b 에게 선물을 준 횟수 저장 
                    if item + ' ' + friends[i] in gifts:
                        item_sum += gifts.count(item + ' ' + friends[i])
                    # 친구b 가 친구a 에게 선물을 줬으면 gift리스트 내의 친구b 가 친구a 에게 선물을 준 횟수 저장 
                    if friends[i] + ' ' + item in gifts:
                        friends_sum += gifts.count(friends[i] + ' ' + item)
                    print()
                # 친구a 가 선물을 준 기록과 친구b 가 선물을 준 기록을 비교해서 
                # 둘중에 선물을 더 많이 준 사람에게 다음달 선물 1개 추가
                # 친구a 와 친구b 가 서로 선물을 준 기록이 같다면 선물 지수가 높은 사람에게 다음달 선물 1개 추가
                if item_sum > friends_sum:
                    friends_gitf_score[item] += 1
                elif friends_sum > item_sum:
                    friends_gitf_score[friends[i]] += 1
                else:
                    if gift_score[item] > gift_score[friends[i]]:
                        friends_gitf_score[item] += 1
                    elif gift_score[item] < gift_score[friends[i]]:
                        friends_gitf_score[friends[i]] += 1
    return friends_gitf_score[max(friends_gitf_score, key=friends_gitf_score.get)]

# 다른 사람이 푼 문제 ㄷㄷ
def solution2(friends, gifts):
    friends_list=int(not [])
    gift_score={idx:[friends_list-friends_list] for idx in friends}
    friends_len = len(friends)
    answer = [friends_list-friends_list]*friends_len
    for item_gift in gifts:

        item_gift = item_gift.split()
        gift_score[item_gift[friends_list-friends_list]].append(item_gift[friends_list])
        gift_score[item_gift[friends_list-friends_list]][friends_list-friends_list]+=friends_list
        gift_score[item_gift[friends_list]][friends_list-friends_list]-=friends_list

    for i in range(friends_len):
        for j in range(i+friends_list,friends_len):
            if gift_score[friends[i]].count(friends[j])==gift_score[friends[j]].count(friends[i]):
                if gift_score[friends[i]][friends_list-friends_list]>gift_score[friends[j]][friends_list-friends_list]:
                    answer[i]+=friends_list
                elif gift_score[friends[i]][friends_list-friends_list]<gift_score[friends[j]][friends_list-friends_list]:
                    answer[j]+=friends_list
            elif gift_score[friends[i]].count(friends[j])>gift_score[friends[j]].count(friends[i]):
                answer[i]+=friends_list
            else:
                answer[j]+=friends_list
    return max(answer)

result1 = solution1(
    # ["joy", "brad", "alessandro", "conan", "david"], 
    ["muzi", "ryan", "frodo", "neo"],
    # ["a", "b", "c"],
    # ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
    ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
    # ["a b", "b a", "c a", "a c", "a c", "c a"]
)

result2 = solution2(
    # ["joy", "brad", "alessandro", "conan", "david"], 
    ["muzi", "ryan", "frodo", "neo"],
    # ["a", "b", "c"],
    # ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
    ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
    # ["a b", "b a", "c a", "a c", "a c", "c a"]
)


print(result1, result2)
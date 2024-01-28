# 나의 풀이
def solution(a, b):
    day_dict: dict = {
        0: "SUN",
        1: "MON",
        2: "TUE",
        3: "WED",
        4: "THU",
        5: "FRI",
        6: "SAT"
    }
    year_2016: dict = {}
    day_idx: int = 4
    m31_list: list = [1, 3, 5, 7, 8, 10, 12]
    for m in range(1, a+1):
        if m == 2:
            month_dict:dict = {}
            for i in range(1, 30):
                month_dict[i] = day_dict[(day_idx+i) % 7]
                # print(f'{m}월 {i}일 {day_dict[(day_idx+i) % 7]} 요일')
            else:
                year_2016[m] = month_dict
                day_idx = (day_idx+i) % 7
        elif m in m31_list:
            month_dict:dict = {}
            for i in range(1, 32):
                month_dict[i] = day_dict[(day_idx+i) % 7]
                # print(f'{m}월 {i}일 {day_dict[(day_idx+i) % 7]} 요일') 
            else:
                year_2016[m] = month_dict
                day_idx = (day_idx+i) % 7
        else:
            month_dict:dict = {}
            for i in range(1, 31):
                month_dict[i] = day_dict[(day_idx+i) % 7]
                # print(f'{m}월 {i}일 {day_dict[(day_idx+i) % 7]} 요일')
            else:
                year_2016[m] = month_dict
                day_idx = (day_idx+i) % 7

    return year_2016[a][b]

# 다른 풀이 1 - datetime 무친 ㄷㄷㄷ
import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]

#다른 풀이 2
def getDayName(a,b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1)%7]

rt1 = solution(5, 24)
print(rt1)

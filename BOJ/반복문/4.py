# 4
price = int(input())
items = int(input())
sum_price = 0

for i in range(0, items):
    i_price , i_item = map(int, input().split())
    sum_price += i_price * i_item

if price == sum_price:
    print("Yes")
else:
    print("No")
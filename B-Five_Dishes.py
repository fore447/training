import math
dishes = [int(input().rstrip()) for i in range(5)]

last_dish_index = 0
too_much = 9
for i in range(5):
    if  0 < dishes[i]%10 < too_much:
        too_much = dishes[i]%10
        last_dish_index = i
    
Ans = 0
for i in range(5):
    if i != last_dish_index:
        if dishes[i] % 10 != 0:
            Ans += math.ceil(dishes[i]/10)*10
        else:
            Ans += dishes[i]
Ans += dishes[last_dish_index]
print(Ans)
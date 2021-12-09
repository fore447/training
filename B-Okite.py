a = int(input().rstrip())
b = int(input().rstrip())
if abs(a-b) > 4:
    if a > b:
        print(10 + b - a)
    else:
        print(10 + a - b)
else:
    print(abs(a-b))


# a=int(input())
# b=int(input())
# print(min(abs(a-b),10-abs(a-b)))

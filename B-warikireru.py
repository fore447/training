import datetime
Y, M, D = input().rstrip().split('/')
new_Y = int(Y)
new_M = int(M.lstrip('0'))
new_D = int(D.lstrip('0'))
day = datetime.date(new_Y, new_M, new_D)

while new_Y % (new_M * new_D) != 0:
    day = day + datetime.timedelta(days=1)
    new_Y = day.year
    new_M = day.month
    new_D = day.day

print("{}/{:02d}/{:02d}".format(new_Y, new_M, new_D))

# import datetime
# Y,M,D=map(int,input().split("/"))
# day=datetime.date(Y,M,D)
# while Y%(M*D)!=0:
#     day=datetime.date(Y,M,D)+datetime.timedelta(days=1)
#     Y,M,D=day.year,day.month,day.day
# print(day.strftime("%Y/%m/%d"))
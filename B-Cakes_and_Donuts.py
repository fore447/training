N = int(input().rstrip())
flag = False
for i in range(26):
    for j in range(13):
        if i*4+j*7 == N:
            flag = True
            break
if flag == True:
    print('Yes')
else:
    print('No') 

# print("Yes" if [4*x+7*y for y in range(13) for x in range(26)].count(N) else "No")
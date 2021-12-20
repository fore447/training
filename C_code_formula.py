S = input().rstrip().split()
Ans = []
for s in S:
    for i in range(len(s)-1):
        if s[i] == '@':
            for j in range(i+1,len(s)):
                if s[j] == '@':
                    if i+1 != j:
                        Ans.append(s[i+1:j])
                        i = j
                    break
                elif j == len(s)-1:
                    Ans.append(s[i+1:len(s)])
                    i = len(s) - 2
                    break              
print(*sorted(set(Ans)), sep='\n')

# S=input()
# user=[]
# for s in S.split():
#     print(s.split("@")[1:])
#     for name in s.split("@")[1:]:
#         if name:
#             user.append(name)
# for name in sorted(set(user)):
#     print(name)

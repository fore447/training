# N = int(input().rstrip())
# S = [input().rstrip() for i in range(N)]
# M = int(input().rstrip())
# T = [input().rstrip() for i in range(M)]

# strings = {}
# for s in S:
#     if s in strings.keys():
#         strings[s] += 1
#     else:
#         strings[s] = 1

# for t in T:
#     if t in strings.keys():
#         strings[t] += -1
#     else:
#         strings[t] = -1

# if max(strings.values()) >= 0:
#     print(max(strings.values()))
# else:
#     print(0)

N=int(input())
s=[input() for n in range(N)]
M=int(input())
t=[input() for m in range(M)]
word=list(set(s))
print(max(0,max(s.count(word[i])-t.count(word[i]) for i in range(len(word)))))
# S = 'DiscoPresentsDiscoveryChannelProgrammingContest2016'
# W = int(input().rstrip())
# wordCount = 0
# while wordCount < len(S):
#     print(S[wordCount: wordCount+W])
#     wordCount += W

import math
W=int(input())
s="DiscoPresentsDiscoveryChannelProgrammingContest2016"
for i in range(math.ceil(len(s)/W)):
    print(s[W*i:W+W*i])
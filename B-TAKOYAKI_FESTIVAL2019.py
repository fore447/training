N = int(input().rstrip())
octopuses = list(map(int, input().rstrip().split()))
sum = 0
for i in range(N):
    for j in range(i+1,N):
        sum += octopuses[i]*octopuses[j]
print(sum)

# print(sum(octopuses[i]*octopuses[j] for i in range(N) for j in range(i+1,N)))
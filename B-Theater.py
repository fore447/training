N = int(input().rstrip())
total_count = 0
for i in range(N):
    l, r = map(int, input().rstrip().split())
    total_count += r - l + 1
print(total_count)
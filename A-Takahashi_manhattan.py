x1, y1 = map(int, input().rstrip().split())
x2, y2 = map(int, input().rstrip().split())
print(abs(x1-x2) + abs(y1-y2) + 1)
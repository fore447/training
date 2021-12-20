A, B, C = map(int, input().rstrip().split())
print(0 if A-B >= C else C-(A-B))

# A,B,C=map(int,input().split())
# water=C-(A-B)
# print(water if water>0 else 0)

# A, B, C = map(int, input().rstrip().split())
# print(max(0, C-(A-B)))
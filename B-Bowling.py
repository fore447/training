a, b = input().rstrip().split()
P = list(map(int, input().rstrip().split()))
Q = list(map(int, input().rstrip().split()))

pin=['x']*10
for i in P:
    pin[i-1] = "."
for i in Q:
    pin[i-1] = "o"

# print(*pin[6:10])
# print(*pin[3:6])
# print(*pin[1:3])
# print(pin[0])

print(" ".join(pin[6:10]))
print(" "+" ".join(pin[3:6]))
print("  "+" ".join(pin[1:3]))
print("   "+" ".join(pin[0]))
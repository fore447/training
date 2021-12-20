X, A, B = [int(input()) for i in range(3)]
X = X-(A+B)
while X >= B:
    X = X-B
print(X)

# X,A,B=[int(input()) for i in range(3)]
# print((X-A)%B)
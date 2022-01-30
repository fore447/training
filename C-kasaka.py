def is_palindrome(S):
    x = 0
    y = 0

    for i in range(0, len(S)):
        if S[i] == "a":
            x += 1
        else:
            break

    for j in range(len(S)-1, -1, -1):
        if S[j] == "a":
            y += 1
        else:
            break

    if x == len(S):
        return True
    if x > y:
        return False
    for i in range(x, len(S)-y):
        if S[i] != S[x + len(S) - y - i - 1]:
            return False
    return True

S = input().rstrip()

if is_palindrome(S):
    print("Yes")
else:
    print("No")
from collections import deque
a, N = map(int, input().split())

# 探索を打ち切る桁数を決定する
M = 1
while M <= N:
    M *= 10

# 幅優先探索
# 到達した数字とその時の操作回数を記録する配列
num_count = [-1] * M
Q = deque()
# a=1（初期値）の時の操作回数を０とする
num_count[1] = 0
# a=1（初期値）をデキューに追加する
Q.append(1)

while len(Q):
    num = Q.popleft()
    # その数字に到達した時の操作回数を保存する
    count = num_count[num]

    # 現在の数字をa倍する操作
    total = a * num
    if total < M and num_count[total] == -1:
        num_count[total] = count + 1
        Q.append(total)

    # 現在の数字を文字列とみなし、列の末尾と先頭を移動させる操作
    if num >= 10 and num % 10 != 0:
        s = str(num)
        total = int(s[-1] + s[:-1])
        if total < M and num_count[total] == -1:
            num_count[total] = count + 1
            Q.append(total)
print(num_count[N])
# turn=0の時　-, +, -, +, -
# turn=1の時　+, -, +, -, +
def culc_min(arr, tmp_sum, arr_length, turn):
    cnt = 0
    for i in range(arr_length):
        # マイナス計算
        if (i+turn) % 2 == 0:
            if tmp_sum+arr[i] >= 0:
                cnt += abs(arr[i]-(-tmp_sum-1))
                arr[i] = -tmp_sum-1
        #プラス計算
        else:
            if tmp_sum+arr[i] <= 0:
                cnt += abs(arr[i]-(-tmp_sum+1))
                arr[i] = -tmp_sum+1
        tmp_sum += arr[i]

        if i==arr_length-1 and sum(arr[0:arr_length]) == 0:
            cnt += 1
    return cnt   

if __name__ == '__main__':
    n = int(input().rstrip())
    a = list(map(int, input().rstrip().split()))
    tmp_a = a.copy()

    # turn=0の時　-, +, -, +, -
    # turn=1の時　+, -, +, -, +
    nega_posi_cnt = culc_min(a, 0, n, 0)
    posi_nega_cnt = culc_min(tmp_a, 0, n, 1)

    print(min(posi_nega_cnt, nega_posi_cnt))

# 再起関数を利用した場合
# import sys

# sys.setrecursionlimit(10**6)

# def culc_min(idx, tmp_sum, arr, turn):
#     ret = 0
#     # マイナス計算
#     if (idx+turn) % 2 == 0:
#         if tmp_sum+arr[idx] >= 0:
#                 ret += abs(arr[idx] - (-tmp_sum-1))
#                 arr[idx] = -tmp_sum-1
#     # プラス計算
#     else:
#         if tmp_sum+arr[idx] <= 0:
#             ret += abs(arr[idx] - (-tmp_sum+1))
#             arr[idx] = -tmp_sum+1
#     # 配列の最後を参照した時
#     if idx == n-1: 
#         if tmp_sum+arr[idx] == 0:
#             ret += 1
#         return ret
#     ret += culc_min(idx+1, tmp_sum+arr[idx], arr, turn)
#     return ret

# if __name__ == '__main__':
#     n = int(input().rstrip())
#     a = list(map(int, input().rstrip().split()))
#     tmp_a = a.copy()

#     # turn=0の時　-, +, -, +, -
#     # turn=1の時　+, -, +, -, +
#     nega_posi_cnt = culc_min(0, 0, a, 0)
#     posi_nega_cnt = culc_min(0, 0, tmp_a, 1)

#     print(min(posi_nega_cnt, nega_posi_cnt))
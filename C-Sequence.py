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

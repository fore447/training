# +, -, +, -, + の時
def posi_nega(arr, arr_length):
    cnt = 0
    for i in range(n):
        if i % 2 == 0:
            if sum(arr[0:i+1]) < 0:
                cnt += abs(arr[i]-(-sum(arr[0:i])+1))
                arr[i] = -sum(arr[0:i])+1
        else:
            if sum(arr[0:i+1]) > 0:
                cnt += abs(arr[i]-(-sum(arr[0:i])-1))
                arr[i] = -sum(arr[0:i])-1

        if i==arr_length-1 and sum(arr[0:arr_length]) == 0:
            cnt += 1
    return cnt

# -, +, -, +, - の時
def nega_posi(arr, arr_length):
    cnt = 0
    for i in range(n):
        if i % 2 == 0:
            if sum(arr[0:i+1]) > 0:
                cnt += abs(arr[i]-(-sum(arr[0:i])-1))
                arr[i] = -sum(arr[0:i])-1
        else:
            if sum(arr[0:i+1]) < 0:
                cnt += abs(arr[i]-(-sum(arr[0:i])+1))
                arr[i] = -sum(arr[0:i])+1

        if i==arr_length-1 and sum(arr[0:arr_length]) == 0:
            cnt += 1
    return cnt   

if __name__ == '__main__':
    n = int(input().rstrip())
    a = list(map(int, input().rstrip().split()))
    tmp_a = a.copy()
    posi_nega_cnt = posi_nega(a, n)
    nega_posi_cnt = nega_posi(tmp_a, n)

    print(min(posi_nega_cnt, nega_posi_cnt))

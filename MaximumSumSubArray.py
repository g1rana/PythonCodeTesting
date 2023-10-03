
def findMaxSumSubArray(arr):
    l , r , maxSum = -1,-1,0
    cur_sum = 0 
    cur_start  = 0 
    for i in range(len(arr)):
        cur_sum += arr[i]
        if cur_sum < 0:
            cur_start = i + 1
            cur_sum = 0 
        if cur_sum > maxSum:
            l = cur_start
            r = i 
            maxSum = cur_sum
    return maxSum, l, r
    
if __name__ == "__main__":
    arr = [-10,20,-100,210,-80]
    print(findMaxSumSubArray(arr))

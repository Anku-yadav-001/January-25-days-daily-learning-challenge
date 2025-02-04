def lower_bound(arr, k):
    low = 0
    high = len(arr) - 1
    ans = -1  

    while low <= high:
        mid = (low + high) // 2 

        if arr[mid] == k:
            ans = mid  
            high = mid - 1
        elif arr[mid] < k:
            low = mid + 1 
        else:
            high = mid - 1 

    return ans

n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = lower_bound(arr, k)
print(result)
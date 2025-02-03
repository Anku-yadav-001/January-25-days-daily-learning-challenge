def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    key = int(input())

    def binary_search_first(arr, key):
        low = 0
        high = n - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == key:
                ans = mid
                high = mid - 1  
            elif arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def binary_search_last(arr, key):
        low = 0
        high = n - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == key:
                ans = mid
                low = mid + 1 
            elif arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        return ans

    first_occurrence = binary_search_first(arr, key)
    last_occurrence = binary_search_last(arr, key)

    if first_occurrence == -1:
        print("-1 -1 0")
    else:
        count = last_occurrence - first_occurrence + 1
        print(first_occurrence, last_occurrence, count)

solve()
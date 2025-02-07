def merge_sort_and_count(arr):
    n = len(arr)
    if n <= 1:
        return arr, 0

    mid = n // 2
    left_arr, left_inversions = merge_sort_and_count(arr[:mid])
    right_arr, right_inversions = merge_sort_and_count(arr[mid:])

    merged_arr = []
    inversions = left_inversions + right_inversions
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            merged_arr.append(left_arr[i])
            i += 1
        else:
            merged_arr.append(right_arr[j])
            inversions += len(left_arr) - i 
            j += 1

    merged_arr.extend(left_arr[i:])
    merged_arr.extend(right_arr[j:])
    return merged_arr, inversions


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    _, inversions = merge_sort_and_count(arr)
    print(inversions)
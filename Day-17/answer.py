def wood_cutter(n, m, trees):
    """
    Finds the maximum height of the sawblade to cut at least M meters of wood.

    Args:
        n: The number of trees.
        m: The required amount of wood.
        trees: A list of tree heights.

    Returns:
        The maximum height of the sawblade.
    """

    low = 0
    high = max(trees)

    while low <= high:
        mid = (low + high) // 2 
        wood_cut = 0

        for tree in trees:
            if tree > mid:
                wood_cut += tree - mid

        if wood_cut >= m:
            low = mid + 1 
        else:
            high = mid - 1 

    return high 


n, m = map(int, input().split())
trees = list(map(int, input().split()))

result = wood_cutter(n, m, trees)
print(result)
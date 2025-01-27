def find_combinations(n, k):
    """
    Finds all possible combinations of k items from a set of n items.

    Args:
        n: The total number of items.
        k: The number of items to choose.

    Returns:
        A list of lists, where each sublist represents a combination.
    """

    def backtrack(start, combination):
        if len(combination) == k:
            combinations.append(combination[:])
            return

        for i in range(start, n + 1):
            combination.append(i)
            backtrack(i + 1, combination)
            combination.pop()

    combinations = []
    backtrack(1, [])
    return combinations

if __name__ == "__main__":
    n, k = map(int, input().split())
    combinations = find_combinations(n, k)
    for combination in combinations:
        print(*combination)
def largestRectangleArea(heights):
    if not heights:
        return 0
    
    n = len(heights)
    lessFromLeft = [-1] * n  
    lessFromRight = [n] * n  

    for i in range(1, n):
        p = i - 1
        while p >= 0 and heights[p] >= heights[i]:
            p = lessFromLeft[p]
        lessFromLeft[i] = p

    for i in range(n - 2, -1, -1):
        p = i + 1
        while p < n and heights[p] >= heights[i]:
            p = lessFromRight[p]
        lessFromRight[i] = p

    max_area = 0
    for i in range(n):
        max_area = max(max_area, heights[i] * (lessFromRight[i] - lessFromLeft[i] - 1))

    return max_area

heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))

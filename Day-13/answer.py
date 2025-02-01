def min_effort_stacks():
    t = int(input())
    for _ in range(t):
        n, x, y = map(int, input().split())
        stacks = []
        for _ in range(n):
            a, b = map(int, input().split())
            stacks.append((a, b))
        
        total_effort = 0
        for a, b in stacks:
            diff = b - a
            if diff > 0:
                total_effort += diff * x 
            elif diff < 0:
                total_effort += abs(diff) * y  
        print(total_effort)

min_effort_stacks()
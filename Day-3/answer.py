def solve(n, m, roads_input, q, queries):
    graph = {i: set() for i in range(1, n + 1)}
    
    for road in roads_input:
        a, b = road
        graph[a].add(b)
        graph[b].add(a)
    
    result = []
    for x, y in queries:
        if y in graph[x]:
            result.append("YES")
        else:
            result.append("NO")
    
    return result

# Example usage:
n = 5
m = 6
roads_input = [
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (3, 5),
    (4, 5)
]
q = 3
queries = [
    (2, 4),
    (1, 3),
    (1, 5)
]

output = solve(n, m, roads_input, q, queries)
for line in output:
    print(line)

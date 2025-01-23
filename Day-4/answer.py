from collections import defaultdict

def count_houses_graph(roads):
    """
    Calculates the number of houses bought using a graph approach.

    Args:
        roads: A list of tuples, where each tuple represents a road 
               between two houses (e.g., (1, 2), (2, 3)).

    Returns:
        The number of houses bought.
    """
    graph = defaultdict(list)
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x) 

    def dfs(node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    visited = set()
    count = 0
    for node in graph:
        if node not in visited:
            dfs(node, visited)
            count += 1

    return count

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        E = int(input())
        roads = []
        for _ in range(E):
            X, Y = map(int, input().split())
            roads.append((X, Y))
        print(count_houses_graph(roads))
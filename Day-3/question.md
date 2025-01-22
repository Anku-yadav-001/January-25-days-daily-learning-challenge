## No Google Maps in Bangalore Problem

## Problem Description
Imagine there is no Google Maps in Bangalore, and you are tasked with finding whether a direct road exists between two locations. Given N locations and M roads connecting them, along with Q queries, your goal is to determine whether a direct road exists for each query.

## Input Description
- The first line contains two integers 𝑁 (number of locations) and 𝑀 (number of roads).
- The next 𝑀 lines each contain two integers 𝐴 and 𝐵, representing a direct road between locations 𝐴 and 𝐵.
- The next line contains an integer 𝑄, the number of queries.
- The next 𝑄 lines each contain two integers 𝑋 and 𝑌, representing the query to check if there is a direct road between - 𝑋 and 𝑌.

### Constraints
- N≤1000 (Number of locations)
- M≤1000 (Number of roads)
- Q≤1000 (Number of queries)

## Output Format
For each query, print `YES` if there exists a direct road between 𝑋 and 𝑌, otherwise print `NO`.


## Example 
- **Input** 
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

- **Output** 
`
NO
YES
NO
`
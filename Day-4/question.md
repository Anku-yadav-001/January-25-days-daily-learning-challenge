## Let's buy some houses

## Problem Description
You have won the lottery and want to buy some houses. However, there's a condition: to buy two houses, you must also buy the road connecting them. Given a list of roads you have already purchased, determine how many houses you will end up owning.

## Input Description
- The first line contains an integer `T`, representing the number of test cases.
- The first line of each test case contains an integer `E`, denoting the number of roads.
- The next `E` lines1 each contain two space-separated integers `X` and `Y`, indicating that there is a road between house `X` and house

### Constraints
- `1 <= T <= 100`
- `1 <= E <= 1000`
- `1 <= X, Y <= 10000`

## Output Format
For each test case, print the number of houses you will end up buying.

## Example 
### Input 
1
3
1 2
2 3
1 3

### Output 
3

## Explanation:
In this example, you have bought three roads:
- Between house 1 and house 2
- Between house 2 and house 3
- Between house 1 and house 3
Since you have bought all the roads connecting the houses, you will end up owning all three houses.
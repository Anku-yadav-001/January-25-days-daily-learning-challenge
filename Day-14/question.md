## Best Time to Buy and Sell Stock II

## Problem Description
You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `ith` day.   

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

## Input Description
- The input consists of multiple test cases.
- The first line contains an integer `t` - the number of test cases.
- The next 2*t lines contain the description of the test cases.
- The first line of each test case contains an integer `n` - the size of the price array.
- The second line of each test case contains `n` space-separated integers denoting the `n` elements of the price array.

## Output
For each test case, output the maximum profit you can achieve.

## Constraints
- `1 <= t <= 10^3`
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Example 
### Input 
- `3`
- `6`
- `7 1 5 3 6 4`
- `5`
- `1 2 3 4 5`
- `5`
- `7 6 4 3 1`

### Output 
`7`
`4`
`0`


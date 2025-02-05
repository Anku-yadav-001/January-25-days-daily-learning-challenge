## Wood Cutter

## Problem Description
Lumberjack Bob needs to chop down M meters of wood. However, Bob is only allowed to cut a single row of trees.

Bob's machine works as follows: Bob sets a height parameter H (in meters), and the machine raises a giant sawblade to that height and cuts off all tree parts higher than H (of course, trees not higher than H meters remain intact). Bob then takes the parts that were cut off.   

For example, if the tree row contains trees with heights of 20, 15, 10, and 17 meters, and Bob raises his sawblade to 15 meters, the remaining tree heights after cutting will be 15, 15, 10, and 15 meters, respectively, while Bob will take 5 meters off the first tree and 2 meters off the fourth tree (7 meters of wood in total).   

Bob is ecologically minded, so he doesn't want to cut off more wood than necessary. That's why he wants to set his sawblade as high as possible. Help Bob find the maximum integer height of the sawblade that still allows him to cut off at least M meters of wood

## Input Description
The first line of input contains two space-separated positive integers, N (the number of trees) and M (Bob's required wood amount).

The second line of input contains N space-separated positive integers less than 1,000,000,000, the heights of each tree (in meters). The sum of all heights will exceed M, thus Bob will always be able to obtain the required amount of wood.

## Output
- The first and only line of output must contain the required height setting.

## Constraints
- `1 ≤ N ≤ 1,000,000`
- `1 ≤ M ≤ 2,000,000,000`

## Example 
### Input 
- `4 7`
- `20 15 10 17`

### Output 
`15`


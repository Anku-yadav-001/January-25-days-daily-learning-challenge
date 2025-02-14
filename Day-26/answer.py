from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        @lru_cache(None)
        def dfs(x, y):
            if x == y:
                return True
            if sorted(x) != sorted(y): 
                return False
            
            n = len(x)
            for i in range(1, n):
                if dfs(x[:i], y[:i]) and dfs(x[i:], y[i:]):
                    return True
                if dfs(x[:i], y[-i:]) and dfs(x[i:], y[:-i]):
                    return True
            return False
        
        return dfs(s1, s2)

s1 = "great"
s2 = "rgeat"

sol = Solution()
print(sol.isScramble(s1, s2))

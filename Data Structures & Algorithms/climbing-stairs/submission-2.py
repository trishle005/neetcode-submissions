class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def step(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = step(i+1) + step(i+2)
            return memo[i]
            
        return step(0)    
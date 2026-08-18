class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        c = len(coins)
        dp = [[0]*(amount+1) for _ in range(c+1)]
        for i in range(c):
            dp[i][0] = 1
        for j in range(c-1, -1, -1):
            for i in range(1, amount+1):
                if i>=coins[j]:
                    dp[j][i]+=dp[j][i-coins[j]]
                dp[j][i]+=dp[j+1][i]
        return dp[0][amount]
        
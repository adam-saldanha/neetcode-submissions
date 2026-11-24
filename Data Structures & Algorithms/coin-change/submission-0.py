class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(amount):
            if amount == 0:
                return 0

            if amount in cache:
                return cache[amount]


            minimum = 1e9
            for coin in coins:
                if (amount - coin) >= 0:
                    minimum = min(minimum, 1 + dfs(amount - coin))

            cache[amount] = minimum
            return minimum

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins

        
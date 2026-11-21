class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0, 0]

        for n in nums:
            temp = max(n + cache[0], cache[1])
            cache[0] = cache[1]
            cache[1] = temp

        return cache[1]
        
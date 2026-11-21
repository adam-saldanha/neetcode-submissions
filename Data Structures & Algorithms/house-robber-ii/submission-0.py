class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            cache = [0, 0]

            for i in range(len(nums)):
                temp = max(cache[0] + nums[i], cache[1])
                cache[0] = cache[1]
                cache[1] = temp
            return cache[1]

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

        
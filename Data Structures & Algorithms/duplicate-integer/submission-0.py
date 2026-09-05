class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if not(i in d):
                d[i] = 1
            else:
                return True
        return False
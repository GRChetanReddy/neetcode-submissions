class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        gm = 0
        m, n = nums[0], nums[0]
        for i in range(1, len(nums)):
            mi = m
            m = max(nums[i], m*nums[i], n*nums[i])
            n = min(nums[i], mi*nums[i], n*nums[i])
            gm = max(m, gm)
        return gm
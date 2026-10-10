class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpn = [0]*len(nums)
        dpm = [0]*len(nums)
        dpm[0], dpn[0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dpm[i] = max(nums[i], dpm[i-1]*nums[i], dpn[i-1]*nums[i])
            dpn[i] = min(nums[i], dpm[i-1]*nums[i], dpn[i-1]*nums[i])
        return max(dpm)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        lis = [1]*l
        for i in range(1, l):
            for j in range(i):
                if nums[i]>nums[j]:
                    lis[i] = max(lis[i], lis[j]+1)
        return max(lis)
        
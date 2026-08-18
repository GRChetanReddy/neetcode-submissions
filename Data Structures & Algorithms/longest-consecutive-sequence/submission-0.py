class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        l = 0
        for num in nums:
            if num-1 not in n:
                c = 0
                curr = num
                while curr in n:
                    curr+=1
                    c+=1
                l = max(l, c)
        return l
        
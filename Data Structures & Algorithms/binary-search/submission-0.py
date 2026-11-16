class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            k = (l+r)//2
            if nums[k]>target:
                r = k-1
            elif nums[k]<target:
                l = k+1
            else:
                return k
        return -1
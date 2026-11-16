class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l<=r:
            k = (l+r)//2
            if nums[k]==target:
                return True
            if nums[l]==nums[k]==nums[r]:
                l+=1
                r-=1
            elif nums[l]<=nums[k]:
                if nums[l]<=target<nums[k]:
                    r = k-1
                else:
                    l = k+1
            else:
                if nums[k]<target<=nums[r]:
                    l = k+1
                else:
                    r = k-1
        return False
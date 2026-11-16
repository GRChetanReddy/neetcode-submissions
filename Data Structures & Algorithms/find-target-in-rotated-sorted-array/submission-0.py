class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            k = (l+r)//2
            if nums[k]>nums[r]:
                l = k+1
            else:
                r = k

        def bs(arr):
            l, r = 0, len(arr)-1
            while l<=r:
                k = (l+r)//2
                if arr[k]>target:
                    r = k-1
                elif arr[k]<target:
                    l = k+1
                else:
                    return k
            return -1
        
        x, y = bs(nums[:l]), bs(nums[l:])
        if x!=-1:
            return x
        elif y!=-1:
            return l+y
        return -1

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(cur, i, target):
            if target<0:
                return
            if target==0 and cur not in res:
                res.append(cur.copy())
                return
            for j in range(i, len(nums)):
                cur.append(nums[j])
                dfs(cur, j, target-nums[j])
                cur.pop()
            return
        dfs([], 0, target)
        return res
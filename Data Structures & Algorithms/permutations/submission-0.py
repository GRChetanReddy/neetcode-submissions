class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(cur):
            if len(cur)==len(nums):
                res.append(cur.copy())
                return
            for i in nums:
                if i not in cur:
                    cur.append(i)
                    dfs(cur)
                    cur.pop()
            return

        dfs([])
        return res
        
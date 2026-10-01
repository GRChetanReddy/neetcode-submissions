# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(cur, i):
            if not cur:
                return 
            if i>=len(res):
                res.append(cur.val)
            dfs(cur.right, i+1)
            dfs(cur.left, i+1)
            return
        dfs(root, 0)
        return res
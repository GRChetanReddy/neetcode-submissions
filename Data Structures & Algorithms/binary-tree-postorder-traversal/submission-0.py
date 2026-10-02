# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            dfs(cur.right)
            res.append(cur.val)
            return
        dfs(root)
        return res
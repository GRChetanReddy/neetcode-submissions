# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(cur):
            if not cur:
                return
            res.append(cur.val)
            dfs(cur.left)
            dfs(cur.right)
            return
        dfs(root)
        return res
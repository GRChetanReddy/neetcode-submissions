# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.p = p
        self.q = q
        def dfs(cur):
            if not cur:
                return None
            if cur==self.p or cur==self.q:
                return cur
            l = dfs(cur.left)
            r = dfs(cur.right)
            if l and r:
                return cur
            return l if l else r
        return dfs(root)        
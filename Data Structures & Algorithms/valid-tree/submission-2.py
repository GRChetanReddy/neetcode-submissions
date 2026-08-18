class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)<n-1:
            return False
        p = [i for i in range(n)]
        def find(x):
            if p[x]!=x:
                return find(p[x])
            else:
                return x
        def union(x, y):
            p[find(y)]=find(x)
        for x, y in edges:
            if p[find(y)]==find(x):
                return False
            else:
                union(x, y)
        return True
        
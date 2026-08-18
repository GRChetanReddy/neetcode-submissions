class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = [i for i in range(n)]
        def find(x):
            if p[x]!=x:
                return find(p[x])
            else:
                return x
        def union(x, y):
            p[find(y)]=find(x)
        for x, y in edges:
            union(x, y)
        unique = set()
        for i in p:
            x = find(i)
            if x not in unique:
                unique.add(x)
        return len(unique)

        
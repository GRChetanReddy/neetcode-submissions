class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        vals = sorted(d.keys(), key = lambda x:d[x])
        return vals[-k:]
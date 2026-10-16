from collections import deque
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        dq = deque()
        for i in nums:
            dq.append([i])
        while len(dq)>1:
            temp = []
            m = dq.popleft()
            n = dq.popleft()
            i, j = 0, 0
            while i<len(m) and j<len(n):
                if m[i]>n[j]:
                    temp.append(n[j])
                    j+=1
                else:
                    temp.append(m[i])
                    i+=1
            while i<len(m):
                temp.append(m[i])
                i+=1
            while j<len(n):
                temp.append(n[j])
                j+=1
            dq.append(temp)
        return dq.pop()
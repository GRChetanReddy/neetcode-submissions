class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        l = len(nums)
        pref = [1]
        sufx = [1]
        for i in range(1, l):
            pref.append(pref[i-1]*nums[i-1])
        for i in range(l-1, 0, -1):
            sufx.append(sufx[l-i-1]*nums[i])
        for i in range(l):
            answer.append(pref[i]*sufx[l-i-1])
        return answer
        
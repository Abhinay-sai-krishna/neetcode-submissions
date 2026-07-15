class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        for i in range(len(nums)-k+1):
            m=nums[i]
            for j in range(i,i+k):
                m=max(m,nums[j])
            ans.append(m)
        return ans    

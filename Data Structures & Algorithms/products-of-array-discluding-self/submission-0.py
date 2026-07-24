class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums) #[1,1,1,1]

        prefix=1
        for i in range(len(nums)):
            res[i]=prefix #[1, 1, 2, 8]
            prefix*=nums[i]
        
        postfix=1
        n=len(nums) #4
        for i in range(n-1,-1,-1): #range 3, -1, -1
            res[i]*=postfix
            postfix*=nums[i]
        
        return res    

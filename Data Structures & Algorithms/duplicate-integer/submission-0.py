class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #solved by sets
        s=set()
        for i in nums:
            if i in s:
                return True
            
            else:
                s.add(i)

        return False 


    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                return True
            
        return False'''

    
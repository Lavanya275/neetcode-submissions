class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        l=0
        max_length=0
        for i in nums:
            s.add(i)
        current=0
        for i in s:
            if i-1 not in s:
                current = i 
                l = 1
                while current+1 in s:
                    current+=1
                    l+=1
            max_length=max(l, max_length)

        return max_length
        '''
        nums.sort()
        max_length=0
        length=1
        
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            elif nums[i]+1!=nums[i+1]:
                max_length=max(max_length, length)
                length=1
            else:
                length+=1
        max_length=max(max_length, length)
        return max_length
            '''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
                continue

        return False
                
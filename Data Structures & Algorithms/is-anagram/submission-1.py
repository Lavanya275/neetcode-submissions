class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #TC: O(n); SC: O(n * log n)
        d1={}
        d2={}
        for i in s:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        
        for i in t:
            if i not in d2:
                d2[i]=1
            else:
                d2[i]+=1

        if sorted(d1.items())==sorted(d2.items()):
            return True
        else:
            return False
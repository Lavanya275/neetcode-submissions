class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={n1: 0 for n1 in range(26)}
        d2={n2: 0 for n2 in range(26)}
        for i in s:
            d1[ord(i)-ord('a')]+=1
        for j in t:
            d2[ord(j)-ord('a')]+=1
        
        if d1==d2:
            return True
        else:
            return False


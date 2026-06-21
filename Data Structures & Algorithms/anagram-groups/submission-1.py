class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs: #n
            s="".join(sorted(i)) #logn
            if s in d:
                d[s].append(i)
            
            else:
                d[s]=[i]
        l=[]
        for i,j in d.items(): 
            l.append(j)

        return l
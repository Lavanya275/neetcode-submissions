class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            i_new="".join(sorted(i))
            if i_new in d:
                d[i_new].append(i)
            else:
                d[i_new]=[i]
        return list(d.values())
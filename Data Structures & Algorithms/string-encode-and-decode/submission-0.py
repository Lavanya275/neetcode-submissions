class Solution:

    def encode(self, strs: List[str]) -> str:
        d=""
        for i in strs:
            l=str(len(i))
            d+=l+"#"+i
        return d
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            end=j+1+length
            res.append(s[j+1:end]) #3#cat 
            i = end

        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        arr=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for num, count in d.items():
            arr.append([count, num])
        arr.sort()
        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return(res)
        
        
        

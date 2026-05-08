class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort 
        d={}
        res=[]
        freq = [ [] for i in range(len(nums)+1)]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        for num, count in d.items():
            freq[count].append(num)
        
        for j in range(len(freq)-1,-1, -1): #freq len 8 -> can't start with index 8 .. index be 7
            for i in freq[j]:
                res.append(i)
                if len(res)==k:
                    return res

        
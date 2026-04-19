class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force approach
        cnt = {}
        for n in nums:
            cnt[n] =1+cnt.get(n, 0)

        pairs = []
        for num, freq in cnt.items():
            # putting freq first bcz sortng fxn looks at frst element by default
            pairs.append([freq, num]) 

        # implicit, sort will order by freq(first element by deafult without lambda)
        pairs.sort(reverse=True)  

        res=[]
        for i in range(k):
            res.append(pairs[i][1])
        
        return res

        
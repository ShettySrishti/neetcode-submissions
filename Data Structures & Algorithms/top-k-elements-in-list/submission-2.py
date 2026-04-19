class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # cnt = {}
        # for n in nums:
        #     cnt[n] =1+cnt.get(n, 0)
        
        # optimal approach (bucket sort)
        cnt = Counter(nums)

        # creating list of empty lists, idx representing counts
        freq = [[] for _ in range(len(nums)+1)]

        for n,c in cnt.items():
            freq[c].append(n)
        
        res=[]
        for i in range(len(freq)-1, 0, -1): # we need top ones so start from highest freq(idx)
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

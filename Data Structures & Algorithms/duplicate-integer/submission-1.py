class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return len(nums) != len(set(nums))   
        from collections import Counter
        cnt = Counter(nums) 

        for num in nums:
            if cnt[num] >1:
                return True
        return False
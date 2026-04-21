class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force approach 

        n = len(nums)
        res=[1]*n

        for i in range(n):
            pdt =1
            for j in range(n):
                if i!=j:
                    pdt *= nums[j]


            res[i] = pdt

        return res


        
        
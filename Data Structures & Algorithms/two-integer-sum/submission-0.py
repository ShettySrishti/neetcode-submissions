class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}

        for i, n in enumerate(nums):
            diff = target-n
            if diff in dict:
                return [dict[diff], i] # returns smaller idx, current idx
            dict[n] = i # storing curr num as key and idx as value for lookup

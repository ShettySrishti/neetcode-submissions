class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # best solution, avoids interating thru entire list.
        # return True immediately as soon as it encounters duplicate.

        seen = set()
        for n in nums:
            if n in seen:
                return True # found duplicate, stops without scanning rest of the nums
            seen.add(n)
        return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams cant have different lengths
        if len(s) !=len(t):
            return False

        # initializing array of 26 0's(a-z lowercase)
        cnt = [0]*26 

        for i in range(len(s)):
            # ord converts char into its ascII value
            cnt[ord(s[i])-ord('a')] += 1
            cnt[ord(t[i]) -ord('a')] -= 1

        for val in cnt:
            if val !=0:
                return False
        return True
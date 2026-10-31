class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Brute Force approach
        res = []

        for char in s:
            if char.isalnum():
                res.append(char.lower())

        res  = ''.join(res)

        return res == res[::-1]


        
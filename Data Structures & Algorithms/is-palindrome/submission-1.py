class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1


        while left < right: # # Keep checking pairs until pointers meet
            while left < right and not s[left].isalnum():  # clean left side
                left += 1
            while left < right and not s[right].isalnum(): # clean right side
                right -= 1

            if s[left].lower() != s[right].lower(): # compare
                return False # mismatch found -> Not Palindrome.

            # if same : move both pointers inward and check next pair
            left += 1
            right -=1

        return True

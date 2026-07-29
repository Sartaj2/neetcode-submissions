class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # Move left pointer to the next alphanumeric character
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Move right pointer to the previous alphanumeric character
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # Compare characters ignoring case
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True    

    def alphaNum(self, c):
        # Check if a character is alphanumeric
        return c.isalnum()

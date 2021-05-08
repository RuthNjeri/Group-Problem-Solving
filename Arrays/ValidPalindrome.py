class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # remove non-alpha numeric characters from string
        s = ''.join(e for e in s if e.isalnum())

        if s == '' or len(s) == 1:
            return True
        
        # convert to lower case
        s = s.lower()
        
        # check if string is equal to its reverse
        return s == s[::-1]
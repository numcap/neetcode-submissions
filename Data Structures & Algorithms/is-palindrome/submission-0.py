class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        we need to find the a valid Palindrome excluding any none alphanumeric 
        character using a 2 pointer appraoch
        
        solution: we can have a pointer on each side of the string and check
        if they equal each other continue, if its a none alphanumeric char
        skip
        """

        L = 0
        R = len(s) - 1

        while L <= R:
            if not s[L].isalnum():
                L += 1
                continue
                
            if not s[R].isalnum():
                R -= 1
                continue

            if s[R].capitalize() == s[L].capitalize():
                R -= 1
                L += 1
                continue
            else:
                return False

        return True
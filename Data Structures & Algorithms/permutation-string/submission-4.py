class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_sorted = sorted(list(s1))

        l, r = 0, len(s1)

        while r <= len(s2):
            temp = sorted(list(s2[l:r]))
            if temp == s1_sorted:
                return True
            l += 1
            r += 1
        return False
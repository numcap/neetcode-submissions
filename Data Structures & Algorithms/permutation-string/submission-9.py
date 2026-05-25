class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_count = {}

        for s in s1:
            s1_count[s] = s1_count.get(s, 0) + 1

        l, r = 0, len(s1)

        while r <= len(s2):
            s2_count = {}
            for s in s2[l:r]:
                s2_count[s] = s2_count.get(s, 0) + 1
            if s1_count == s2_count:
                return True
            l += 1
            r += 1
        return False
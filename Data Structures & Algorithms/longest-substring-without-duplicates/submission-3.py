class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        problem: we want to find the longest substring without repeated characters
        
        potential solution: we can do a sliding door solution where we can create
        left and right pointers and set the left pointer to when we see a new character
        and the right pointer to go through the string until we get to a seen character
        we can use a array to store what we have seen
        """

        # l = r = 0
        # seen = set()
        # longest = 0

        # if len(s) == 0:
        #     return 0
        # elif len(s) == 1:
        #     return 1

        # while l <= r:
        #     if l == r:
        #         seen.add(s[l])
        #         r += 1
        #         longest = max(longest, len(seen))
        #         continue
        #     elif r >= len(s):
        #         break
            
        #     if s[r] not in seen:
        #         seen.add(s[r])
        #         r+=1
        #     else:
        #         seen.discard(s[l])
        #         l += 1
        #     longest = max(longest, len(seen))
        
        # return longest

        seen = {}
        l = 0
        longest = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest
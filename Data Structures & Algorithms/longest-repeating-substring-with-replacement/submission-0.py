class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # """
        # problem: we have k replacements we need to return the longest substring after
        # k replacements are done

        # potential solution: i am thinking that we chould use a map to store everytime
        # we come across a new character, when we come across a new character we can
        # check if the gap between the 2 same characters are less than or equal to k
        # then we can use save that as the longest
        # """

        # l = r = 0
        # longest = 0
        # seen = [(s[l], 0)]
        # # temp_k = k

        # while r < len(s):
        #     if s[l] == s[r]:
        #         longest = max(longest, l - r + 1)
        #     else:
        #         cont = False
        #         for i in range(k):
        #             print(r - l + 1 + i)
        #             longest = max(longest, r - l + 1 + i)
        #             if (s[r], r) not in seen:
        #                 seen.append((s[r], r))
        #             if r + i + 1 < len(s) and s[r + i + 1] == s[l]:
        #                 r = r + i + 1
        #                 cont = True
        #                 break
        #         if not cont:
        #             l = seen[seen.index((s[l], l)) + 1][-1]
        #             r = l + 1
        #     r += 1

        # return longest

        count = {}
        l = 0
        max_freq = 0
        longest = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest
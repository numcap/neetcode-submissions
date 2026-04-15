class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_in_t = {}
        seen_in_s = {}

        for s_letter in s:
            seen_in_s[s_letter] = seen_in_s.get(s_letter, 0) + 1
        for t_letter in t:
            seen_in_t[t_letter] = seen_in_t.get(t_letter, 0) + 1

        return seen_in_t == seen_in_s
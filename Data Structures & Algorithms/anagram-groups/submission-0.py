class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        so we need to check if these are proper anagrams, which we can do 
        by counting how many letters in each string

        we need to go through all the strings count then add same ones to array
        that would be costly tho

        we can try to use the ascii of the leters byt how would that work
        - we take a array fuilled with 26 zeros, then we add 1 everytime we get 
            a letter by subtracting the ASCII value of the letter by a's ASCII 
            value, this lets us have uniform lists that i can use as keys in 
            order to append a new value (the string) onto the tuple of the array, 
            then take the values of all of them
        """

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # so this is an array of 0
            for c in s:
                count[ord(c) - ord("a")] += 1 # we add a 1 everytime 
            res[tuple(count)].append(s)
        return list(res.values())
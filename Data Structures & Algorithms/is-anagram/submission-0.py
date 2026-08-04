class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = []
        letters_t = []

        for letter in s:
            letters_s.append(letter)
        for letter in t:
            letters_t.append(letter)
        letters_s.sort()
        letters_t.sort()
        if letters_s == letters_t:
            return True
        else:
            return False
        

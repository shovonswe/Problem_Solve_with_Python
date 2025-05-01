class Solution:
    def wordPattern(self, pattern, s):
        word = s.split()
        if len(word) != len(pattern):
            return False
        char_to_word = {}
        word_to_char = {}
        for c,w in zip(pattern,word):
            if c in char_to_word and char_to_word[c] != w:
                return False
            if w in word_to_char and word_to_char[w] != c:
                return False
            char_to_word[c] = w
            word_to_char[w] = c
        return True    

Solution = Solution()
pattern = "abba"
s = "dog cat cat dog"
print(Solution.wordPattern(pattern,s))

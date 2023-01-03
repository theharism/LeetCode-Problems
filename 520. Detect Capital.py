class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        match1,match2,match3 = True,True,True

        len_word = len(word)
        if len_word < 1 or len_word > 100:
            return False
        
        count = 0

        if word[0].isupper():
            for l in range(1,len_word):
                if not word[l].islower():
                    match1 = False
                    break
            if match1:
                return True
        
        count = 0

        for l in word:
            if l.isupper():
                match2 = False
                break
        if match2:
                return True

        count = 0
        for l in word:
            if l.islower():
                match3 = False
                break
        if match3:
                return True
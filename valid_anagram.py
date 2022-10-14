class Solution:
    def isAnagram(self, s,t):
        
        if len(s) == len(t):
            saved_letters = {}
            for letter in s:
                if letter not in saved_letters.keys():
                    saved_letters[letter] = 1
                else:
                    saved_letters[letter] +=1
            
            for letter in t:
                if letter in saved_letters.keys():
                    saved_letters[letter] -= 1
                else:
                    return False
            
            for value in saved_letters.values():
                if value != 0:
                    return False 
            
            return True

        return False



s = "anagram"
t = "nagaram"

S = Solution()
print(S.isAnagram(s,t))
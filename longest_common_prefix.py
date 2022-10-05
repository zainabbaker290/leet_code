class Solution(object):
    def longestCommonPrefix(self, strs):
        common_string = ""
        base_word = 0
        #to make sure index is never out of range 
        if len(strs[base_word]) < len(strs[base_word + 1]):
            length = len(strs[base_word])
        else:
           length = len(strs[base_word + 1]) 

        j = len(strs) -1 
        while j > 0:
            for i in range(length): 
                if strs[base_word][i] == strs[base_word + 1][i]: #comparing the base word to the word after
                    common_string += strs[base_word][i]
            if common_string != "" and j != 1:
                common_string = "" #resetting common word 
                base_word += 1 
                j -= 1 
            elif common_string != "":
                return common_string
            else:
                return "none"
        return common_string

#issue
#i know how to fix the issue in my head but not with code
#i need to reset the base word to be the common word
#but im not too sure how to do this


S = Solution()
print(S.longestCommonPrefix(["flower","flowx","fligxht"]))
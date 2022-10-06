class Solution(object):
    def longestCommonPrefix(self, strs):
        common_string = ""
        base_word = strs[0]
        i = 0
        list_pos = 1

        if len(strs) == 1:
            return base_word
        
        #list pos is 0????? 
        for list_pos in range(len(strs)):
            if len(base_word) < len(strs[list_pos]):
                length = len(base_word)
            else:
                length = len(strs[list_pos]) 
            for i in range(length):
                if base_word[i] == strs[list_pos][i]:
                    common_string += base_word[i]
                else:
                    break
            
            if strs[list_pos] != strs[-1]:
                base_word = common_string
                common_string = ""
            else:
                return common_string

        return base_word

S = Solution()
print(S.longestCommonPrefix(["aaa","aa", "aaa"]))
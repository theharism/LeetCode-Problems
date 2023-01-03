class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s_list = s.split(' ')
        dic = dict()
        new_list = []
        k = 0

        if len(pattern) != len(s_list):
            return False 

        for i in s_list:
            if dic.get(pattern[k]) != None:
                vaal = dic[pattern[k]]
                if vaal != i:
                    return False
            else:
                if i in new_list:
                    return False
                dic[pattern[k]] = i
                new_list.append(i)
            k = k + 1
        
        return True
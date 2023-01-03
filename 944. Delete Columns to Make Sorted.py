class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        n = len(strs)

        if n < 1 or n > 1000:
            return 0
        
        strs_n = len(strs[0])

        count = 0
        
        for i in range(strs_n):
            for j in range(n - 1):
                if strs[j][i] > strs[j+1][i]:
                    count += 1
                    break

        return count
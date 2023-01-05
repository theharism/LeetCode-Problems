import numpy as np

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)

        if n < 1 or n > 10**5:
            return -1

        if n == 1:
            return 1

        points.sort(key = lambda x: x[1])

        count = 1

        endpoint = points[0][1]

        for i in range(1,len(points)):
            if points[i][0] > endpoint:
                count += 1
                endpoint = points[i][1] 

        return count





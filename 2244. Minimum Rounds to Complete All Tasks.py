class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        # """
        n = len(tasks)

        if n < 1 or n > 10**9:
            return -1

        counts = {}

        for i in tasks:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        count = 0

        for key in counts:
            value= counts[key]
            if value < 2:
                return -1
            elif value % 3 == 0:
                count += value / 3
            elif value == 2 or value == 4:              
                 count += value / 2
            elif (value % 3) % 2 != 0:
                    divisor = (value / 3) - 1
                    count += divisor + (value - (divisor * 3)) / 2
            else:
                    count += value / 3
                    count += (value % 3) / 2


        return count
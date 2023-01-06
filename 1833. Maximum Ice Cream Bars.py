class Solution(object):
    def maxIceCream(self, costs, coins):

        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """

        n = len(costs)

        if n < 1 or n > 10**5:
            return 0

        if coins < 1 or coins > 10**8:
            return 0

        costs.sort()

        count = 0

        spent = 0

        for cost in costs:
            if cost < 0 or cost > 10**5:
                return 0
            if spent + cost <= coins:
                count += 1
                spent += cost
            else:
                break

        return count

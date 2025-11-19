'''
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n ==0:
            return 1
        return x**n
        
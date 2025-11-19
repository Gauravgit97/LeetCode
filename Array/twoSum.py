'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

#Most easy approch O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            find = target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==find:
                    return [i,j]
                

# good approch time->O(N) and space-> O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in dic:
                return [i,dic[remain]]
            dic[nums[i]] = i
# Problem: Two Sum (LeetCode - Easy)
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Tags: Array, Hash Table
# Description:
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return []

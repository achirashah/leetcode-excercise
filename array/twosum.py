# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists

# two pointer, array
from typing import List


nums = [2,8,11,15,0,9,8]
target = 9
#Output: [0,1]

def twosum(nums, target):
    for i in range(len(nums)):
        print("i = ", i)
        for j in range(i+1, len(nums)):
            print("j = ", j)
            sum = nums[i] + nums[j]
            print("i:",nums[i], "j:",nums[j]," = ",sum )
            if sum == target:
                return [i,j]

# print(twosum(nums, target))

# Time complexity - O(O^2)
# Space complexity - O(1)
 
# list
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            print(i)
            print(value)
            print(nums)
            remaining = target - nums[i]
            if remaining in seen:
                return[seen[remaining],i]
            seen[value] = i    

print(Solution.twoSum(Solution(), nums, target))

# Time complexity - O(n)
# Space complexity - O(n)

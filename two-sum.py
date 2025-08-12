#Problem: Two Sum
"""
Two Sum Problem
---------------
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the
same element twice. You can return the answer in any order.

Example:
--------
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] == 9

Constraints:
------------
- 2 <= nums.length <= 10^4
- -10**9 <= nums[i] <= 10**9
- -10**9 <= target <= 10**9
- Only one valid answer exists.
"""

#Solution

class Solution(object):
    def twoSum(self, nums, target):
        """
        Finds indices of the two numbers in the list that add up to the target.

        :param nums: List[int] - List of integers
        :param target: int - Target sum
        :return: List[int] - Indices of the two numbers
        """
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i


if __name__ == "__main__":
    # Example usage
    solution = Solution()

    # Test cases
    print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(solution.twoSum([3, 2, 4], 6))      # Output: [1, 2]
    print(solution.twoSum([3, 3], 6))         # Output: [0, 1]

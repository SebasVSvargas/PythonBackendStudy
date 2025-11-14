
""" Problem Statement:
Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. """


from typing import List

nums = [3,2,4]
target = 6

# Solution 1: Brute Force Approach   Complexity O(n^2) because of nested loops
def two_index_of_sum(nums: list[int], target: int) -> list[int] :

    for i in range(len(nums)):
        num1 = nums[i]
        if i+1 < len(nums):
            for j in range(i+1, len(nums)) :
                num2 = nums[j]
                if num1 + num2 == target :
                    return [i, j]
        else:
            return []
        

result = two_index_of_sum(nums, target)
print(f"The index of two values that add up to target are: {result}")
print(f"num1: {nums[result[0]]} + num2: {nums[result[1]]} = {target}")


# [BEST] Solution 2: Using Hash Map  Complexity O(n) Because of single loop
def two_index_of_sum_hashmap(nums: List[int], target: int) -> List[int]:
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []

result = two_index_of_sum_hashmap(nums, target)
print(f"The index of two values that add up to target are: {result}")
print(f"num1: {nums[result[0]]} + num2: {nums[result[1]]} = {target}")


# Solution 3: Sorting and using binary search  Complexity O(n log n) + O(log n) because of sorting and binary search in which eliminates half of the array in each iteration
def two_index_of_sum_sorting(nums: List[int], target: int) -> List[int]:
    indexed_nums = list(enumerate(nums))
    indexed_nums.sort(key=lambda x: x[1])
    
    left, right = 0, len(indexed_nums) - 1
    
    while left < right:
        current_sum = indexed_nums[left][1] + indexed_nums[right][1]
        if current_sum == target:
            return [indexed_nums[left][0], indexed_nums[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return []
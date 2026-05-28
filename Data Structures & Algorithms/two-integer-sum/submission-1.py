class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reverse = []
        for i, num in enumerate(nums):
            a = target - num
            if a in nums and nums.index(a) != i:
                reverse.append(i)
                reverse.append(nums.index(a))
                return sorted(reverse)
            
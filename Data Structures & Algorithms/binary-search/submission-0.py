class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            first = 0
            last = len(nums) - 1
            while last >= first:
                mid = (first + last) // 2
                if nums[mid] == target:
                    return mid
                else:
                     if target < nums[mid]:
                         last = mid - 1
                     else:
                         first = mid + 1
            return False
        else:
            return -1
        
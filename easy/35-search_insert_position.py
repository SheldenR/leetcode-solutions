class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] >= target:
                return i
            else:
                i += 1

        return len(nums)

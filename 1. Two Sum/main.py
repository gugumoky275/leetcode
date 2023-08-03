class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        candidates = {}
        for idx, num in enumerate(nums):
            counterpart = target - num
            if counterpart in candidates:
                return [candidates[counterpart], idx]
            candidates[num] = idx

        return [None, None]
                
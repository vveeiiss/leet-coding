class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i in nums:
                if i == target:
                    return nums.index(i)
        else:
            return -1
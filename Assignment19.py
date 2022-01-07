from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums, start, end):
            while (start < end):
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)

        print(nums)

Solution().rotate([1,2,3,4,5,6,7], 3)
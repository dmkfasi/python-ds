class Solution:
  def sortColors(self, nums):
    # Fill this in.

    # Array length
    # high, low and mid pointers
    high = len(nums) - 1
    low, mid = 0, 0

    while mid <= high:
      if (0 == nums[mid]):
        t = nums[low]
        nums[low] = nums[mid]
        nums[mid] = t
        low = low + 1
        mid = mid + 1
      if (1 == nums[mid]):
        mid = mid + 1
      if (2 == nums[mid]):
        if mid > high:
          continue
        t = nums[mid]
        nums[mid] = nums[high]
        nums[high] = t
        high = high - 1
      print(low, mid, high, nums)

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
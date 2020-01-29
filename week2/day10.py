class Solution(object):
  def threeSum(self, nums):
    # Fill this in.

    # There is no sum to form zero
    if min(nums) >= 0:
      return False

    # Output buffer
    zeroSum = []

    # Sorting for O(n2) solution
    nums.sort()
    length = len(nums)

    for i in range(length - 2):
      l = i + 1
      r = length - 1
      while (l < r):
        tripletSum = nums[i] + nums[l] + nums[r]
        if tripletSum == 0:
          zeroSum.append([ nums[i], nums[l], nums[r] ])
          l += 1
          r -= 1
        if tripletSum < 0:
          l += 1
        if tripletSum > 0:
          r -= 1

    return zeroSum

# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]

nums = [0, -1, 2, -3, 1]
print(Solution().threeSum(nums))
# [0, -1, 1], [2, -3, 1]
class Solution:
  def moveZeros(self, nums):
    # Fill this in.
			cnt = 0

			for num in nums:
				if num is 0:
					nums.remove(0)
					cnt = cnt + 1

			for z in range(cnt):
				nums.append(0)

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]


def witnesses(heights):
  # Fill this in.

	# Assume the first person in line is the tallest one
	m = heights[0]

	ql = len(heights)
	mi = 0
	cnt = 0

	# Find actual tallest person
	for i in range(1, ql):
		height = heights[i]

		if height >= m:
			m = height
			mi = i

	# Whenever tallest person is the last in line
	if mi == (ql - 1):
		return 1

	# Get this very person into account
	cnt = cnt + 1

	# Slice people line by the tallest person
	heights = heights[mi + 1:]

	# Dive in to find other tallest people
	cnt = cnt + witnesses(heights)

	return cnt


print(witnesses([7, 2, 1, 7, 6, 3, 4, 6]))
# 2

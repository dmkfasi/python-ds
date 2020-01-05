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

	# Shift line one person below
	mi = mi + 1
	# Assume the second tallest person
	m = heights[mi]

	# Find any person shorter than this one
	for i in range(mi, ql):
		height = heights[i]

		# Anyone shorter can see from here
		if height < m:
			cnt = cnt + 1
		# Anyone taller cannot see
		if height > m:
			m = height
			mi = i

	return cnt


print(witnesses([3, 2, 1, 7, 6, 4, 4, 4]))
# 5

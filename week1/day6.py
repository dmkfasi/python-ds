def matrix_spiral_print(M):
  # Fill this in.
	height = len(M)
	width = len(M[0])
	length = width * height

	# Column
	c = 0
	# Row
	r = 0

	# Start column
	sc = 0
	# Start row
	sr = 0

	# Boundary column
	bc = width - 1
	# Boundary row
	br = height - 1

	# Already traversed?
	trav = 0

	# Output accumulator
	acc = []

	for i in range(length):

		acc.append(M[r][c])
		#print(v, '@', r, 'x', c, ' br, bc:', br, bc)

		if r == sr and c < bc:
			c = c + 1
		elif c == bc and r < br:
			r = r + 1
		elif r == br and c > sc:
			c = c - 1
		elif c == sc and r > sr:
			r = r - 1

		if r == br and c == sc:
			sr = sr + 1
			bc = bc - 1
			trav = trav + 1

		if c == bc and r == sr and trav > 0:
			br = br - 1
			sc = sc + 1
			
	print(acc)


#grid = [[1,  2,  3,  4,  5],
#        [6,  7,  8,  9,  10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20]]
#matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12

#grid = [[ 1,  2,  3,  4,  5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14, 15, 16, 17, 18],
#        [19, 20, 21, 22, 23, 24, 25, 26, 27],
#        [28, 29, 30, 31, 32, 33, 34, 35, 36],
#        [37, 38, 39, 40, 41, 42, 43, 44, 45]]

grid = [[ 1,  2,  3,  4,  5],
        [ 6,  7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 25 24 23 22 21 16 11 6 7 8 9 14 19 18 17 12 13


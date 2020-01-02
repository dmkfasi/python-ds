import random

class Solution(object):
	def getRandomDominoes(l):
		random.seed()
		dominoes = ''
		for i in range(l):
			d = random.randint(0, 2)
			# 0 equals dot, 1 equals right, 2 equals left
			if d == 0:
				dominoes += '.'
			if d == 1:
				dominoes += 'R'
			if d == 2:
				dominoes += 'L'

			dominoes += '.'

		return dominoes

	def pushDominoes(self, dominoes):

			l = len(dominoes)
			d = list(dominoes)
			out = []
			vn = ''

			if l < 2:
				return ''.join(dominoes)

			if l == 2:
				if d[0] == 'R':
					dominoes = dominoes.replace('.', 'R')
				if d[1] == 'L':
					dominoes = dominoes.replace('.', 'L')

				return dominoes

			for i, v in enumerate(d):

				if vn is not '':
					val = vn
					out.append(val)
					vn = ''
					continue
				else:
					val = v
					out.append(val)

				if v == 'R':
					vn = v

				if v == 'L':
					if i > 1 and out[i - 2] == 'R':
						out[i - 1] = '.'
					else:
						out[i - 1] = v

					out[i] = v
					continue


			return ''.join(out)

#str = '..R...L..R.'
str = Solution.getRandomDominoes(5)
print(' Input: ' + str)
print('Output: ' + Solution().pushDominoes(str))


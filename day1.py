import random

class Solution(object):
	def getRandomDominoes(l):
		dominoes = ''
		for i in range(l):
			random.seed()
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
			vnext = ''

			if l < 2:
				return ''.join(dominoes)

			for i, v in enumerate(d):

				if vnext is not '':
					val = vnext
					out.append(val)
					vnext = ''
					continue
				else:
					val = v
					out.append(val)

				if v == 'R':
					vnext = v

				if v == 'L':
					if i > 1 and out[i - 2] == 'R':
						out[i - 1] = '.'
					else:
						out[i - 1] = v

					out[i] = v
					continue


			return ''.join(out)

#str = '..R...L..R.'
#str = '.L'
str = Solution.getRandomDominoes(15)
print(' Input: ' + str)
print('Output: ' + Solution().pushDominoes(str))


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def removeConsecutiveSumTo0(node):
  # Fill this in.
	s = 0
	idx = 0
	p_idx = 0
	head = node
	ret = None
	sums = [ node.value ]

	while node is not None:
		v = node.value
		s = s + v

		if s in sums:
			print('pidx: ', p_idx, 'idx: ', idx, 's: ', s, 'v: ', v)
			for i in range(p_idx + 1, idx + 1):
				if head.next is not None:
					head = head.next
					#continue
			ret = Node(head.value)
			ret.next = head.next

			p_idx = idx

		sums.append(s)
		idx = idx + 1
		node = node.next

	return ret


node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
  print(node.value),
  node = node.next
# 10


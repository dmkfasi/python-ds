class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    current_node = self
    result = []
    while current_node:
      result.append(current_node.val)
      current_node = current_node.next
    return str(result)

def remove_kth_from_linked_list(head, k):
  # Fill this in
	node = []
	step = 0
	currhead = head

	while head:
		nexthead = head.next

		if nexthead is not None:
			nextval = nexthead.val
			step = step + 1
			
		if nextval is k:
			#print('Found k, steps so far: ', step)
			for i in range(0, step):
				currval = currhead.val
				node.append(currval)
				#print(' -- currval: ', currval)
				currhead = currhead.next
			step = 0

		head = nexthead

	#print('Outer steps so far: ', step)
	currhead = currhead.next
	for i in range(0, step):
		currval = currhead.val
		node.append(currval)
		#print(' -- outer currval: ', currval)
		currhead = currhead.next

	return node

head = Node(1, Node(2, Node(3, Node(5, Node(4, Node(3, Node(3)))))))
print(head)
# [1, 2, 3, 5, 4, 3, 3]
head = remove_kth_from_linked_list(head, 3)
print(head)
# [1, 2, 3, 5, 4, 3]


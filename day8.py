from collections import deque
import math

class Node:
  def __init__(self, value, left=None, right=None):
      self.value = value
      self.left = left
      self.right = right

  def __str__(self):
    # level-by-level pretty-printer
    nodes = deque([self])
    answer = ''

    while len(nodes):
      node = nodes.popleft()
      if not node:
        continue
      answer += str(node.value)
      nodes.append(node.left)
      nodes.append(node.right)
    return answer


def createBalancedBST(nums):
  # Fill this in.

  # Find the top of the tree which is in the middle of sequence
  treeTop = findTreeTop(nums)
  node = Node(treeTop)

  # Split the sequence by the tree top index
  # and define left and right sub trees from that point
  treeTopIndex = nums.index(treeTop)
  leftSubTree = nums[:treeTopIndex]
  rightSubTree = nums[treeTopIndex + 1:]

  # Find the top of each sub tree then
  if (len(leftSubTree) > 0):
    # Assign left sub tree
    node.left = createBalancedBST(leftSubTree)
  if (len(rightSubTree) > 0):
    # Assign right sub tree
    node.right = createBalancedBST(rightSubTree)

  return node

def findTreeTop(nums):
  firstItem = nums[0]
  lastItem = nums[len(nums) - 1]
  #print(firstItem, lastItem)
  return math.floor((firstItem + lastItem) / 2)
	
print(createBalancedBST([1, 2, 3, 4]))
#2134
print(createBalancedBST([1, 2, 3, 4, 5, 6, 7]))
# 4261357
#   4
#  / \
# 2   6
#/ \ / \
#1 3 5 7

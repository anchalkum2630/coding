class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None
# in this first curr=root, then we start a loop-> if curr is not none then append it then do curr.left if curr is none then print the value then do curr.right 
# if list is empty then break the loop
def inorderTraversal(root):
	l=[]
	curr=root
	if root is None:
		return l
	while True:
		if curr is not None:
			l.append(curr)
			curr=curr.left
		else:
			if len(l) == 0:
				break
			else:
				curr=l.pop()
				print(curr.data,end=" ")
				curr=curr.right
#  Driver Program to test above function
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)

	print("inOrder Traversal of binary tree is -")
	inorderTraversal(root)


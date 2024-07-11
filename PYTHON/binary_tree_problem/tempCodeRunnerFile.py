class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None
def preorderTraversal(root):
	l=[]
	l.append(root)
	while l:
		temp=l.pop()
		print(temp.data)
		if(temp.right!=None):
			l.append(temp.right)
		if(temp.left!=None):
			l.append(temp.left)
# Driver Program to test above function
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)

	print("Level Order Traversal of binary tree is -")
	preorderTraversal(root)


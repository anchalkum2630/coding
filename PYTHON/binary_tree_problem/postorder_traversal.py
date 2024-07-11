class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None
# using two stack
def PostOrder(root):
	l1=[]
	l2=[]
	l1=[root]
	if(root is None):
		return
	else:
		while l1:
			temp=l1.pop()
			l2.append(temp.data)
			if temp.left is not None:
				l1.append(temp.left)
			if temp.right is not None:
				l1.append(temp.right)
	l2.reverse()
	print(l2)

# using one list
			
	
		

# Driver Program to test above function
def post(root):
	if(root is None):
		return
	post(root.left)
	post(root.right)
	print(root.data)
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	print("PostOrder Traversal of binary tree is - ")
# postorderTraversal(root)
PostOrder(root)
print("hello")
post(root)


class BNode:
     
     def __init__(self,val):
     	self.val = val
     	self.size = 1 #how many copies of the value the node is storing (used for dupe handling)
     	self.left = None
     	self.right = None

     def addVal():
     	self.size += 1
     def delVal():
     	self.size -= 1
     	assert self.size > 0, "Node is storing negative values"
     def setLeft(node):
     	self.left = node
     def setRight(node):
     	self.right = node

     def getVal():
     	return self.val
     def getSize():
     	return self.size
     def getLeft():
     	return self.left
     def getRight():
     	return self.right


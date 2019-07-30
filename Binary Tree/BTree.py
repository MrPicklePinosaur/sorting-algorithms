from BNode import *

class BTree:

     def __init__(self):
     	self.root = None

     def add(val):
     	if self.root == None: #if the tree is empty, the new node becomes the root
     		self.root = BNode(val)
     		return
     	add(self.root,val) #Otherwise start traversing tree
     def add(curNode,val):
     	if val < curNode.getVal(): #smaller values are stored to the left
     		if curNode.getLeft() != None: #if we can still travel left
     			add(curNode.getLeft(),val)
     		else: #otherwise we create a new left child node
     			curNode.setLeft(BNode(val))
     	elif val > curNode.getVal():
     		if curNode.geRight() != None:
     			add(curNode.getRight(),val)
     		else:
     			curNode.setRight(BNode(val))
     	elif val == curNode.getVal(): #Stack values onto node if there is a dupe
     		curNode.addVal()

     def setRoot(node):
     	self.root = node

     def getRoot():
     	return self.root

cedar = BTree()
cedar.add(4)

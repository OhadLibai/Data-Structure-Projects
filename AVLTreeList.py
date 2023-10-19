
"""A class represnting a node in an AVL tree"""

class AVLNode(object):

	"""Constructor, you are allowed to add more fields.
	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = None


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	Time Complexity: O(1)
	"""
	def getLeft(self):
		return self.left


	"""returns the right child
	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	Time Complexity: O(1)
	"""
	def getRight(self):
		return self.right


	"""returns the parent 
	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	Time Complexity: O(1)
	"""
	def getParent(self):
		return self.parent


	"""return the value
	@rtype: str
	@returns: the value of self, None if the node is virtual
	Time Complexity: O(1)
	"""
	def getValue(self):
		return self.value


	"""returns the height
	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	Time Complexity: O(1)
	"""
	def getHeight(self):
		return self.height


	"""sets left child
	@type node: AVLNode
	@param node: a node
	Time Complexity: O(1)
	"""
	def setLeft(self, node):
		self.left = node


	"""sets right child
	@type node: AVLNode
	@param node: a node
	Time Complexity: O(1)
	"""
	def setRight(self, node):
		self.right = node


	"""sets parent
	@type node: AVLNode
	@param node: a node
	Time Complexity: O(1)
	"""
	def setParent(self, node):
		self.parent = node


	"""sets value
	@type value: str
	@param value: data
	Time Complexity: O(1)
	"""
	def setValue(self, value):
		self.value = value


	"""sets the height of a node
	@type h: int
	@param h: the height
	Time Complexity: O(1)
	"""
	def setHeight(self, h):
		self.height = h


	"""returns whether self is not a virtual node 
	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	Time Complexity: O(1)
	"""
	def isRealNode(self):
		return (not self.height == -1)


	      ##############################
	###-> Additional Methods For AVLNode <-###
	      ##############################


	"""Time Complexity: O(log(n))"""
	def successor(self):
		if self.right.isRealNode():
			currNode = self.right
			while currNode.left.isRealNode():
				currNode = currNode.left
			return currNode

		else:
			succCand = self
			while (succCand.parent is not None) and (succCand.parent.left is not succCand):
				succCand = succCand.parent
			return succCand.parent


	"""Time Complexity: O(log(n))"""
	def predecessor(self):
		if self.left.isRealNode():
			currNode = self.left
			while currNode.right.isRealNode():
				currNode = currNode.right
			return currNode

		else:
			predCand = self
			while (predCand.parent is not None) and (predCand.parent.right is not predCand):
				predCand = predCand.parent
			return predCand.parent


	"""Time Complexity: O(n)"""
	def inOrderArr(self, sortedArr):
		#base case#
		if not self.isRealNode():
			return sortedArr

		else:
			sortedArr = self.left.inOrderArr(sortedArr)
			sortedArr.append(self.value)
			sortedArr = self.right.inOrderArr(sortedArr)

		return sortedArr


	"""Time Complexity: O(1)"""
	def maintainSizeHeight(self): #self = currNode#
		heightChanges = 0
		heightBefore = self.height
		heightAfter = max(self.left.height,self.right.height) + 1

		if heightBefore != heightAfter:
			heightChanges+=1
		self.height = heightAfter

		self.size = 1
		if self.left.isRealNode():
			self.size+=self.left.size
		if self.right.isRealNode():
			self.size+=self.right.size

		return heightChanges


	"""Time Complexity: O(1)"""
	def leftRotation(self): #self = currNode#
		self.right = self.right.left
		self.right.parent.left = self

		if self.parent is not None:
			if self.parent.left is self:
				self.parent.left = self.right.parent
			else:
				self.parent.right = self.right.parent

		self.right.parent.parent = self.parent
		self.parent = self.right.parent
		self.right.parent = self

		self.maintainSizeHeight()
		self.parent.maintainSizeHeight()


	"""Time Complexity: O(1)"""
	def rightRotation(self):
		self.left = self.left.right
		self.left.parent.right = self

		if self.parent is not None:
			if self.parent.left is self:
				self.parent.left = self.left.parent
			else:
				self.parent.right = self.left.parent

		self.left.parent.parent = self.parent
		self.parent = self.left.parent
		self.left.parent = self

		self.maintainSizeHeight()
		self.parent.maintainSizeHeight()


	"""Time Complexity: O(1)"""
	def rotate(self, BfCurrNode): #self=currNode#
		rotationNum = 0

		if BfCurrNode == -2:	#pulling too much right
			BfRson = self.right.left.height - self.right.right.height
			if (BfRson == -1) or (BfRson==0) :
				self.leftRotation()
				rotationNum += 1
			else:
				self.right.rightRotation() # here the height change should not be added cause its temporary
				self.leftRotation()
				rotationNum += 2

		else:	#pulling too much left
			BfLson = self.left.left.height - self.left.right.height
			if (BfLson == 1) or (BfLson == 0) :
				self.rightRotation()
				rotationNum += 1
			else:
				self.left.leftRotation() # here the height change should not be added cause its temporary
				self.rightRotation()
				rotationNum += 2

		return rotationNum


	"""Time Complexity: O(log(n))"""
	def fixTree(self): #self = currNode#
		rotationNum = 0
		heightChanges = 0
		rotated = False
		currNode = self

		while currNode is not None:
			BfCurrNode = currNode.left.height - currNode.right.height

			if abs(BfCurrNode) == 2:
				rotationNum += currNode.rotate(BfCurrNode)
				rotated = True

			if rotated:
				beforeChangingNode = currNode
				currNode = currNode.parent
				rotated = False
			else:
				heightChanges += currNode.maintainSizeHeight()
				beforeChangingNode = currNode
				currNode = currNode.parent

		resAsNode = AVLNode(None)
		resAsNode.right = beforeChangingNode
		resAsNode.left = rotationNum + heightChanges
		return resAsNode


	"""Time Complexity: O(log(n))"""
	def join(self, leftRoot, rightRoot):
		self.parent = None
		self.right = rightRoot
		self.left = leftRoot
		rightRoot.parent = self
		leftRoot.parent = self

		#join empty lists#
		if not leftRoot.isRealNode():
			if not rightRoot.isRealNode():
				self.maintainSizeHeight()
				return self
			else:
				tmpAVLTree = AVLTreeList()
				tmpAVLTree.root = rightRoot
				rightRoot.parent = None
				virtR = AVLNode(None)
				virtR.parent = self
				self.right = virtR
				tmpAVLTree.insert(0, self.value)
				currNode = tmpAVLTree.root
				return currNode

		if not rightRoot.isRealNode():
			if not leftRoot.isRealNode():
				self.maintainSizeHeight()
				return self
			else:
				tmpAVLTree = AVLTreeList()
				tmpAVLTree.root = leftRoot
				leftRoot.parent = None
				self.left = None
				tmpAVLTree.updateLast() #because we insert to last index, in contrary to the insertion above at index 0
				tmpAVLTree.insert(tmpAVLTree.length(), self.value)
				currNode = tmpAVLTree.root
				return currNode


		if rightRoot.height > leftRoot.height: # aleph situation
			currNode = rightRoot
			while (currNode.left.isRealNode()) and (currNode.height > leftRoot.height):
				currNode = currNode.left

			if currNode.parent is self: # move down only once, dont need to change pointers
				currNode = self
			else:
				currNode.parent.left = self
				self.right.parent = None
				self.right = currNode
				self.parent = currNode.parent
				currNode.parent = self

		if leftRoot.height > rightRoot.height: # beit situation
			currNode = leftRoot
			while (currNode.right.isRealNode()) and (currNode.height > leftRoot.height):
				currNode = currNode.right

			if currNode.parent is self:
				currNode = self

			else:
				currNode.parent.right = self
				self.left.parent = None
				self.left = currNode
				self.parent = currNode.parent
				currNode.parent = self

		resAsNode = self.fixTree()
		return resAsNode.right


	###########################################################
	############		ENDS HERE		#######################
	###########################################################


"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.
	"""
	def __init__(self):
		self.root = None
		self.firstElem = None
		self.lastElem = None


			############################
	###-> Additional Methods For AVLTreeList <-###
			############################


	"""Time Complexity: O(log(n))"""
	def treeSelect(self,i):
		if not self.root.left.isRealNode():
			if i==1:
				return self.root
			else:
				tmpTree = AVLTreeList()
				tmpTree.root = self.root.right
				return tmpTree.treeSelect(i-1)

		elif i > self.root.left.size:
			if self.root.left.size+1 == i:
				return self.root

			else: #going right#
				i = i- (self.root.left.size+1)
				tmpTree = AVLTreeList()
				tmpTree.root = self.root.right
				return tmpTree.treeSelect(i)

		else: #going left#
			tmpTree = AVLTreeList()
			tmpTree.root = self.root.left
			return tmpTree.treeSelect(i)


	"""Time Complexity: O(log(n))"""
	def updateFirst(self):
		#finding the new first and updating it#
		currNode = self.root
		if currNode is None:
			self.firstElem = None
		else:
			while currNode.left.isRealNode():
				currNode = currNode.left
			self.firstElem = currNode


	"""Time Complexity: O(log(n))"""
	def updateLast(self):
		#finding the new last element and updating it#
		currNode = self.root
		if self.root is None:
			self.lastElem = None
		else:
			while currNode.right.isRealNode():
				currNode = currNode.right
			self.lastElem = currNode


	###########################################################
	############		ENDS HERE		#######################
	###########################################################


	"""returns whether the list is empty
		@rtype: bool
		@returns: True if the list is empty, False otherwise
		Time Complexity: O(1)
		"""
	def empty(self):
		return self.root is None


	"""retrieves the value of the i'th item in the list
	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	Time Complexity: O(log(n))
	"""
	def retrieve(self, i):
		if (self.root is None) or (0>i or i>=self.root.size):
			return None
		else:
			ithNode = self.treeSelect(i+1)
			return ithNode.value


	"""inserts val at position i in the list
	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list 
	@returns: the number of rebalancing operation due to AVL rebalancing
	Time Complexity: O(log(n))
	"""
	def insert(self, i, val):
		if (i < 0) or (i > self.length()):
			return

		toBeIn = AVLNode(val)

		# the list is empty#
		if self.root is None:
			self.root = toBeIn
			virtL = AVLNode(None)
			virtR = AVLNode(None)
			toBeIn.left = virtL
			toBeIn.right = virtR
			virtL.parent = toBeIn
			virtR.parent = toBeIn
			toBeIn.height = 0
			toBeIn.size = 1
			self.firstElem = toBeIn
			self.lastElem = toBeIn
			return 0

		# insert to last index#
		if i == self.root.size:
			physicalNode = self.lastElem
			physicalNode.right = toBeIn
			toBeIn.parent = physicalNode
			toBeIn.height = 0
			toBeIn.size = 1
			virtR = AVLNode(None)
			virtL = AVLNode(None)
			toBeIn.right = virtR
			toBeIn.left = virtL
			virtL.parent = toBeIn
			virtR.parent = toBeIn

		else:
			prevIthNode = self.treeSelect(i + 1)
			boolLeftChild = False

			if (not prevIthNode.left.isRealNode()):
				boolLeftChild = True

			else:
				predOfPrev = prevIthNode.predecessor()

			if boolLeftChild:  # assign to left of prevIthNode
				physicalNode = prevIthNode
				physicalNode.left = toBeIn
				toBeIn.parent = physicalNode
				toBeIn.height = 0
				toBeIn.size = 1
				virtR = AVLNode(None)
				virtL = AVLNode(None)
				virtR.parent = toBeIn
				virtL.parent = toBeIn
				toBeIn.right = virtR
				toBeIn.left = virtL
			else:
				physicalNode = predOfPrev
				physicalNode.right.parent = toBeIn
				toBeIn.right = physicalNode.right
				toBeIn.parent = physicalNode
				physicalNode.right = toBeIn
				if toBeIn.right.isRealNode():
					toBeIn.height = toBeIn.right.height + 1  # in order not to count the change in height of a node
															 # who didn't exist in the tree before assignment
				else:
					toBeIn.height = 0

				toBeIn.size = 1  # this is not neccessarlly true but will be corrected in fixTree
								 # it is here for initialization
				virtL = AVLNode(None)
				virtL.parent = toBeIn
				toBeIn.left = virtL

		currNode = toBeIn
		resAsNode = currNode.fixTree()  # right son- new root, left son- number of balancing operation
		self.root = resAsNode.right
		cntBalance = resAsNode.left

		self.updateFirst()
		self.updateLast()

		return cntBalance


	"""deletes the i'th item in the list
	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	Time Complexity: O(log(n))
	"""
	def delete(self, i):
		if (i > self.root.size-1) or (i<0):
			return -1

		toBeDel = self.treeSelect(i+1)
		useOfSuccessor = False

		#the list has one element#
		if self.root.size == 1:
			self.root=None
			self.firstElem = None
			self.lastElem = None
			toBeDel = None
			return 0

		#case1: toBeDel is a leaf
		if toBeDel.size == 1:
			if toBeDel.parent.left is toBeDel:
				virtL = AVLNode(None)
				toBeDel.parent.left = virtL
				virtL.parent = toBeDel.parent
			else:
				virtR = AVLNode(None)
				toBeDel.parent.right = virtR
				virtR.parent = toBeDel.parent

			currNode = toBeDel.parent


		#case2: toBeDel has one child
		elif toBeDel.size == 2:
			if self.root is toBeDel:
				if toBeDel.left.isRealNode():
					toBeDel.left.parent = None
					self.root = toBeDel.left
				else:
					toBeDel.right.parent = None
					self.root = toBeDel.right

				self.firstElem = self.root
				self.lastElem = self.root
				toBeDel = None
				return 0

			else:
				if toBeDel.parent.left is toBeDel:
					if toBeDel.right.isRealNode():
						toBeDel.right.parent = toBeDel.parent
						toBeDel.parent.left = toBeDel.right
					else:
						toBeDel.left.parent = toBeDel.parent
						toBeDel.parent.left = toBeDel.left
				else:
					if toBeDel.right.isRealNode():
						toBeDel.right.parent = toBeDel.parent
						toBeDel.parent.right = toBeDel.right
					else:
						toBeDel.left.parent = toBeDel.parent
						toBeDel.parent.right = toBeDel.left

			currNode = toBeDel.parent


		#case3: toBeDel has 2 children
		else:
			toBeDelSucc = toBeDel.successor()
			useOfSuccessor = True

			if toBeDel.right is toBeDelSucc: #the case of which the successor is direct right son
				toBeDelSucc.parent = toBeDel.parent
				toBeDelSucc.left = toBeDel.left
				if toBeDel.parent is not None:
					if toBeDel.parent.left is toBeDel:
						toBeDel.parent.left = toBeDelSucc
					else:
						toBeDel.parent.right = toBeDelSucc
				toBeDel.left.parent = toBeDelSucc

				currNode = toBeDelSucc

			else:
				currNode = toBeDelSucc.parent  # the physical place in the tree when we start to rebalance

				toBeDelSucc.parent.left = toBeDelSucc.right
				toBeDelSucc.right.parent = toBeDelSucc.parent
				toBeDelSucc.parent = toBeDel.parent
				if toBeDel.parent is not None:
					if toBeDel.parent.left is toBeDel:
						toBeDel.parent.left = toBeDelSucc
					else:
						toBeDel.parent.right = toBeDelSucc
				toBeDel.left.parent = toBeDelSucc
				toBeDel.right.parent = toBeDelSucc
				toBeDelSucc.right = toBeDel.right
				toBeDelSucc.left = toBeDel.left


		resAsNode = currNode.fixTree()
		self.root = resAsNode.right
		cntBalance = resAsNode.left

		self.updateFirst()
		self.updateLast()

		if useOfSuccessor: #according to the instructions, changing a height of the successor doesn't count
			cntBalance -= 1
		toBeDel = None
		return cntBalance


	"""returns the value of the first item in the list
	@rtype: str
	@returns: the value of the first item, None if the list is empty
	Time Complexity: O(1)
	"""
	def first(self):
		if self.firstElem is None:
			return None
		return self.firstElem.value


	"""returns the value of the last item in the list
	@rtype: str
	@returns: the value of the last item, None if the list is empty
	Time Complexity: O(1)
	"""
	def last(self):
		if self.lastElem is None:
			return None
		return self.lastElem.value


	"""returns an array representing list 
	@rtype: list
	@returns: a list of strings representing the data structure
	Time Complexity: O(n)
	"""
	def listToArray(self):
		if self.root is None:
			return []
		else:
			sortedArr = self.root.inOrderArr([])
			return sortedArr


	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	Time Complexity: O(1)
	"""
	def length(self):
		if self.root is None:
			return 0
		else:
			return self.root.size


	"""splits the list at the i'th index
	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	Time Complexity: O(log(n))
	"""
	def split(self, i):
		if i<0 or i>=self.length():
			return None

		ithNode = self.treeSelect(i + 1)

		T1 = AVLTreeList()  # T1 bigger
		T2 = AVLTreeList()  # T2 smaller
		T1.root = ithNode.left
		T2.root = ithNode.right
		T1.root.parent = None
		T2.root.parent = None
		leftNow = False
		leftFuture = False

		if ithNode is self.root:
			T1.root = self.root.left
			T1.root.parent = None
			if T1.root.isRealNode():
				T1.firstElem = self.firstElem
			else:
				T1.firstElem = None
			T1.updateLast()

			T2.root = self.root.right
			T2.root.parent = None
			if T2.root.isRealNode():
				T2.lastElem = self.lastElem
			else:
				T2.lastElem = None
			T2.updateFirst()

			return [T1, ithNode.value, T2]

		if self.root.left is ithNode:	#ithNode is left child of the root
			T2.root = self.root.join(T2.root , self.root.right)
			T2.updateFirst()
			if self.root.right.isRealNode():
				T2.root = self.lastElem
			else:
				T2.lastElem = None

			T1.root = ithNode.left
			T1.root.parent = None
			if T1.root.isRealNode():
				T1.firstElem = self.firstElem
			else:
				T1.root = None
				T1.firstElem = None
			T1.updateLast()

			return [T1, ithNode.value, T2]

		if self.root.right is ithNode:	#ithNode is right child of the root
			T1.root = self.root.join(self.root.left, T1.root)
			if self.root.left.isRealNode():
				T1.firstElem = self.firstElem
			else:
				T1.firstElem = None
			T1.updateLast()

			T2.root = ithNode.right
			T2.root.parent = None
			if T2.root.isRealNode():
				T2.lastElem = self.lastElem
			else:
				T2.root = None
				T2.lastElem = None
			T2.updateFirst()

			return [T1, ithNode.value, T2]

		if ithNode.parent.left is ithNode:
			leftNow = True
		if ithNode.parent.parent.left is ithNode.parent:
			leftFuture = True

		currNode = ithNode.parent
		tmp = currNode.parent

		#in case tmp is self.root at first assignment
		if tmp is self.root:
			if leftNow:
				T2.root = currNode.join(T2.root, currNode.right)
			else:
				T1.root = currNode.join(currNode.left, T1.root)


		while tmp is not self.root:
			tmp = currNode.parent
			if currNode.parent.left is currNode:
				leftFuture = True
			else:
				leftFuture = False

			if leftNow: 			#currNode sees the tree as left child
				T2.root = currNode.join(T2.root, currNode.right)
			else: 					#currNode sees the tree as right child
				T1.root = currNode.join(currNode.left, T1.root)

			currNode = tmp
			leftNow = leftFuture

		#carrying out the last join. with the root
		currNode = tmp
		if leftFuture:
			T2.root = currNode.join(T2.root, currNode.right)
		else:
			T1.root = currNode.join(currNode.left, T1.root)

		#in purpose to null the empty lists
		if not T1.root.isRealNode():
			T1.root = None
		if not T2.root.isRealNode():
			T2.root = None

		T1.updateFirst()
		T1.updateLast()
		T2.updateFirst()
		T2.updateLast()

		return [T1, ithNode.value, T2]


	"""concatenates lst to self
	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	Time Complexity: O(log(n))
	"""
	def concat(self, lst):
		#concat empty lists#
		if lst.empty() and (not self.empty()) :
			return self.root.height+1

		if self.empty():
			if lst.empty():
				return 0
			else:
				self.root = lst.root
				return lst.root.height+1

		deltaHeight = abs(self.root.height - lst.root.height)
		newLast = lst.lastElem
		currNode = self.lastElem

		if self.root.size == 1:
			lst.insert(0, currNode.value)
			self.lastElem = newLast
			self.root = lst.root
			return deltaHeight


		self.delete(self.length()-1) 		#plug out the last element from the tree
		self.root = currNode.join(self.root, lst.root)
		self.lastElem = newLast

		return deltaHeight


	"""searches for a *value* in the list
	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	Time Complexity: O(log(n))
	"""
	def search(self, val):
		tmpNode = self.firstElem
		i=0
		len = self.length()
		while len > i :
			if tmpNode.value == val:
				return i
			else:
				tmpNode = tmpNode.successor()
				i+=1

		return -1


	"""returns the root of the tree representing the list
	@rtype: AVLNode
	@returns: the root, None if the list is empty
	Time Complexity: O(1)
	"""
	def getRoot(self):
		return self.root
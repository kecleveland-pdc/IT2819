class Node :
	def __init__( self, data ) :
		self.data = data
		self.next = None
		self.prev = None

class LinkedList :
	def __init__( self ) :
		self.head = None		

	def add( self, data ) :
		node = Node( data )
		if self.head == None :	
			self.head = node
		else :
			node.next = self.head
			node.next.prev = node						
			self.head = node			

	def search( self, k ) :
		p = self.head
		if p != None :
			while p.next != None :
				if ( p.data == k ) :
					return p				
				p = p.next
			if ( p.data == k ) :
				return p
		return None	

	def remove(self, k) :
		p = self.head # set head to node p
		if p != None :
			if (p.data == k) : # if head node data matches key
				self.head = p.next # set self.head to next
				#print("Found match: ", str(p.data))
				#print("Deleting: ", str(p.data))
				p = None # set p to None 
				return # return bc found
		while(p != None) : # begin interating over list to find matching key
			if p.data == k :
				#print("Found match: ", p.data)
				break # found
			temp = p # hold cur in temp
			p = p.next
		if p == None : # if p never in list
			return None # nothing to remove
		
		temp.next = p.next 
		#print("Deleting: ", str(p.data))
		p = None # delete

	def __str__( self ) :
		s = ""
		p = self.head
		if p != None :		
			while p.next != None :
				s += p.data
				p = p.next
			s += p.data
		return s

# example code
l = LinkedList()

print ("Add: a")
l.add( 'a' )
print ("List = ", l, "\n")

print ("Add: b")
l.add( 'b' )
print ("List = ", l, "\n")

print ("Add: c")
l.add( 'c' )
print ("List = ", l, "\n")
	
print ("Remove: c")
l.remove( 'c' )
print ("List = ", l, "\n")

print ("Remove: a")
l.remove( 'a' )
print ("List = ", l, "\n")
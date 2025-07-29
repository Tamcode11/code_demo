#custom class for LinkedList .
class Node:
    def __init__(self,data):
       #LL has NODEs which store data and next pointer .
        self.data=data # when object create insert values into data variable.
        self.next=None # Now next is None(EMPTY)

a=Node(5)  #obj a has val = 5
b=Node(4)  #obj b has val = 4
c=Node(3)  #obj c has val = 3

Head=a #First node of LL is HEAD always (IMP for traversing)
print(Head.data)  #print Head=a ,data = 5 

#Join 
a.next=b #a points to b
b.next=c #b points to c 

print(a.next.data) # a -> b -> 4 
print(a.next.next.data)  # a -> b -> -> c -> 3 

#For Large data use loop 
def printLL(Head):
 curr = Head # iterator curr is on Head 
 while curr != None: # iterate until curr not reach to None 
    print(curr.data,end=" ") # print values with space 
    curr=curr.next   #update curr iterator 
#printLL(Head)

# Insert at beginning  (insert 6)

Newnode=Node(6) # create a newnode (Newnode next is null )
Newnode.next=Head # (Newnode next which was null now attached to head )
Head=Newnode # Now Newnode become Head 
#printLL(Head) # 6 -> 5 -> 4 -> 3 

# Insert at end (insert 2 )
newnode=Node(2) # create new node 
curr =Head     # curr iterator is on Head  
while curr.next != None: # iterate until curr not reach to null 
   curr=curr.next   # update
curr.next=newnode   # assign newnode after previous node 
#printLL(Head)  # 6 -> 5 -> 4 -> 3 -> 2 

# Insert at kth index 

k=2 # insert at second index 
newNode=Node(7) # create newnode 
curr = Head # curr itertor is on Head 

for i in range(k-1):  # range(1): runs once
   curr=curr.next  # curr = 6 ,next = 5 
newNode.next = curr.next  #  newnode=7 ->None -> curr =5 -> next =4 
curr.next = newNode  # Node with value 5 now points to newNode(7)
#printLL(Head)  # 6 -> 5 ->7 -> 4 -> 3 -> 2

# Delete First Node (Head)
Head=Head.next # head=6 now head is 5 
#printLL(Head)  # 5 ->7 -> 4 -> 3 -> 2

# Delete last node 
curr = Head  # curr is on Head = 5 
while curr.next.next != None: 
   curr=curr.next
curr.next=None
#printLL(Head)  # 5 ->7 -> 4 -> 3

# Delete node kth index (1 index)
k=1

curr = Head
for i in range(k-1):
 curr=curr.next 
            # 7-> 4 ->3
curr.next =curr.next.next
printLL(Head)  # 5 -> 4 -> 3 








 







    





























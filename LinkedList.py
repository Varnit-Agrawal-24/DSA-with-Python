# Implementation of Linked List

#create node class 
class Node:
    #constructor of node class
    def __init__(self,data):
        self.data=data #to assign data of node
        self.next=None #assign address of next node which initially is NULL

#create linked list class
#every features of linked list comes here
class LinkedList:
    #constructor of linked list 
    def __init__(self):
        self.head=None #create head of LL

    #traversal of LL and print     
    def printLL(self):
        #create temporary node and assign to head 
        #bcz we don't want any change in head node of LL
        temp=self.head 
        while(temp): #travel LL until we found last node (last node address is null which break this loop) 
            print(temp.data) #print data of temp node
            temp=temp.next #assign temp node to the next address of current temp node
    

    #Insert element at Begin
    def insertHead(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    
    #Insert element at End
    def insertTail(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while(last_node.next): 
            last_node=last_node.next
        last_node.next=new_node

    #Insertion at given postion
    def insertIndex(self,pos,new_data):
        new_node=Node(new_data)
        if(pos==1):
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        pos=pos-2
        while(pos>0 and temp is not None):
            temp=temp.next
            pos=pos-1
        if temp is None:
            print("Index not exist!")
            return
        new_node.next=temp.next
        temp.next=new_node


    #Delete starting element    
    def deleteHead(self):
        if self.head is None:
            return
        self.head=self.head.next

    #Delete end element
    def deleteTail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
            return
        last_node=self.head
        while(last_node.next.next):
            last_node=last_node.next
        last_node.next=None


    #Search in LL
    def search(self,key):
        res=1
        temp=self.head
        while(temp):
            if temp.data==key:
                return res
            else:
                res=res+1
                temp=temp.next
        return f"{key} is not present"


if __name__=='__main__':
    # create object of class linked list
    ll=LinkedList()
    #create node of value 10 and assign to head of the linked list
    ll.head=Node(1)

    #create node of value 20 and assign in object called sec
    sec=Node(2)
    #assign address of the head to sec
    ll.head.next=sec

    #Insertion
    ll.insertHead(10)
    ll.insertHead(14)
    ll.insertTail(23) 
    ll.insertTail(17) 
    ll.insertIndex(5,20)



    #print linked list
    ll.printLL()


    #Deletion
    ll.deleteHead()
    ll.deleteTail()
    print("After Deletion")
    ll.printLL()


    #Searching
    x=int(input("Enter element"))
    p=ll.search()
    print(p)
    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.perv=None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    
    def printDLL(self):
        temp=self.head
        print("Printing Double Linked List:")
        while(temp):
            print(temp.data)
            temp=temp.next
    
    def insert(self,new_data):
        newNode=Node(new_data)
        newNode.next=self.head
        self.head.perv=newNode
        self.head=newNode
    
    def reverse(self):
        if self.head is None or self.head.next is None:
            return
        pervNode=None
        currNode=self.head
        while(currNode):
            pervNode=currNode.perv
            currNode.perv=currNode.next
            currNode.next=pervNode
            currNode=currNode.perv
            if(currNode is not None):
                self.head=currNode

if __name__=="__main__":
    #create DLL and insert values with self assigning of node
    dll=DoubleLinkedList()
    dll.head=Node(10)
    secNode=Node(15)
    dll.head.next=secNode
    secNode.perv=dll.head
    dll.printDLL()

    # insert data in DLL using Function
    dll.insert(12)
    dll.insert(35)
    dll.printDLL()

    #reverse DLL
    dll.reverse()
    dll.printDLL()
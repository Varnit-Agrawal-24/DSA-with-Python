class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
#insert in Last   
    def insert(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=newNode

#print LL
    def printLL(self):
        if self.head==None:
            print("Empty LL")
            return
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
        print()

        #reverse LL
    def reverse(self):
        pre=pos=None
        cur=self.head
        while cur:
            pos=cur.next
            cur.next=pre
            pre=cur
            cur=pos
        self.head=pre




if __name__=="__main__":
    ll=LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.insert(40)
    ll.insert(50)
    ll.printLL()
    ll.reverse()
    ll.printLL()

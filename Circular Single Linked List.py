class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def Insert_Begin(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
            
    def Insert_End(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
        self.tail=new_node
        self.tail.next=self.head
    
    def Insert_Index(self,data,index):
        new_node=Node(data)
        temp=self.head
        count=1
        while(temp.next!=None and count<index):
            temp=temp.next
            count+=1
        new_node.next=temp.next
        temp.next=new_node
    def Delete_Begin(self):
        if self.head==None:
            print("NO nodes")
        else:
            self.head=self.head.next
            self.tail.next=self.head
    def Delete_End(self):
        if self.head==None:
            print("NO nodes")
        elif self.head.next==None:
            self.head=None
        else:
            temp=self.head
            while(temp.next!=self.tail):
                temp=temp.next
            self.tail=temp
            temp.next=self.head
    def Delete_Index(self,index):
        if self.head==None:
            print("NO nodes")
        else:
            temp=self.head
            count=1
            while(temp.next!=None and count<index):
                temp=temp.next

                count+=1
            temp.next=temp.next.next
    def Display(self):
        temp=self.head
        if (self.head==None):
            print("NO nodes")
        while(temp!=None):
            print(temp.data,"-->",end=" ")
            temp=temp.next
            if temp == self.head:
                break
    def Search(self,data):
        if self.head==None:
            print("NO nodes")
        else:
            temp=self.head
            count=0
            while(temp):
                count+=1
                if(temp.data==data):
                    print(data," found at Position-->",count)
                    return
                temp=temp.next
                if temp==self.head:
                    break
            print("Element not found")
        
         






class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkList:
    def __init__(self,value): 
        node=Node(value)
        self.head = node
        self.tail = node
        self.length = 1
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next   

    def append(self,value):
        node=Node(value)
        if(self.length==0):
            self.head = node
            self.tail = node
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node

        self.length+=1
        return True

    def pop(self):
        if(self.length==0):
            return None
        temp=self.tail
        if(self.length==1):
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev =None

        self.length-=1
        return temp

    def prepend(self,value):
        node =Node(value)
        if(self.length==0):
            self.tail=node
            self.head=node

        else:
            node.next=self.head
            self.head.pre=node
            self.head=node
        self.length+=1
        return True    
    def prepop(self):
        if(self.length==0):
            return None
        temp=self.head        
    
        if(self.length==1):
            self.tail=None
            self.head=None
        else:
            self.head=self.head.next
            self.head.prev=None

            temp.next= None
        self.length-=1
        return temp    

    def get_node(self,index):
        if(index <0 or index >= self.length):
            return None
        temp = self.head

        if(index <= self.length/2):
            for i in range(index):
                temp=temp.next
        else:
            temp = self.tail
            for i in range(self.length-1,index,-1):
                temp=temp.prev
                   
        return temp  
    def set_node(self,index,value):
        if(index <0 or index >= self.length):
            return None
        temp=self.get_node(index) 
        temp.value=value
        if(temp):
            return True
        return False 

    def insert(self,index,value):
        if(index <0 or index > self.length):
            return False
        if(index == self.length):
            return self.append(value)  

        if(index == 0):
            return self.prepend(value)      


        node=Node(value)
        before=self.get_node(index-1)
        after=before.next

        node.prev=before
        node.next=after
        before.next=node
        after.prev=node
        self.length+=1
        return True

    def remove(self, index):
        if(index <0 or index >= self.length):
            return None
        if(index == self.length-1):
            return self.pop()  

        if(index == 0):
            return self.prepop()

        temp=self.get_node(index)
        temp.next.prev=temp.prev
        temp.prev.next=temp.next
        temp.prev=None
        temp.next=None
        self.length-=1
        return temp





        




                


            




dl=DoubleLinkList(4)
dl.append(3)
dl.append(6)
dl.append(8)

# dl.prepend(2)
# print(dl.prepop())
# print(dl.prepop())
# print(dl.prepop())
# print(dl.get_node(1))
# dl.set_node(0,9)
# dl.insert(0,7)
# dl.remove(2)

#ohoooo thats it all working ....



dl.print_list()

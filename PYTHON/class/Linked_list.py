class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def insert_after_position(self,data,position):
        new_node=Node(data)
        if self.head is None :
            self.head=new_node
            return
        count=1
        temp=self.head
        while count!=position and temp.next!=None:
            # if(count == position):
            #     temp=temp.next
            #     break
            # else:
            temp=temp.next
            count=count+1
        if count==position:
            # print("count->",count)
            new_node.next=temp.next
            temp.next=new_node
        else:
            print("exceed the list element")
    def print_list(self):
        current = self.head
        while current!=None:
            print(current.data, end=' ')
            current = current.next
        print()
    def second_num(self):
        current=self.head
        while current.next.next:
            current=current.next
        return current.data
    # def find_second_last(self):
    #     if self.head is None or self.head.next is None:
    #         return None  # List has less than two elements
    #     current = self.head
    #     while current.next.next:
    #         current = current.next
    #     return current.data
    def search(self,data):
        temp=self.head
        while temp is not None: 
            # or while temp:
            if(temp.data==data):
                print("data found")
                return
            else:
                temp=temp.next
        print("data not found")
        return
    def swap(self):
        cur=self.head
        while cur is not None and cur.next is not None:
            cur.data,cur.next.data=cur.next.data,cur.data
            cur=cur.next.next
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        self.head=prev
# Usage
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
linked_list.print_list()
linked_list.search(3)
linked_list.search(7)
print(linked_list.second_num())
linked_list.swap()
linked_list.print_list()
linked_list.reverse()
linked_list.print_list()
linked_list.insert_after_position(45,3)
linked_list.print_list()

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
#         new_node.prev = current

#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.data, end=' ')
#             current = current.next
#         print()

#     def print_reverse(self):
#         current = self.head
#         while current.next:
#             current = current.next
#         while current:
#             print(current.data, end=' ')
#             current = current.prev
#         print()

# # Usage
# doubly_linked_list = DoublyLinkedList()
# doubly_linked_list.append(1)
# doubly_linked_list.append(2)
# doubly_linked_list.append(3)
# doubly_linked_list.append(4)
# doubly_linked_list.append(5)
# doubly_linked_list.append(6)
# doubly_linked_list.print_list()
# doubly_linked_list.print_reverse()
# # circular doubly linked list delete node at last and at begining
# circular and doubly linklist
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# class dlinklist:
#     def __init__(self):
#         self.head=None
#     def insert(self,data):
#         new_node=Node(data)
#         if(self.head==None):
#             self.head=new_node
#             new_node.next=self.head
#             # print("node-->",self.head.data," address prev-->",self.head.prev," address.next-->",self.head.next)
#         else:
#             temp=self.head
#             while temp.next!=self.head:
#                 temp=temp.next
#             temp.next=new_node
#             new_node.prev=temp
#             # from here it will become circular
#             new_node.next=self.head
#             self.head.prev=new_node
#             # print("node---->",new_node.data," address prev--->",self.head.prev," address.next--->",self.head.next)
#     def print(self):
#         # print("enter")
#         curr=self.head
#         # print("hello")
#         while True:
#             print(curr.data,end=" ")
#             curr=curr.next
#             if(curr==self.head):
#                 break
#         # or temp last  data print
# link1=dlinklist()
# link1.insert(1)
# link1.insert(2)
# link1.insert(3)
# link1.insert(4)
# link1.insert(5)
# link1.insert(6)
# link1.insert(7)
# link1.insert(8)
# link1.insert(9)
# link1.insert(10)
# link1.print()
def print(self):
        print("enter")
        curr=self.head
        print("hello")
        while curr.next is not self.head:
            print(curr.data,end=" ")
            curr=curr.next
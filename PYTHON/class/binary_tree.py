# full binary tree can be complete tree reverse not true
# depth see from up and height find from down
class BtNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BtTree:
    def __init__(self):
        self.root=None

    # def insert(self,data):
    #     new_node=BtNode(data)
    #     if self.root==None:
    #         self.root=new_node
    #         print("insert1 : ",self.root.data)
    #     else:
    #         temp=self.root
    #         count=0
    #         while temp!=None:
    #             if(data>temp.data):
    #                 temp=temp.left
    #                 print("left")
    #             if(data<temp.data):
    #                 temp=temp.right
    #                 print("right")
    #             print(count," ")
    #             count=count+1
    #         temp=new_node
    #         print("insert : ",temp.data)
    # def inorderTraversal(self):
        

    def insert(self,val):
        if(self.root==None):
            new_node=BtNode(val)
            self.root=new_node
            # print("added2")
            return
        else:
            temp=self.root
            self.add(temp,val)
    def add(self,curr,data):
        if(curr.left==None):
            new_node=BtNode(data)
            curr.left=new_node
            # print("added1")
            return
        if(curr.right==None):
            new_node=BtNode(data)
            curr.right=new_node
            # print("added2")
            return
        self.add(curr.left,data)
        # self.add(curr.right,data)


    def inorder(self):
        temp=self.root
        self.intrack(temp)
    def intrack(self,curr):
        if curr is None:
            return
        else:
            self.intrack(curr.left)
            print(curr.data,end=" ")
            self.intrack(curr.right)


    def preorder(self):
        temp=self.root
        self.pretrack(temp)
    def pretrack(self,curr):
        if curr is None:
            return
        else:
            print(curr.data,end=" ")
            self.pretrack(curr.left)
            self.pretrack(curr.right)


    def postorder(self):
        temp=self.root
        self.posttrack(temp)
    def posttrack(self,curr):
        if curr is None:
            return
        else:
            self.posttrack(curr.left)
            self.posttrack(curr.right)
            print(curr.data,end=" ")
            return

    def height(self):
        if(self.root==None):
            print("no root found so height is -1")
            return
        temp1=self.root
        temp2=self.root
        count1=1
        count2=1
        while True:
            if(temp1==None):
                break
            temp1=temp1.left
            count1=count1+1
        while True:
            if(temp2==None):
                break
            temp2=temp2.left
            count2=count2+1
        if count1>count2:
            print("\nheight : ",count1)
        else:
            print("\nheight : ",count2)


    def no_of_node(self):
        temp=self.root
        node=self.countnode(temp)
        print(node," ")
    def countnode(self,curr):
        if curr is None:
            return 0
        return 1+self.countnode(curr.left)+self.countnode(curr.right)



bt1=BtTree()
bt1.insert(10)
bt1.insert(20)
bt1.insert(30)
bt1.insert(40)
bt1.insert(50)
bt1.insert(60)
bt1.insert(70)
bt1.insert(80)
print("inorder : ")
bt1.inorder()
print("\npreorder : ")
bt1.preorder()
print("\npostorder : ")
bt1.postorder()
bt1.height()
bt1.no_of_node()
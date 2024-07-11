# # a=[1,"Anchal","Roshnni",5]
# # print(a[1])
# # print(a[3])
# # #change the value using 
# # a[0]="Krishna"
# # print(a.insert(0,"hy"))
# # print(a[0])
# # print(a[0:3])
# # print(a[0:])
# # list=[1,3,5,99,3,7,55,77]
# # print(list)
# # #we cannot use another datatype for storting it actually change the list
# # #list.sort()  sort the list
# # #list.reverse()  reverse the list
# # #list.append(667)  add sometghing at the last
# # #list.insert(0,7)  insert at the position mentioned
# # #list.pop(3)  remove the item from the index
# # #list.remove(3)  remove the number that first arrive
# # #l1=list.count(3)  count the element
# # list.sort()
# # print(list)
# # list.pop()
# # list.remove(3)
# # print(list)
# # list.reverse()
# # print(list)
# # count=list.count(3)
# # print("count : ",count)
# # al=eval(input("enter some number :"))
# # print(al)
# # li="1,2,3,4,5"
# # x=li.split()
# # print(x)
# # x=int(input("enter no. in list : "))
# # li=[]
# # i=1
# # for i in range(0,x,1):
# #     li.append(i)
# # print(li)
# # zero=0
# # listy=[]
# # for i in range(0,5,1):
# #     listy.append(zero) 
# # print(listy)
# # l1=[1,2,3,4,5]
# # l2=[6,7,8,9,10]
# # l3=l1+l2
# # print(id(l3))
# # l3+=[88,99]
# # print(id(l3))
# # print(l1)
# # print(l2)

# # l=[1,2,3,4,5]
# # print(l.pop())
# # print(l.pop(2))
# # print(l)
# # l.append(8)
# # print(l)
# # print(len(l))
# # print(l.count(1))
# # print(l.index(1))
# # # li=[]
# # # print(li.pop())
# # l.reverse()
# # print(l)
# # l.sort()
# # print(l)
# # # aliasing
# # y=l
# # l[0]=1000
# # print(l)
# # print(y)
# # # cloning done by ->slicing and copying
# # b=l[:]
# # l[0]=100
# # print(l)
# # print(b)
# # x=[1,"anchal",3,40]
# # y=x.copy()
# # x[0]=55
# # print(x)
# # print(y)


# list1 = [1, 2, 3]
# list2 = [1, 2, 3]

# print(list1 < list2)   # False
# print(list1 <= list2)  # True
# print(list1 > list2)   # False
# print(list1 >= list2)  # True
# print(list1 == list2)  # True
# print(list1 != list2)  # False

# list3 = [1, 2, 3, 4]
# print(list1 < list3)   # True
# print(list1 <= list3)  # True
# print(list1 > list3)   # False
# print(list1 >= list3)  # False
# print(list1 == list3)  # False
# print(list1 != list3)  # True

# list4=[[1,2,3],["anchal","saloni","roshni"],['a','b','c','d']]
# for i in range (0,3):
#     print(list4[i])
# list5=[]




# my_list = [x for x in range(5)]
# my_list = list(range(5))
# my_list = list((1, 2, 3, 4, 5))
# my_list = [0] * 5       output->[0, 0, 0, 0, 0]
# my_list = [1, 2, 3]
# my_list.extend([4, 5, 6])
my_list = list(range(5))
my_list.append(5)
print(my_list)
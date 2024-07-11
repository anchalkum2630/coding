a=10
# id() function is a built-in function that returns the unique identifier of an object. The identifier is an integer, which represents the memory address of the object. The id() function is commonly used to check if two variables or objects refer to the same memory location.
print("id of ",a,"is ",id(a))


#type() function is mostly used for debugging purposes. Two different types of arguments can be passed to type() function, single and three arguments. If a single argument type(obj) is passed, it returns the type of the given object. If three argument types (object, bases, dict) are passed, it returns a new type object. 
print("type of ",a," is ",type(a))

#range() function returns a sequence of numbers, in a given range. The most common use of it is to iterate sequences on a sequence of numbers using Python loops.
for i in range(1,5):
    print(i)
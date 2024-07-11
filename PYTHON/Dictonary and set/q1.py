dic={
    "fanka":"fan",
    "hawa":"air",
    "panni":"water",
    "nind":"sleep",
    "jarurat":"important"
}
print("option : ",dic.keys())
a=input("Enter the hindi word to know it's meaning : ")
#print(dic[a])  this will throw an error to avoid this i use 
print("Meaning of the word : ",dic.get(a))

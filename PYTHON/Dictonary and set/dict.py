mydic = {
    "Fast":"In a quick mannner",
    "Harry":"A Coder",
    "Marks":[1,2,3,4],
    "anodic":{"Anchal":"A learner"}
}
print(mydic["Fast"])   #or print(mydic.get("Fast"))=throw none in terminal if the item is not present and direct name throw an error if item is not present

print(mydic["Marks"])
print(mydic["anodic"])
print(mydic["anodic"]["Anchal"])
#marks can be changed

print(mydic.keys())
print(type((mydic.keys())))
print(list((mydic.keys())))
print("\n")
print(mydic.values())
print("\n")
print(mydic.items())
updatedic={
    "lovish":"Friend",
    "Stolid":"Unemotional"
}
mydic.update(updatedic)
print("\n")
print(mydic.items())



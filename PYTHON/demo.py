def count(child_dict,i):
    if i not in child_dict.keys():
        return 1
    ans=1
    for j in child_dict[i]:
        ans+=count(child_dict,j)
    return ans
child_dict=dict()
child_dict[0]=[1,2]
child_dict[1]=[3,4,5]
child_dict[2]=[6,7,8]
print(count(child_dict,0))

s="SillyPython-561"
result=""
for char in s:
    if char in str(not s):
        result+="B"
    elif char.isalpha():
        result+=char.upper()
    elif char.isdigit():
        result+=str(int(char)+3)
    else:
        result+=char
print(result)

vehicles={"Bicycle","Scooter","Car","Bike","Truck","Bus","Rickshaw"}
heavyVehicles={"Truck","Bus"}
lightVehicles={"Rickshaw","Scooter","Bike","Bicycle"}
lyt=vehicles-heavyVehicles
print(lyt)
hyt=vehicles-lightVehicles
avg=lyt&hyt
print(avg)
tran=lightVehicles|heavyVehicles
print(tran)
print(min(vehicles))
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
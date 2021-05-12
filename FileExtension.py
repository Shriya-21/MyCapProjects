myDict={"c":"C","cpp":"C++","py":"Python","java":"Java"}

Name=str(input("Name: "))
Ext=str(input("Extension: "))

print("Input the Filename: ",Name,".",Ext)
print("The extension of the file is: ")
print(myDict.get(Ext))

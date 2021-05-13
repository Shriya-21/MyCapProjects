myDict = {"c":"C", "cpp":"C++", "py":"Python", "java":"Java", "txt":"Text"}

file = input ("Input the filename: ")
file_ext = file.split (".")

print ("The extension of the file is:", myDict.get (file_ext[1]))

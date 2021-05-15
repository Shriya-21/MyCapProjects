i=0
myList=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    ele = int(input())
    myList.append(ele)
    
for i in range(0,n):
    if myList[i]>=0:
        print(myList[i])
    i=i+1

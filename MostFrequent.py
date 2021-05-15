def most_frequent(string):
    freq={}
    for i in string:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    l=list(freq.items())
    print(sorted(l,key=lambda l:l[1], reverse=True))

string=str(input("Please input a string: "))
most_frequent(string)

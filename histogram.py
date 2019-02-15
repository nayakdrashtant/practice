def histogram(mystring):
    dictonary = dict()
    for my in mystring:
        if my not in dictonary:
            dictonary[my] = 1
        else:
            dictonary[my] += 1
    return dictonary

var = input("Enter word to count histogram:")
print("Your output for histogram is:", histogram(var))

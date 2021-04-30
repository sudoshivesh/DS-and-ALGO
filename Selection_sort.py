#WAp to sort the element using selection sort
mylist=input("Enter a Number: ").split()
A=[int(i) for i in mylist]
print("Before Sorting: ")
print(A)
length=len(A)
for i in range(length-1):
    min=i
    for j in range(i+1,length):
        if A[min]>A[j]:
            min=j
    if i!=min:
        A[i],A[min]=A[min],A[i]
print("Sorted List: ")
print(A)

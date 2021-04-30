mylist=input("enter numbers: ").split()
A=[int(i) for i in mylist]
A.sort()
print("The Sorted List is: ")
print(A)
length=len(A)
low=0
high=length-1
value=int(input("Enter a number to be search: "))
loc=-1
while(low<=high):
    mid=(low+high)//2
    if value==A[mid]:
        loc=mid+1
        break
    elif value>A[mid]:
        low=mid+1
    elif value<A[mid]:
        high=mid-1
        low=0
if loc==-1:
    print(value,"not found")
else:
    print(value,"is found at",loc,"postion")
    
#pehle half karega index ko jod ke then search krega mid me
    #uske baad compare karegaa mid se bara chota ya equal
    #phir divide karega list 

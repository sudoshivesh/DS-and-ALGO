#program to implement linear search or sequencial searching
mylist=input("enter numbers: ").split()
A=[int(i) for i in mylist]
A.sort()
print("Before Sorting: ")
print(A)
length=len(A)
#logic of linear Searching
value=int(input("Enter a Number to be searched: "))
loc=-1
for i in range(length):
    if value==A[i]:
        loc=i+1
        break
if loc==-1:
    print(value,"not found")
else:
    print(value,"found at",loc,"position")



#Nahi hai to search krte rahega aur
#jaise value milega ti loop se baharaake print kr dega

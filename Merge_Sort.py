#mergeshort
def merge(A,p,mid,r):
    L=A[p:mid+1]
    R=A[mid+1:r+1]
    L.append(1000)
    R.append(1000)
    i=j=0
    for k in range(p,r+1):
        if L[i]<R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1
def mergeshort(A,p,r):
    if p<r:
        mid=(p+r)//2
        mergeshort(A,p,mid)
        mergeshort(A,mid+1,r)
        merge(A,p,mid,r)
mylist=input("Enter Elements: ").split()
A=[int(i) for i in mylist]
length=len(A)
print("Before Sorting: ")
print(A)
mergeshort(A,0,length-1)
print("Sorted List: ")
print(A)

        
    

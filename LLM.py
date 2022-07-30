# FUnctions
def l_s(ar,item):
    i=0
    while i < len(ar) and ar[i]!=item :
        i+=1
    if i< len(ar):
        return i
    else:
        return False
def b_s(ar,item):
    beg=0
    last=len(ar)-1
    while(beg<=last):
        mid= (beg+last)//2
        if (item == ar[mid]):
            return mid
        elif (item >ar[mid]):
            beg=mid+1
        else:
            last= mid-1
    else:
        return False          #when item not found
def b_sort(alist):
    n=len(alist)
    for i in range(n):
        for j in range(0,n-i-1):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
    print("list after shorting",alist)
def i_sort(ar):
    for i in range(1,len(ar)):
        v=ar[i]
        j=i-1
        while ar[j]> v and j>=0:
            ar[j+1]=ar[j]
            j-=1
        #Insert the value at its correct postion
        else:
            ar[j+1]=v
    print("list after shorting",ar)
def traverse(ar):
    size =len(ar)
    for i in range(size):
        print (ar[i],)

def cls(n):
    print (" "*n )
def s():
    print( "--------------------------------------------------------------------------------")

# remove element
from array import *

arr=array('i', [101, 102, 101, 103, 104, 105, 101])

n=len(arr)
i=0

while i<n:
	print(arr[i])
	i+=1

print("Array After Remove")
r=arr.remove(101 )

n=len(arr)
i=0

while(i<n):
	print(arr[i])
	i+=1
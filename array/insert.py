# Insert
from array import *

arr=array('i', [101,102,103,104,105])

n=len(arr)
i=0


while i<n:
	print(arr[i])
	i+=1

print("Array After Insert")
arr.insert(1,1006)
arr.insert(3,1007)

n=len(arr)
i=0

while(i<n):
	print(arr[i])
	i+=1


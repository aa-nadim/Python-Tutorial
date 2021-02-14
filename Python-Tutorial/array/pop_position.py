# pop (positionNumber)
from array import *

arr=array('i', [101,102,103,104,105])

n=len(arr)
i=0


while i<n:
	print(arr[i])
	i+=1

print("Array After POP")
r=arr.pop(1)

n=len(arr)
i=0

while(i<n):
	print(arr[i])
	i+=1
	
print("Removed elemint:", r)


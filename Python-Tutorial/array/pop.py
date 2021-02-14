# pop()
from array import *

arr=array('i', [101,102,103,104,105])

n=len(arr)
i=0


while i<n:
	print(arr[i])
	i+=1

print("Array After POP")
arr.pop()

n=len(arr)
i=0

while(i<n):
	print(arr[i])
	i+=1


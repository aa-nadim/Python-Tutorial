#Getting Array Input from user using while Loop
from array import *

arr=array('i', [])
n=int(input("Enter Number of Elements: "))
i=0
j=0

while i<n:
	arr.append(int(input("enter element: ")))
	i=i+1

while (j<len(arr)):
	print(arr[j])
	j=j+1
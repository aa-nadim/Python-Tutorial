# Iterative python program to reverse an array
 
# Function to reverse A[] from start to end
from array import *
def reverseList(A,start,end):
	while start<end:
		A[start],A[end]=A[end],A[start]
		start += 1
		end -= 1
A=array('i', [101, 102, 101, 103, 104, 105, 101])
print(A)
n=len(A)
i=0
while i<n:
	print(A[i])
	i+=1

reverseList(A,0,n-1)
print("Reversed list is")
print(A)
i=0
while i<n:
	print(A[i])
	i+=1

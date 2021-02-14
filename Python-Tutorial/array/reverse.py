# Iterative python program to reverse an array
from array import *

n=int(input())
A=array('i', [])

i=0
while i<n:
	A.append(int(input()))
	i+=1
	
	
#The original array
print("Original Array is :",A)
#reversing using reverse()
A.reverse()
print("Reversed Array:",A)
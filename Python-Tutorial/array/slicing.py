from array import *
A=array('i', [101, 102, 103, 104, 105])

print("Original Array")

n=len(A)
for i in range(n):
	print(i, "=", A[i])

print("*****************")
a=A[1:5]
for i in a:
	print(i)
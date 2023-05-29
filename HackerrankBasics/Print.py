#Read an integer N 
#Without using any string methods, try to print the following
# 123....N

n = int(input())
print(*range(1,n+1),sep=' ') 

"""
range(1, n+1) creates an iterable range object that starts from 1 and ends at n (inclusive).
The * operator is used to unpack the range object into individual values. This allows the print() function to receive each number as a separate argument.
sep=' ' specifies that a space character should be used as the separator between the numbers when they are printed.
"""

#You are given 3 integers X,Y and Z representing the dimensions of a cuboid along with an intger N
#You have to print a list of all possible coordinates given by (i,j,k) where the sum of 
# i+j+k is not equal to N. Here 0<i<X, 0<i<Y, 0<i<Z

x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())
l = list()

for i in range(x+1):
  for j in range(y+1):
    for k in range(z+1):
      if(i+j+k!=n):
        l.append([i,j,k])

print(l)        
  

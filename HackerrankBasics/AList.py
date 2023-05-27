#Consider a list list=[]
# You can perform the following commands
# insert i e: Insert integer e at any position
# print: print the list
# remove e: Delete the first ocurrence of integer e
# append e: Insert integer e at the end of the list
# sort: sort the list
# pop: Por the last element of the list
# reverse: Reverse the list

# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 
# 7 types listed above. iterate through each command in order and perform the operation on your list

arr = {}
for i in range(N):
  s = input().split()
  for i in range(1,len(s)):
    s[i] = int(s[i])
    
  if s[0] == "append":
    arr.append(s[1])
  elif s[0] == "insert":
    arr.insert(s[1],s[2])
  elif s[0] == "remove":
    arr.remove(s[1])
  elif s[0] == "pop":
    arr.pop()
  elif s[0] == "sort":
    arr.sort()
  elif s[0] == "reverse":
    arr.reverse()
  elif s[0] == "print":
    arr.print()
#############################
##########  SPLIT  ##########

sentence = "Hello, how are you?"
words = sentence.split()
print(words)

#TAKES A SPACE AS SEPARATOR

data = "apple,banana,grape,orange"
fruits = data.split(",")
print(fruits)

#TAKES , AS A SEPARATOR

numbers = "1-2-3-4-5-6"
digits = numbers.split("-", 3)
print(digits)

# TAKES - AS A SEPARATOR AND PERFORMS MAXIMUM 3 SPLITS


    
    
    
    
    
    
    

#The user enters a string and a substring. You have to print the number of times that the substring 
#occurs in the given string, traversal will take place from ñeft to right

def count_substring(string,sub_string):
  ml = len(string)
  sl = len(substring)
  c=0
  for i in range(ml-sl+1):
    if(string[i:(i+sl)]==sub_string)
    c=C+1
  return c

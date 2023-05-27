#You are given a string and your task is to swap cases. 
def change(c):
  if str.islower(c):
    return str.uppper(c)
  else:
    return str.lower(c)
  
def swap_case(s):
  return ''.join(map(change,s))

s= input()
result = swap_case(s)
print(result)

#Given the names and grades for eah student in aPhysics class of N students 
#store them in a nested list and print the names of any student having the second lowest grade
#Note: if there are multiple students with the lowest grade. Order them alfabetically

dic = {}
s = list()
 for _ in range(int(input())):
    name = input()
    score = float(input())
#The code checks if the entered score already exists in the dictionary.
#If it does, the student's name is appended to the list of names for that score. 
#Otherwise, a new key-value pair is added to the dictionary with the score as the key and a list containing the student's name as the value.
    if score in dic:
      dic[score].append(name)
    else:
      dic[score] = [name] 
#The code checks if the score is already in the list of unique scores (s). If not, it appends the score to the list.
    if score not in s:
      s.append(score)
m=min(s)    
s.remove(m)
m1=min(s)

dic[m1].sort()
for i in dic[m1]:
  print(i)



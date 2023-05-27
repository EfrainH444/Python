#Given the participants score sheet for your University Sports Day. You are
#required to find the runner up score. You are given N scores. Store them in a list and find the runner up (subcampeón)

n = int(raw_input())
arr = map(int,raw_input().split())
a = max(arr)
c = count(a)

for i in range(c):
  arr.remove(a)
  
print(max(arr))

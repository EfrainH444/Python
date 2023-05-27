#Given an integer n, and n space-separated integers as input, create a tuple t of those n integers
#Then compute and print the results of hash(t)

n = int(input())
integer_list = tuple(map(int, input().split()))
print(hash(integer_list))

#####################
######## MAP ########
#The map() function takes two parameters:
#function: It specifies the function to be applied to each item of the iterable. This can be a built-in function or a custom-defined function.
#iterable: It represents the iterable object (e.g., list, tuple, string) that the map() function will iterate over.
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))

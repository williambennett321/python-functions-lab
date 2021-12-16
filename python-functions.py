# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  num_list = []
  for num in range(n):
    num_list.append(num)
  total_list = sum(num_list, n)
  print(total_list)


sum_to(10)


print("----------------------------------------------------------------------------")

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

num_list = []

def largest(num_list):
  num_list.sort()
  largest_val = num_list[-1]
  print(largest_val)

largest([10, 4, 2, 231, 91, 54])



print("----------------------------------------------------------------------------")
# 3. Write a function named `occurances` that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurrences(str1, str2):
  count_value = str1.count(str2)
  print(count_value)

occurrences("fleep floop", "e")
occurrences("fleep floop", "p")
occurrences("fleep floop", "ee")
occurrences("fleep floop", "fe")



print("----------------------------------------------------------------------------")

# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*args):
  total = 1
  for num in args:
    total *= num
  print(total)

product(-1,4)
product(2, 5, 5) 
product(4, 0.5, 5) 




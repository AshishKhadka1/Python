# Write a program that asks the user for a number and prints whether it's positive, negative, or zero.

a = float(input("Enter a number: "))

if a > 0:
    print('positive')
elif a < 0:
    print('Negative')
else:
    print('Zero')

# Ask the user for a number and print its multiplication table up to 10.

num = int(input("Enter a number to see its multiplication table: "))

print(f"Multiplication Table of {num}")

for i in range(1,10):
    print(f"{num} * {i} = {num * i}")

# Write a function find_maximum(num_list) that takes a list of numbers and returns the largest number (without using max()).

def find_maximum(num_list):
  if not num_list:
      return None
  
  largest = num_list[0]
  for num in num_list:
    if num > num_list:
      largest = num
      return largest
  
  
#   - For numbers 1 to 100:
#     - If divisible by 3, print "Fizz"
#     - If divisible by 5, print "Buzz"
#     - If divisible by both 3 and 5, print "FizzBuzz"
#     - Otherwise, print the number.

for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0:
        print ('FizzBuzz')
    elif i % 3:
        print ('Fizz')
    elif i % 5:
        print ('Bizz')
    else:
        print (i)
        
# Write a function reverse_string(s) that returns the reverse of a given string (without using [::-1] or reversed()).
      
def reverse_string(s):
    reversed_str = ""

    for char in s:
        reversed_str = char + reversed_str

    return reversed_str

print(reverse_string("man"))

# Write a program that counts the number of vowels (a, e, i, o, u) in a user-input string.

text = input("enter a String ")

count = 0
vowels = 'aeoiuAEIOU'

for char in text:
    if char in vowels:
        count += 1
        print ("Number of Vowels:", count )
        

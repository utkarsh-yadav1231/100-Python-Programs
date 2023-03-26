# 101. Below python codes are some of the compiled solutions of workattech Beginner-level-problems

# -------------------------------------------------------------------------------------------------------------------------

# Write a program to print numbers from 1 - 10 with each number printed in a separate line.
for i in range(1,11) : print(i)

# -------------------------------------------------------------------------------------------------------------------------
# Write a program to print the sum of the first 10 numbers (1-10).
sum = 0
for i in range(1,11): sum+=i
print(sum)

# -------------------------------------------------------------------------------------------------------------------------
# Simple Interest
p, r, t = [float(a) for a in input().split()]
interest = (p * r * t)/100
print(f'{interest:.6f}')

# -------------------------------------------------------------------------------------------------------------------------
# Candies
    #Input Format
    #A single line with two space-separated integers representing the number of candies and the number of cousins repectively.
    #Output Format
    #Print "YES" if you can equally distribute the candies and "NO" if you cannot.

a, b = [int(x) for x in input().split()]
if a%b==0 :
	print("YES")
else:
	print("NO")

# -------------------------------------------------------------------------------------------------------------------------
# Milkman
# Your mother has sent you to the milkman with a cylindrical bottle. 
# You have to pay the milkman the price for the bottle full of milk at a rate of ₹40 per litre of milk. 
# You are given the radius (r) and the height (h) of the bottle in centimetres. You can assume the value of π as 3.14.
# Formula for volume of cylinder: V=π r2h

# Also, 1 litre = 1000 cm3.

# Input Format
# 1 line containing two space separated integers - the radius and the height of the bottle (in centimetres).

# Output Format
# The amount you need to pay to the milkman in rupees, accurate upto exactly 2 decimal places.

r, h = [int(x) for x in input().split() ]
volume = (3.14 * r * r * h)
print(f'{volume * pow(10,-3) * 40:.2f}')

# -------------------------------------------------------------------------------------------------------------------------
# Average Weight
# Input Format
# A single line with 10 space separated weights
# w1 w2 w3 w4 w5 w6 w7 w8 w9 w10

# Output Format
# A single value - The average weight
# The value should be accurate upto exactly 6 decimal places.

lst = []
nsum = 0
lst = [float(x) for x in input().split()]
for xn in lst: nsum+=xn
avg = nsum/10
print(f'{avg:.6f}')

# -------------------------------------------------------------------------------------------------------------------------
# Print Digits
# Given a two-digit number n, print both the digits of the number.

# Input Format
# The first line indicating the number of test cases T.
# Next T lines will each contain a single number ni.

# Output Format
# T lines each containing two digits of the number ni separated by space.

T = int(input())
for i in range(T):
	num = int(input())
	lst = []
	while num>0:
		lst.insert(0,num%10)
		num = int(num/10)
	
	for x in lst:
		print(x, end =" ")
	print("")
		
# -------------------------------------------------------------------------------------------------------------------------
# Temperature Conversion

# Formula for conversion: Temp (℉) = (9t / 5) + 32

# Input Format
# The first line indicating the number of test cases T
# Next T lines contains the temperature in Centigrade - ti (can be decimal values).

# Output Format
# T lines each indicating the temperature in fahrenheit.
# The fahrenheit values are accurate to upto exactly 2 decimal places.
T = int(input())
for i in range(T):
	cel = float(input())
	fah = ((9 * cel)/5) + 32
	print(f'{fah:.2f}')

# -------------------------------------------------------------------------------------------------------------------------
# Triangle
# Given three sticks with lengths L1, L2, L3 - find out if these sticks can form a triangle.

# If they can form a triangle, calculate the circumference of the triangle.

# Circumference of a triangle (C) = L1 + L2 + L3

# The condition to be satisfied for three sticks to form a triangle is that the sum of lengths of any two sides of the triangle should be greater than or equal to the length of the third side.

# Examples
# Sides: 3, 4, 5
# Here, if you pick any 2 sides, its sum will be greater than the remaining side.

# Sides: 1, 2, 4
# Here, 1 + 2 < 4. Therefore, this cannot form a triangle.

# Input Format
# There are multiple test cases in this problem.

# First line has a number T representing the number of test cases.

# The next T lines each represent a test case and have three space-separated integers representing the lengths of the sticks.

# Output Format
# T lines, one for each test case.

# If the three side can't form a triangle, print "-1".

# If the three sides can form a triangle, print "<Circumference>"
# Write your code here
N = int(input())
for i in range(N):
	a,b,c = [int(x) for x in input().split()]
	if a+b>=c and a+c>=b and b+c>=a: 
		sum = a+b+c
		print(str(sum))
	else:
		print("-1")

# -------------------------------------------------------------------------------------------------------------------------
# Number Reversal
# Input Format
# A single line containing a 3 digit number n.

# Output Format
# The number generated by reversing the digits.

# Write your code here
num = int(input())
rev = 0
while num>0:
	rev = rev*10 + num%10
	num = int(num/10)
	
print(rev)
	

# -------------------------------------------------------------------------------------------------------------------------
# Add One
# You are given the name and age of a person as input. You want to say "Hello" to that person along with what their age will be after one year.
# Write your code here
name,age = input().split()
age = int(age)
age+=1
reply = "Hello {0}! Next year, you will be {1} years old"

print(reply.format(name,age))


# -------------------------------------------------------------------------------------------------------------------------
# Reverse Order
# Given a set of numbers, print them in the reversed order.

# Input Format
# First lines containing the number of numbers n

# Second line containing all the n numbers a1 a2 a3 . . . . an

# Output Format
# A single line containing the numbers in the reversed order an an-1 an-2 . . . .a1
# Write your code here
T = int(input())
lst = [int(x) for x in input().split()]
lst.reverse()
for i in lst:
	print(i, end = " ")


# -------------------------------------------------------------------------------------------------------------------------
# Weather
# Given the temperature and humidity for the day, determine which category the day's weather falls into.
# Write your code here
T = int(input())

for i in range(T):
	temp, hum = [int(x) for x in input().split()]
	if temp>=30 and hum>=90 : print("Hot and Humid")
	if temp>=30 and hum<90 : print("Hot")
	if temp<30 and hum>=90 : print("Cool and Humid")
	if temp<30 and hum<90 : print("Cool")


# -------------------------------------------------------------------------------------------------------------------------
# Palindrome
def check_palindrome(mystr):
	lo = 0
	hi = len(mystr)-1

	while lo<hi :
		if mystr[lo] != mystr[hi] : return False
		lo+=1
		hi-=1
	return True
	
# Write your code here
T = int(input())
for i in range(T):
	s = input()
	print(check_palindrome(s))


# -------------------------------------------------------------------------------------------------------------------------
# Multiplication Table
# Given a number n, you have to print the multiplication table of n till the 10th multiple.
def print_table(num):
	for i in range(1,11): print(i*num, end=" ")
	print()
	
# Write your code here
T = int(input())
for i in range(T):
	num = int(input())
	print_table(num)


# -------------------------------------------------------------------------------------------------------------------------
# Star Pattern 1
# Print the following pattern to the output.
# *
# **
# ***
# ****
# *****

# Write your code here
row, col = 5, 5

for r in range(1, row+1):
	for c in range(1, col+1):
		if c<=r : print("*", end = "")
	print()


# -------------------------------------------------------------------------------------------------------------------------
# Vowels
# Input Format
# First line has a number n representing the number of your friends.
# n lines follow with the first name of each of your friends all in separate lines.
# Output Format
# n lines, each indicating the number of candies the person received.

def vowel(name):
	lst = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
	vow = 0
	for s in name: 
		if s in lst: vow += 1
	return vow 

# Write your code here
N = int(input())
for i in range(N):
	name = input()
	print(vowel(name))


# -------------------------------------------------------------------------------------------------------------------------
# Pastries
# Input Format
# First line has two numbers n representing the number of pastries that you have at the beginning and q representing the number of customers in the queue.
# Next q lines will have a number pi representing the number of pastries the ith customer wants.

# Output Format
# One line for each customer.
# "Enjoy your dessert!" if you can serve that customer.
# "Sorry, we are all out!" if you cannot serve that customer
# Write your code here
limit, T = [int(x) for x in input().split()]
left = limit
for i in range(T):
	demand = int(input())
	
	if demand <= left : print("Enjoy your dessert!")
	elif demand > left and left>0 : print("Enjoy your dessert!")
	else : print("Sorry, we are all out!")
	
	left -= demand

# -------------------------------------------------------------------------------------------------------------------------
# Words in Sentence
# Sample Input
# The quick brown fox jumped over the lazy dog.
# Expected Output
# 9
# Write your code here
line = input()
space = 0
for i in line:
	if i == " ": space+=1
	
print(space+1)


# -------------------------------------------------------------------------------------------------------------------------
# Percentage
# You just saw all your answer scripts after correction at school but haven't received a report card yet. 
# So, you want to find out the percentage that you scored. Assume the total marks for each subject to be 80.
# Write your code here
N = int(input())
total_marks = N*80
i = 0
marks = 0
while i<N:
	marks += int(input())
	i+=1

perc = (marks/total_marks)*100
print(f'{perc:.2f}' + "%")


# -------------------------------------------------------------------------------------------------------------------------
# Max in Matrix
# Given an integer matrix (2D array) of dimension m*n (m rows, n columns), find out the largest integer in the entire matrix.
# Write your code here
row, col = input().split()
row = int(row)
largest = 0

for r in range(row):
	col_list = [int(x) for x in input().split()]
	for c in col_list:
		if c > largest : largest = c
	col_list.clear()
		
print(largest)


# -------------------------------------------------------------------------------------------------------------------------
# Adjacent Zeros
# A binary number is a number composed of 0s and 1s.
# Given a binary number, check if the number has adjacent zeroes or not, i.e., if two zeroes are present side by side or not.

# Write your code here
T = int(input())
flag = False
while T>0 :
	bnum = input()
	i,j = 0,1
	while(len(bnum)>1 and j<len(bnum)):
		if bnum[i] == "0" and bnum[j] == "0": 
			flag = True
			break
		j+=1
		i+=1
	if flag == True : print("Yes")
	else : print("No") 
	flag = False
	T-=1


# -------------------------------------------------------------------------------------------------------------------------
# Digit Sum
# Given a number, find the sum of its digits.
# If the number is represented as d1d2d3d4d5, then the sum will be d1 + d2 + d3 + d4 + d5.
# Write your code here
T = int(input())
while T>0 :
	num = str(input())
	sum = 0
	idx = 0
	while(idx < len(num)):
		sum += int(num[idx])
		idx+=1
	print(sum)
	T-=1


# -------------------------------------------------------------------------------------------------------------------------
# Fibonacci Series
# Given a number (n), print the first n fibonacci numbers.
# Write your code here
def fib(num):
	if(num == 0 or num == 1): return num
	return fib(num-2) + fib(num-1)

T = int(input())
while(T>0):
	num = int(input())
	first, second = 0, 1
	result = 0
	for i in range(num):
		if i<=1 : result = i
		else : 
			result = first + second
			first = second
			second = result
		
		print(result, end=" ")
		
	print()
	T-=1

# -------------------------------------------------------------------------------------------------------------------------
# N Factorial
# Factorial of 5 is 1*2*3*4*5 = 120.
# Write your code here
T = int(input())
while T>0 :
	num = int(input())
	fact = 1
	for i in range(1, num+1):
		fact *= i
	print(fact)
	T-=1

# -------------------------------------------------------------------------------------------------------------------------
# Net Salary
# The net salary of a person is (Gross Salary - Tax).

# There are different tax slabs for computing the tax.
# Tax Rates for different income:

# Slab 1 → 0 to 300000: 0%
# Slab 2 → 300001 to 500000: 5%
# Slab 3 → 500001 to 1000000: 20%
# Slab 4 → 1000001+: 30%

# Tax = 0% of Slab 1 + 5% of Slab 2 + 20% of Slab 3 + 30% of Slab 4
# Net Salary = Gross Salary - Tax
# Write your code here
T = int(input())

while T>0:
	gross = int(input())
	ctc = gross
	slab1, slab2, slab3, slab4 = 0,0,0,0
	if ctc <= 300000:
		slab1 = 300000
	elif ctc <= 500000: 
		slab1 = 300000
		slab2 = ctc-300000
	elif ctc <= 1000000: 
		slab1 = 300000
		slab2 = 200000
		slab3 = ctc - 500000
	else: 
		slab1 = 300000
		slab2 = 200000
		slab3 = 500000
		slab4 = ctc - 1000000

	tax = ((0/100) * slab1) + ((5/100) * slab2) + ((20/100) * slab3) + ((30/100) * slab4) 
	gross = float(gross)
	net_salary = gross - tax
	print(f'{net_salary:.2f}')
	T-=1



# -------------------------------------------------------------------------------------------------------------------------
# Toggle Case
# Given a string consisting of a mix of uppercase and lowercase characters, toggle the case of each character and print the resultant string.
# The string contains only lowercase and uppercase letters.

# Write your code here
T = int(input())

while T>0:
	s = input()
	s2 = ""
	lo, slen = 0, len(s) 
	while(lo<slen):
		if s[lo].isupper() : s2 += s[lo].lower()
		else: s2 += s[lo].upper()
		lo+=1
	
	print(s2)
	T-=1


# -------------------------------------------------------------------------------------------------------------------------
# Reverse Array
# Given an array, reverse it.
# Write your code here
N = int(input())
try:
	lst = [int(x) for x in input().split()]
	lst.reverse()
	for x in lst: print(x, end=" ")
except:
	pass


# -------------------------------------------------------------------------------------------------------------------------
# Is Sorted Array?
def call_function():
	slen = int(input())
	lst = [int(x) for x in input().split()]
	i = 1
	flag = False
	
	while (i<slen):
		if lst[i-1]>lst[i] : flag = True 
		i+=1
		
	if flag == True : print("No") 
	else :	print("Yes")
	flag = False
	
# Driver Code
if __name__ == "__main__":
	try:
		T = int(input())
		while T>0:	
			call_function()
		T-=1
	except:
		pass


# -------------------------------------------------------------------------------------------------------------------------
# Swap Adjacent Elements
# Given an array of integers, swap the elements in pairs.

# Examples
# Array: [1, 2, 3, 4, 5, 6, 7, 8]
# After swap: [2, 1, 4, 3, 6, 5, 8, 7]

# Array: [5, 2, 7, 8, 6, 3, 1]
# After swap: [2, 5, 8, 7, 3, 6, 1]

def swapList(sl,pos1,pos2):      
    sl[pos1], sl[pos2] = sl[pos2], sl[pos1]  
    return sl
# Write your code here
N = int(input())
try:
	lst = []
	lst = [int(x) for x in input().split()]

	i, j, slen = 0, 1, len(lst)

	while(j<slen):
		lst = swapList(lst, i, j)
		i+=2
		j+=2

	for p in lst:
		print(p, end=" ")
except:
	pass

# -------------------------------------------------------------------------------------------------------------------------




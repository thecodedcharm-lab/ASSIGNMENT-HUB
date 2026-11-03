# Topic-1 — Comparison Operators


# Q1. Predict the Output
a = 15
b = 20
print(a < b)
print(a > b)
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)
# True
# False
# False
# True
# True
# False

# Q2. Compare Expressions
x = 10
y = 10
print(x == y)
print(x != y)
print(x < y)
print(x <= y)
print(x >= y)
# True
# False
# False
# True
# True

# Q3. Comparison with Arithmetic
a = 10
b = 5
print(a + b == 15)
print(a * b > 40)
print(a - b != 5)
print(a // b == 2)
# True
# True
# False
# True

# Q4. String Comparison
# Predict the output:
print("Python" == "Python")
print("Python" == "python")
print("Hello" != "hello")
# True
# False
# True


# Topic-2 — Assignment Operators


# Q5. Trace the Value
# Predict the final value of x:
# Write the value of x after each statement.
x = 20
x += 10
print(x) # 30
x -= 5
print(x) # 25
x *= 2
print(x) # 50
x //= 5
print(x) # 10

# Q6. Assignment Operator Practice
# Start with:
marks = 50
# Use assignment operators to:
# Increase marks by 10
# Decrease marks by 5
# Multiply marks by 2
# Print the final value.
marks = 20
marks += 10
marks -= 5
marks *= 2
marks //= 5
print(marks)
#10


# Topic-3 — Membership Operators with Strings


# Q7. Basic Membership
# Predict the output:
text = "Python Programming"
print("Python" in text)
print("Java" in text)
print("Python" not in text)
# True
# False
# False

# Q8. Character Membership
# Given:
word = "computer"
# Write expressions to check:
# Whether "p" is present.
# Whether "x" is present.
# Whether "c" is not present.
print("p" in word)
print("x" in word)
print("c" not in word)
# True
# False
# False

# Q9. Case Sensitivity in Membership
# Predict the output:
text = "Python"
print("P" in text)
print("p" in text)
print("Python" in text)
print("python" in text)
True
False
True
False

# Q10. Membership with User Input
# Take a word or sentence as input and check whether the character "a" occurs in it.
word=input("Enter Your Word : ")
print("a" in text)

# Q11. Email Symbol Check
# Take an email address as input and check whether "@" is present.
Email=input("Enter Your Email : ")
print("@" in Email)


# Topic-4 — ASCII and Unicode


# Q12. Find Character Codes
# Use ord() to find the Unicode code point of:
# A
# a
# Z
# z
# 0
# 9
# @
print(ord("A")) # 65
print(ord("a")) # 97
print(ord("Z")) # 90
print(ord("z")) # 122
print(ord("0")) # 48
print(ord("9")) # 57
print(ord("@")) # 64

# Q13. Convert Codes to Characters
# Use chr() to find the character represented by:
# 65
# 66
# 97
# 98
# 48
# 57
# 64
print(chr(65)) # A
print(chr(66)) # B
print(chr(97)) # a
print(chr(98)) # b
print(chr(48)) # 0
print(chr(57)) # 9
print(chr(64)) # @

# Q14. Uppercase and Lowercase
# Use ord() to find the code points of:

# A
# a
# B
# b
# Answer:
print(ord("A")) # 65
print(ord("a")) # 97
print(ord("B")) # 66
print(ord("b")) # 98
# Which is larger: ord("A") or ord("a")? a because its UNICODE is greater than A 
# What is the difference between them? a has UNICODE 97 while A has UNICODE 65 its has difference of 32
# Is the difference the same for B and b? yes ,b has UNICODE 98 while B has UNICODE 66 its has difference of 32

# Q15. Character Code Program
# Take one character as input and print its Unicode code point.
word=input("Enter Your Character: ")
print(ord(word))

# Q16. Next Character
# Take a single uppercase English letter as input.
# Use ord() and chr() to print the next character.
char = input("Your Character : ")
next_char = chr(ord(char) + 1)
print("Next Character : ", next_char)

# Q17. Character Comparison and Unicode
# Predict the output:
print("A" < "B") #True
print("a" < "b") #True
print("A" < "a") #False
print("0" < "9") #True
# Then use ord() to understand why the results occur.
print(ord("A")) # 65
print(ord("B")) # 66
print(ord("a")) # 97
print(ord("b")) # 98
print(ord("9")) # 57
print(ord("@")) # 64

# Q18. Unicode Character Challenge
# Use chr() to display the characters represented by:
print(chr(9731)) #☃
print(chr(9829)) #♥
print(chr(8377)) #₹
# Then use ord() on those characters to verify the values.
print(ord("☃")) # 9731
print(ord("♥")) # 9829
print(ord("₹")) # 8377


# Topic-5 — String Indexing


# Q19. Basic Indexing
text = "PYTHON"
# First character
print(text[0]) #p
# Second character
print(text[1]) #Y
# Last character
print(text[-1]) #N
# Second-last character
print(text[-2]) #O

# Q20. Positive and Negative Indexing
text = "COMPUTER"
# Find the characters at:
# 0
# 3
# -1
# -3
print(text[0]) #C
print(text[3]) #P
print(text[-1]) #R
print(text[-3]) #T

# Q21. Predict the Output
text = "PYTHON"
print(text[0])  #P
print(text[2])  #T
print(text[-1]) #N
print(text[-2]) #O

# Q22. Indexing a User Input
# Take a word from the user and print:
# First character
# Last character
text=input("Enter Your Text : ")
print(text[0] , "and" , text[-1])  

# Q23. Think Carefully About Indexing
word = "PROGRAM"
# Without running the code, determine:
print(word[0])  #P
print(word[2])  #O
print(word[-1]) #M
print(word[-4]) #G


# Topic-6 — String Slicing


text = "PYTHON"
print(text[0:3])#PYT
print(text[2:5])#THO
print(text[1:6])#YTHON

# Q25. Start and Stop
# Predict:
text = "PROGRAMMING"
print(text[:4]) #PROG
print(text[4:]) #RAMMING
print(text[:])  #PROGRAMMING

# Q26. Negative Slicing
text = "COMPUTER"
print(text[-5:])   #PUTER
print(text[:-3])   #COMPU
print(text[-6:-2]) #MPUT

# Q27. Step in Slicing
text = "PYTHON"
print(text[::2])  #PTO
print(text[1::2]) #YHN
print(text[::-1]) #NOHTYP

# Q28. Reverse a String
# Take a string as input and reverse it using slicing.
word=input("Enter Your Word : ")
print(word[::-1])

# Q29. Alternate Characters
# Take a string as input and print every second character starting from index 0.
word=input("Enter Your Word : ")
print(word[::2])

# Q30. Extract First and Last Three Characters
# Take a string as input and print:
word=input("Enter Your Word : ")
# First three characters
print(word[0:3])
# Last three characters
print(word[-1:-4])

# Q31. Slicing Challenge
text = "ABCDEFGHIJ"
print(text[2:8:2])  # CEG
#start: 2    stop: 8    step: 2    
print(text[8:2:-2]) # IGE
#start: 8    stop: 2    step:-2    
print(text[::-2])   # JHFDB
#start: 0    stop:10     step:-2   

# Q32. Slice Without Counting from the Beginning
text = "BTECH-CSE-2026"
# Use slicing to extract:
# BTECH
print(text[0:5]) 
# CSE
print(text[6:9]) 
# 2026
print(text[10:14]) 


# Topic-7 — String split()


# Q33. Basic split()
# Predict the output:
text = "Python is easy"
print(text.split()) # ['Python', 'is', 'easy']
# Explain what separates the words.
# split() breaks a string into separate pieces and puts them inside a list.
# By default, split() separates words wherever there is whitespace, usually a space " "

# 34. Custom Separator
# Predict the output:
data = "apple,banana,mango"
print(data.split(",")) #['apple', 'banana', 'mango']

# Q35. Separator Not Present
# Predict the output:
text = "Python is easy"
print(text.split(",")) #['Python is easy']
# Why does it not split at the spaces?
# Because our split function is comma (.split(",")) not space (.split())

# Q36. Split a Full Name
text=input("Enter Your Text : ") #Rahul Kumar Sharma
print(text.split()) #['Rahul', 'Kumar', 'Sharma']

# 37. Multiple Inputs Using split()
# Take two values from the user in one line.
first_name, last_name = input("first_name last_name: ").split()
print("First Name:", first_name)
print("Last Name:", last_name)

# Q38. Three Numeric Inputs
# Take three integers in one line using .split().
first_number, second_number, third_number = input("Enter Any Three Number With Space : ").split()
print("SUM OF THREE NUMBER : ", int(first_number)+ int(second_number)+int(third_number))

# Q39. Student Record
Name, Age, Course, City = input("ENTER YOUR Name, Age, Course, City with comma ").split(",") #Rahul,20,BTech,Ahmedabad
print("Name: ",Name )        # Name:  Rahul  
print("Age: ",Age )          # Age:  20
print("Course: ",Course )    # Course:  BTech
print("City: ",City )        # City:  Ahmedabad

# Q40. Email Analyzer
Username, Domain= input("Enter Your Email : ").split("@") #student@yahoo.com
print("Username : ", Username) #student
print("Domain : ", Domain) #yahoo.com

# Q41. Sentence Analyzer
sentence = input("Enter a sentence: ")           #Python is very powerful
words = sentence.split()
print("First word:", words[0])                   #Python
print("Last word:", words[-1])                   #powerful
print("Total number of words:", len(words))      #4


# Topic-8 — Escape Sequences


# Q42. New Line
# Write a statement that produces exactly:
print("Hello\nWorld")
# Hello
# World

# Q43. Tab
# Write a program that produces:
print("Name:\tRahul")         #Name:   Rahul
print("Age:\t20")             #Age:    20
print("City:\tAhmedabad")     #City:   Ahmedabad

# Q44. Backslash
# Write a program that displays exactly:
# C:\Python\Programs
print("c:\\Python\\Programs")

# Q45. Single Quote
# Write a statement that displays:
# It's Python
print("It\'s Python")
# Use an appropriate escape sequence.

# Q46. Double Quote
# Write a statement that displays:
# He said "Hello"
print("He said \"Hello\"")

# Q47. Predict the Output
print("Python\nProgramming") 
#Python  
#Programming

# Q48. Combined Escape Sequences
# Write a program that displays:
Name, Age, Course = "Rahul", 20, "B.Tech"
print("Student Details\n\nName :\t",Name, "\nAge :\t", Age, "\nCourse:\t", Course )
# Name:    Rahul 
# Age:     20 
# Course:  B.Tech


# Topic-9 — print(), sep, end, and f-Strings


# Q49. sep
# Predict the output:
print("2026", "09", "09", sep="-") #2026-09-09

# Q50. end
# Predict the output:
print("Hello", end=" ")
print("Python")
#Hello Python

# Q51. sep and end
# Use sep and end.
# Write a program that produces exactly:
# 10-20-30
# 40-50-60
print(10, 20, 30, sep="-", end="\n")
print(40, 50, 60, sep="-")

# Q52. Student Introduction
# Display them using an f-string:
Name, Age, City, Course = "Rahul", 20 , "Ahmedabad", "B.Tech"
print(f"Name : {Name}", f"Age : {Age}", f"City : {City}", f"Course : {Course}", sep="\n")
# Name : Rahul
# Age : 20
# City : Ahmedabad
# Course : B.Tech

# Q53. Formatted Price
# Take a price as input and display it with exactly two decimal places.
# Use an f-string.
price = float(input("Enter price: "))
print(f"{price:.2f}")
# Remember: .2f = exactly 2 digits after the decimal point.


# Topic-10 — Debugging


# Q54. String and Integer
# Find and correct the error:
age = input("Enter age: ")
print("Age after 5 years:", int(age) + 5)

# Q55. Incorrect Quotes
# Find and correct the error:
print("It's Python'")

# Q56. Incorrect Slicing Syntax
# Find and correct the error:
text = "Python"
print(text[1:4])

# Q57. Incorrect split() Separator
# The program is:
# a, b = input().split(",")
# The user enters:10 20
# Why does the program fail?
# THE SEPARATOR FUNCTION IS COMMA NOT SPACE
# Rewrite it correctly for the given input.
a, b = input("").split()
print(a, b)

# Q58. String Addition vs Numeric Addition
a, b = input("").split()
print(int(a) + int(b))

# Q59. Escape Sequence Debugging
# Find and correct the problem:
print("C:\\new\\test")


# Topic-11 — Integrated Problems


# Q60. Student Result Information
# Take
# Student name 
name = input("Student name : ")
marks = input("write your 3 subject marks with space : ").split()
# Three subject marks
m1 = int(marks[0])
m2 = int(marks[1])
m3 = int(marks[2])
# Calculate:
# Total
# Average
total = m1 + m2 + m3
average = total / 3
# Display the student's information using an f-string.
print(f"Name: {name}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")

# Q61. Student ID Analyzer
# A student enters:
# BTECH-24-CSE-105
# Write a program that:
# Takes the ID as input.
# Uses .split("-") to separate the parts.
# Displays:
# Degree
# Batch
# Branch
# Roll Number
# Uses string slicing to extract the last three characters from the original ID.
# Converts the roll number into an integer.
# Prints the roll number.
Student_ID = input("Write in this form Degree-Batch-Branch-Roll Number: ")
parts = Student_ID.split("-")
degree = parts[0]
batch = parts[1]
branch = parts[2]
roll_number = Student_ID[-3:]
roll_number = int(roll_number)
print(f"Degree : {degree}")
print(f"Batch : {batch}")
print(f"Branch : {branch}")
print(f"Roll Number : {roll_number}")

# Q62. Username Generator
# Take a three-word full name:   #Rahul Kumar Sharma
# Use .split() and string indexing/slicing to create: #rahul.sharma
Full_name="Rahul Kumar Sharma".split()
Username = Full_name[0] +"."+ Full_name[2]
print(Username)

# Q63. Sentence Information
Text= input("Enter Your Text : ")#Python is very powerful
# Use .split() and string indexing to display:
word=Text.split()
print ("First word : ",word[0])    # First word: Python
print ("Last word : ",word[-1])    # Last word: powerful
print("Number of words:", len(word))# display the number of words.

# Q64. Email Analyzer + Membership
# Take an email address as input.
Email=input("Enter Your Email : ")#rahul@gmail.com
# Membership operator to check for "@"
print("@" in Email)
# .split("@")
Username, Domain=Email.split("@")
print("Username : ", Username) #rahul
print("Domain : ", Domain) #gmail.com

# Q65. Character Analyzer
# Take one character from the user.
character = input("Enter your character : ")
print("code : ",(character))
# Unicode code point
print("character : ",ord(character))
# Previous character
Previous_character=chr(int(ord(character))-1)
print("Previous_character : ",(Previous_character))
# Next character
Next_character=chr(int(ord(character))+1)
print("Next_character : ",(Next_character))

# Q66. Product Bill
Product_name = (input("Product : "))
Price =float(input("Price : "))
Quantity =int(input("Quantity : "))
Discount_percentage =float(input("Discount : "))
Subtotal = Price * Quantity
Discount = Subtotal * Discount_percentage / 100
Final_Total = Subtotal - Discount
print(f"Product : {Product_name}", f"Price : {Price}", f"Quantity : {Quantity}", f"Discount : {Discount}", f"Subtotal : {Subtotal}", f"Price : {Price}", f"Final_Total : {Final_Total}", sep="\n" )

# Q67. Date Analyzer
Date=input("DATE : ").split("-") #09-09-2026
Day=Date[0]
Month=Date[1]
Year=Date[2]
print (f"Day : {Day}",f"Month : {Month}",  f"Year : {Year}", sep="\n")

# Q68. String Transformation Challenge
Text=input("Enter Your Text : ").split()       #Python Programming
print(f"First Word: {Text[0]}", f"Second Word: {Text[1]}", sep="\n")
first_word=Text[0]
Second_word=Text[1]
print(f"First Word Reversed: {first_word[::-1]}", f"Second Word Reversed: {Second_word[::-1]}", sep="\n")

# Q69. Final Challenge — Student Code Formatter
Student_ID = input("Write in this form Degree-Batch-Branch-Roll Number: ") #BTECH-2026-CSE-105
parts = Student_ID.split("-")
degree = parts[0]
batch = parts[1]
branch = parts[2]
roll_number = Student_ID[-3:]
roll_number = int(roll_number)
print(f"Degree : {degree}")
print(f"Batch : {batch}")
print(f"Branch : {branch}")
print(f"Roll Number : {roll_number}")
print(f"Code: {degree}\\{branch }\\{roll_number}")
# Degree : BTECH
# Batch : 2026
# Branch : CSE
# Roll Number : 105
# Code: BTECH\CSE\105

# Q70. Final String + Input/Output Challenge
name = input("full name : ") #Rahul Kumar Sharma
NAME = name.split()
print(f"Original : {name}", f"First Name : {NAME[0]}", f"Last Name : {NAME[-1]}", f"First Name (Upper Part) : {name[0:3:-1]}", f"Last Name (Lower Part) : {name[-1:-3:-1]}", f"Full Name Reversed {name[::-1]}", sep="\n")

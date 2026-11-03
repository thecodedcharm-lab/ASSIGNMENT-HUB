# Assignment-7
# Topic: Python While Loop


# Type 1: Output Guessing

# Level 1: Understand the Basic Flow
# Q1. Simple Counting

i = 1
while i <= 4:
    print(i)
    i += 1

# Predicted output:

# 1
# 2
# 3
# 4

# Q2. Counting by Two

n = 2
while n <= 8:
    print(n, end=" ")
    n += 2

# Predicted output:

# 2 4 6 8

# Q3. Reverse Counting

x = 5
while x >= 1:
    print(x, end=" ")
    x -= 1

# Predicted output:

# 5 4 3 2 1

# Q4. The Condition Is Initially False

count = 7
while count < 5:
    print("Hello")
    count += 1
print("Finished")

# Predicted output:

# Finished

# Level 2: Track the Order of Statements

# Q5. Update Before Printing

i = 1
while i <= 4:
    i += 1
    print(i, end=" ")

#  Predicted output:

# 2 3 4 5

#  Q6. Print After the Loop

n = 1
while n <= 3:
    print(n, end=" ")
    n += 1

print("Done")

#  Predicted output:

# 1 2 3 Done

#  Q7. Two Updates in One Iteration

x = 1
while x < 10:
    print(x, end=" ")
    x += 2
    x += 1

#  Predicted output:

# 1 4 7

# Q8. Change the Variable Before Checking Again

value = 10
while value > 0:
    value -= 3
    print(value, end=" ")

# Predicted output:

# 7 4 1 -2

# Level 3: Arithmetic and Accumulation

# Q9. Add the Counter Values

i = 1
total = 0
while i <= 4:
    total += i
    i += 1
print(total)

# Predicted output:

# 10

# Q10. Multiply During Each Iteration

n = 1
result = 1
while n <= 4:
    result *= 2
    n += 1

print(result)

# Predicted output:

# 16

# Q11. Use the Remainder Operator

n = 11

while n > 0:
    print(n % 3, end=" ")
    n -= 4

# Predicted output:

# 2 1 0    

# Q12. Integer Division
number = 583

while number > 0:
    print(number // 10, end=" ")
    number //= 10

# Predicted output:
# 58 5 0 

# Level 4: Conditions and Logical Thinking

# Q13. Print Only When a Condition Is True
i = 1

while i <= 6:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
# Predicted output:
# 2 4 6 


# Q14. A Conditional Expression Inside a Loop
n = 1

while n <= 5:
    print("Even" if n % 2 == 0 else "Odd", end=" ")
    n += 1
# Predicted output:
# Odd Even Odd Even Odd 

# Q15. The Condition Changes Inside the Loop
x = 1

while x < 10:
    print(x, end=" ")
    x *= 2
# Predicted output:
#  1 2 4 8 

# Q16. A Tricky Starting Value
i = 5

while i > 0:
    print(i, end=" ")
    i -= 2

print("Stop:", i)
# Predicted output:
# 5 3 1 Stop: -1

# Level 5: Strings and Tricky Cases


# Q17. Build a String Repeatedly
i = 1
result = ""
while i <= 4:
    result += "A"
    print(result)
    i += 1
# Predicted output:
# A
# AA
# AAA
# AAAA


# Q18. A String Variable Changes Each Time
word = "PY"
while len(word) < 6:
    print(word)
    word += "T"
print(word)
# Predicted output:
# PY
# PYT
# PYTT
# PYTTT
# PYTTTT

# Q19. Does the Loop Run at All?
x = 3
while x > 10:
    print("Inside")
    x += 1
print(x)
# Predicted output:
# 3

# Q20. Find the Problem
i = 1
while i <= 4:
    print(i, end=" ")
    i -= 1
print("Finished")

#  B. It prints 1 0 -1 -2 ... and continues indefinitely
# Because i decreases instead of increasing, it moves further 
# away from the termination condition (i <= 4), causing an infinite loop.

# # Day 02

# Type 2: Basic While Loop Problems — Statement Based

# Q21. Print Numbers from 1 to N

N = int(input("Enter Number : "))
i = 1 
while i <= N:      
    print(i)      
    i += 1

# Q22. Print Numbers from N to 1

N = int(input("Enter Number : "))
i = N
while i >= 1:      
    print(i)      
    i -= 1

# Q23. Print Even Numbers up to N

N = int(input("Enter Number : "))
i = 2 
while i <= N:      
    print(i)      
    i += 2

# Q24. Print Odd Numbers up to N

N = int(input("Enter Number : "))
i = 1
while i <= N:      
    print(i)      
    i += 2

# Q25. Print Multiples of a Number

K = int(input("K = "))
N = int(input("N = "))
current = 1

while current <= N:
    if current % K == 0:
        print(current)
    current += 1

# Level 2: Counting with Small Changes

# Q26. Multiplication Table

number = int(input("Enter Number : "))
count = 1

while count <= 10:
    print(f"{number} X {count} = {number * count}")
    count += 1

# Q27. Count by a Given Step

start = int(input("Enter START : "))
step = int(input("Enter STEP : "))
count = 1
while count <= 5:
    print(start)
    start += step 
    count += 1

# Q28. Sum of Numbers from 1 to N
num = int(input("Enter Number : "))
Sum = 0
while num >= 1:
    Sum=Sum+num
    num-=1
print(Sum)

# Q29. Sum of Even Numbers up to N
num = int(input("Enter Number : "))
Sum = 0
while num >= 1:
    if num % 2 == 0:
        Sum=Sum+num
    num-=1
print(Sum)

# Q30. Sum of Odd Numbers up to N
num = int(input("Enter Number : "))
Sum = 0
while num >= 1:
    if num % 2 != 0:
        Sum=Sum+num
    num-=1
print(Sum)

# # Level 3: Simple Repeated Calculations

# Q31. Calculate the Total Cost
price = int(input("PRICE = "))
qty = int(input("QUANTITY = "))
total_cost = 0  
count = 0
while count<qty:
    total_cost+=price
    count+=1
print(total_cost)

# Q32. Calculate Total Savings

DAILY_SAVING = int(input("DAILY_SAVING = "))
DAYS = int(input("DAYS = "))
total_amount=0
count=0
while count<DAYS:
    total_amount+=DAILY_SAVING
    count+=1
print(total_amount)

#  Q33. Calculate a Number Raised to a Power

BASE=int(input("BASE = "))
POWER=int(input("POWER = "))
result=1
count=0
while count<POWER:
    result *= BASE
    count+=1
print(result)

# Q34. Calculate Factorial

N = int(input("Enter Number : "))
result = 1
while N > 1:
    result *= N
    N -= 1
print(result)

# Q35. Find the Sum from START to END

start = int(input("START = "))
end = int(input("END = "))
sum=0
while start<=end:
    sum=sum+start
    start=start+1
print(sum)

Level 4: Read the Condition Carefully

# Q36. Count Down by Two

N = int(input("Enter Number : "))
while N >=2:
    print (N)
    N-=2

# Q37. Repeatedly Divide by Two

N = int(input("Enter Number : "))

while N > 0:
    N = N // 2  
    print(N)

# Q38. Count How Many Steps Are Needed

N = int(input("Number = "))
count=0
while N>=0:
    N-=3
    count+=1
print(count)
   
# Q39. Save Until the Target Is Reached

saved = int(input("SAVED = "))
daily_amount = int(input("DAILY_AMOUNT = "))
target = int(input("TARGET = "))
total_saving=saved
days=0
while total_saving<= target:
    total_saving+=daily_amount
    days+=1

print(days)

# Q40. Print a Number Sequence in Reverse Steps

start = int(input("START = "))
step = int(input("STEP = "))
while start>=0:
    print(start)
    start=start-step
 
# # DAY 03

# # Type 3: Factorial and Number & Digit Logic

# # Level 1: Basic Digit Logic

# Q41. Count the Digits
N = int(input("Enter Number : "))
count = 0
while N > 0:
    d = N % 10
    count += 1
    N //=10
print(count)

# Q42. Find the Sum of Digits
N = int(input("Enter Number : "))
sum = 0
while N > 0:
    d = N % 10
    sum += d
    N //= 10
print(sum)

# Q43. Reverse a Number
N = int(input("Enter Number : "))
reverse = 0
while N > 0:
    d = N % 10
    reverse = (reverse * 10) + d
    N = N // 10
print(reverse)

# Q44. Find the Product of Digits
N = int(input("Enter Number : "))
product = 1
while N > 0:
    d = N % 10
    product *= d
    N //= 10
print(product)

# Q45. Print Digits from Right to Left
N = int(input("Enter Number : "))
while N > 0:
    d = N % 10
    print(d)
    N //= 10

# # Level 2: Work with Specific Digits

# Q46. Find the First and Last Digit
N = int(input("Enter Number: "))
last_digit = N % 10
while N >= 10:
    N = N // 10
first_digit = N
print("First digit:", first_digit)
print("Last digit:", last_digit)

# Q47. Count Even Digits
N = int(input("Enter Number: "))
even_digit = 0
while N > 0:
    d = N % 10
    if d % 2 == 0:
        even_digit+=1
    N //= 10
print(even_digit)

# Q48. Count Odd Digits
N = int(input("Enter Number: "))
odd_digit = 0
while N > 0:
    d = N % 10
    if d % 2 != 0:
        odd_digit+=1
    N //= 10
print(odd_digit)

# Q49. Find the Sum of Even Digits
N = int(input("Enter Number: "))
even_digit_sum = 0
while N > 0:
    d = N % 10
    if d % 2 == 0:
        even_digit_sum+=d
    N //= 10
print(even_digit_sum)

# Q50. Find the Largest Digit
N = int(input("Enter Number: "))
largest = -1
while N > 0:
    d = N % 10
    if largest<d:
        largest=d
    N //= 10
print(largest)

# Q51. Find the Smallest Digit
N = int(input("Enter Number: "))
smallest = 9
while N > 0:
    d = N % 10
    if smallest>d:
        smallest=d
    N //= 10
print(smallest)

# # Level 3: Combine Digit Logic

# Q52. Check Whether a Number Is a Palindrome

N = int(input("Enter Number: "))
original_N=N
reverse = 0
while N > 0:
    d = N % 10
    reverse = (reverse * 10) + d
    N = N // 10
if reverse == original_N:
    print("Palindrome")
else:
    print("Not Palindrome")

# Q54. Check Whether All Digits Are the Same

N = int(input("Enter Number: "))
target_digit = N % 10
while N > 0:
    if N % 10 != target_digit:
        print("No")
        break
    N = N // 10
else:
    print("Yes")














# Day 04

### Level 1: Understand Nested while Loops

### Q59. Two Loops, Two Values


1 1
1 2
1 3
2 1
2 2
2 3


### Q60. Print Values on the Same Line


1 2
1 2
1 2

### Q61. Different Inner Loop Limits


*
* *
* * *


### Q62. Outer Value Changes the Inner Starting Point


1 2 3
2 3
3


### Q63. Print After the Inner Loop


1 2 End
1 2 End
1 2 End


## Level 2: Trace the Flow Carefully

### Q64. Print After Both Loops


2
3
3
4
Finished


### Q65. Two Separate while Loops

A 1
A 2
B 1
B 2
B 3


### Q66. Inner Counter Is Not Reset


1 1
1 2


### Q67. Update the Outer Variable After the Inner Loop

11
33


### Q68. Inner Loop Depends on the Outer Variable


X
1 X
1 2 X


## Level 3: Nested Loops with break

### Q69. Break the Inner Loop

1 1
1 2
2 1
2 2
3 1


### Q70. Break After Printing a Value

1 2 |
1 2 |


### Q71. Break Condition Is Never Reached

1 1
1 2
2 1
2 2


### Q72. break Does Not Stop the Outer Loop

1 1
Next row
2 1
Next row
3 1
Next row

## Level 4: Nested Loops with continue

### Q73. Skip One Inner-Loop Value

1 1
1 3
1 4
2 1
2 3
2 4


### Q74. Continue After Updating the Counter
  
2 4 5 6


### Q75. Continue in the Inner Loop

1 3 Row
1 3 Row
1 3 Row

### Q76. continue Does Not Skip the Whole Outer Loop


1 2
1 3
2 1
2 3
3 1
3 2

## Level 5: Combine Nested Loops, break, and continue

### Q77. Skip One Value, Then Break


1 1
1 3
2 1
2 3


### Q78. Predict the Complete Output

1 3 4 End
2 6 8 End
3 6 9 End
Done

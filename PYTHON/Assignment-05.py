# Important Rules

# Use exactly one for loop for every programming question.
# Do not use nested loops.
# Do not use while, break, or continue.
# You may use if, elif, and else inside the single for loop.
# Do not use lists, dictionaries, sets, or functions unless a question explicitly allows them.
# Do not hard-code the answer for the given test cases.
# Use % and // for number/digit problems where requested.
# For string questions, use indexing/slicing and character iteration where appropriate.
# If a question says without len(), do not use len().
# If a question says without max() / min(), do not use them.
# For output-prediction questions, do not run the code before predicting.
# Keep the solution limited to the concepts already taught in class.

# #     Level 1 — Loop Thinking & range()


##  Q1. Predict the Loop Values

for i in range(2, 15, 3):
    print(i)
    # 2, 5, 8, 11, 14

# Q2. Reverse range() Prediction

for i in range(15, 2, -3):
    print(i)
    # 15, 12, 9, 6, 3

# Q3. How Many Iterations?

for i in range(4, 31, 5):
    print(i)
    # 4 ,9 ,14 ,19 ,24 ,29

# Q4. Correct the Boundary

for i in range(3, 19, 3):
    print(i)

# Q5. Number and Distance from 20

for i in range(5,11):
    print(i,20-i)

# Q6. Number, Square and Cube

for i in range (1,7):
    print(i,i*i,i*i*i)

## Level 2 — Counting & Accumulation


# Q7. Sum of Numbers in a Range

start = int(input("Enter Number : "))
end = int(input("Enter Number : "))
sum = 0
for i in range(start,end+1):
    sum = sum + i
print(sum)

# Q8. Count Multiples of 3

N = int(input("Enter Number : "))
count = 0
for i in range (1,N+1):
    if i % 3 == 0:
        count=count+1
print(count)

# Q9. Sum of Multiples of 4

N = int(input("Enter Number : "))
Sum = 0
for i in range (1,N+1):
    if i % 4 == 0:
        Sum=Sum+i
print(Sum)

# Q10. Count Numbers with Two Conditions

N = int(input("Enter Number : "))
count = 0
for i in range (1,N+1):
    if i % 3 == 0 and i % 5 == 0:
        count=count+1
print(count)

# Q11. Sum Numbers Except Multiples of 3

N = int(input("Enter  Number : "))
sum = 0
for i in range (1,N+1):
    if i % 3 != 0:
        sum=sum+i
print(sum)

# Q12. Count Even and Odd Together

N = int(input("Enter Number : "))
even_count=0
odd_count=0
for i in range (1,N+1):
    if i % 2 == 0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print (even_count)
print (odd_count)

# Q13. Running Sum

N=int(input("Enter Number : "))
sum=0
for i in range (1,N+1):
    sum=sum+i
    print(sum)

# Q14. Running Product

N=int(input("Enter Number : "))
product = 1
for i in range (1,N+1):
    product=product*i
    print(product)

##     Level 3 — Factorial & Product Logic

# Q15. Factorial of a Number

N=int(input("Enter Number : "))
product=1
for i in range (1,N+1):
    product=product*i
print(product)

# Q16. Factorial from 1 to N

N=int(input("Enter Number : "))
product=1
for i in range (1,N+1):
    product=product*i 
    print(i,"! =",product)

# Q17. Product of Even Numbers

N=int(input("Enter Number : "))
product=1
for i in range (1,N+1):
    if i % 2 == 0:
        product=product*i
print(product)

# Q18. Product of Odd Numbers

N=int(input("Enter Number : "))
product=1
for i in range (1,N+1):
    if i % 2 != 0:
        product=product*i
print(product)

# Q19. Double Factorial — Even Numbers

N=int(input("Enter Number : "))
result=1
for i in range (N,0,-2):
    result=result*i
print(result)

# Q20. Sum of Squares

N = int(input("Enter Number : "))
sum_of_square=0
for i in range (1,N+1):
    sum_of_square=sum_of_square+i*i
print(sum_of_square)

# Q21. Sum of Cubes

N = int(input("Enter Number : "))
sum_of_cubes=0
for i in range (1,N+1):
    sum_of_cubes=sum_of_cubes+i*i*i 
print(sum_of_cubes)

# Q22. Factorial-Based Sum

N = int(input("Enter Number : "))
factorial=1
sum_of_factorial=0
for i in range (1,N+1):
    factorial=factorial*i
    sum_of_factorial=sum_of_factorial+factorial
print(sum_of_factorial)

##     Level 4 — Number & Digit Logic


# Q23. Count Digits Using a Loop

N = int(input("Enter Number : "))
N = abs(N)
count=0
import math
for i in range (int(math.log10(N))+2):
    count+=1
print(count)

# Q24. Sum of Digits

N = int(input("Enter Number : "))
last_digit=0
sum_of_digit=0
import math
for i in range (int(math.log10(N))+2):
    last_digit=N%10
    sum_of_digit=sum_of_digit+last_digit
    N=N//10
print(sum_of_digit)

# Q25. Product of Digits

N = int(input("Enter Number : "))
product_of_digit=1
import math
for i in range (1,int(math.log10(N))+2):
    last_digit=N%10
    product_of_digit=product_of_digit*last_digit
    N=N//10
print(product_of_digit)

# Q26. Count Even Digits

N = int(input("Enter Number : "))
N = abs(N)
even_count = 0
import math
for i in range(1, int(math.log10(N)) + 2):
    last_digit = N % 10
    if last_digit % 2 == 0:
        even_count = even_count + 1
    N = N // 10
print(even_count)

# Q27. Sum of Even Digits

N = int(input("Enter number : "))
N = abs(N)
even_sum = 0
import math
for i in range (int(math.log10(N))+2):
    last_digit = N % 10
    if last_digit % 2 == 0:
        even_sum = even_sum + last_digit
    N = N // 10
print(even_sum)

# Q28. Largest Digit Without max()

N = int(input("Enter number : "))
N = abs(N)
import math
Greatest=-1
for i in range (int(math.log10(N))+1):
    last_digit = N % 10
    if Greatest < last_digit :
            Greatest = last_digit
    N = N // 10
print(Greatest)

# Q29. Smallest Digit Without min()

N = int(input("Enter number : "))
N = abs(N)
import math
Smallest=10000000000
for i in range (int(math.log10(N))+1):
    last_digit = N % 10
    if Smallest> last_digit :
            Smallest = last_digit
    N = N // 10
print(Smallest)

# Q30. Reverse a Number

N = int(input("Enter number : "))
N = abs(N)
import math
reverse=0 
for i in range (int(math.log10(N))+1):
    reverse = reverse * 10 + N % 10
    N //=10
print(reverse)

# 31. Palindrome Number

N = int(input("Enter number : "))
N = abs(N)
original = N
reversed_number = 0
import math
for i in range (int(math.log10(N))+1):
    last_digit = N % 10
    reversed_number = reversed_number * 10 + last_digit
    N = N // 10
if reversed_number == original:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

# Q32. Count a Specific Digit

num=int(input("Enter Number : "))
digit=int(input("Enter Digit : "))
digit_repeat=0
import math
for i in range(int(math.log10(num))+1):
    last_digit=num%10
    if last_digit==digit:
        digit_repeat=digit_repeat+1
    num=num//10
print(digit_repeat)

# Q33. First Digit Using Repeated Division

num=int(input("Enter Number : "))
import math
for i in range(int(math.log10(num))):
   last_digit=num%10
   num=num-last_digit   
   num=num//10
print(num) 

# Q34. Difference Between Largest and Smallest Digit
n = int(input("Enter Number : "))
n=abs(n)
largest = 0
smallest = 9
import math
for i in range(int(math.log10(n))+1):
    d = n % 10
    if d > largest:
        largest = d
    if d < smallest:
        smallest = d
    n //= 10
print(int(largest - smallest))

#Q35. Digit Position Value

n = int(input("Enter Number : "))
n = abs(n)
digit=0
import math
for i in range(int(math.log10(n))+1):
    d = n % 10
    digit = digit*10+d
    n=n//10
    print(digit)

# Q36. Armstrong Number — 3 Digit

n = input("Enter 3-digit number : ") 
sum_of_Armstrong=0
for i in n:
    sum_of_Armstrong = sum_of_Armstrong + int(i) ** 3

if sum_of_Armstrong == int(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# Q37. Print Characters with Index

word=input("Enter Word :- ")
for i in range (len(word)):
    print(i,word[i])

# Q38. Count Characters Without len()

text=input("Enter String :- ")
count=0
for i in text:
    count=count+1
print(count)

# Q39. Count Vowels and Consonants

text=input("Enter String :- ")
count=0
vowels=0
consonants=0
for i in range(len(text)):
    if text[i] in "AIEOUaieou":
        vowels=vowels+1
    elif text[i]!= " ":
        consonants=consonants+1
print("Vowels : ",vowels)
print("Consonants : ",consonants)

# Q40. Character Frequency

text=input("Enter String : ")
target_character=input("Enter character : ")
frequency=0
for i in range(len(text)):
    if text[i]==target_character:
        frequency=frequency+1
print(frequency)

# Q41. First Occurrence Position

text = input("Enter String : ")
target = input("Enter Character : ")

found = -1

for i in range(len(text)):
    if text[i] == target and found == -1:
        found = i

if found == -1:
    print("Not Found")
else:
    print("Position : ", found)


# Q42. Count Uppercase and Lowercase

text=input("Enter String : ")
uppercase=0
lowercase=0
for i in text:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":  
        uppercase=uppercase+1
    elif i in "abcdefghijklmnopqrstuvwxyz":
        lowercase=lowercase+1
print("Uppercase : ",uppercase)
print("Lowercase : ",lowercase)

# Q43. Character Code Analyzer

text=input("Enter String : ")
for i in text:
    print(i,ord(i))

# Q44. String Without Vowels

text=input("Enter String : ")
for i in text :
    if i not in "AEIOUaeiou":
        print(i ,end="")


## Level 6 — Midpoint, Half & String Logic


#  Q45. Find the Middle Character

text=input("Enter String : ")
mid=len(text)//2
for i in range (1,len(text)+1):
    if i % 2 != 0:
        if i == mid:
            print(text[i])

# Q46. First Half and Second Half

s = input("Enter an even-length string: ")
mid = len(s) // 2
first_half = ""
second_half = ""
for i in range(len(s)):
    if i < mid:
        first_half += s[i]
    else:
        second_half += s[i]
print("First Half:", first_half)
print("Second Half:", second_half)

# Q47. Split a String by Length — Odd vs Even

text = input("Enter a string: ")
mid = len(text) // 2
first_half = ""
second_half = ""
middle_character = ""
length = len(text)
for i in range(length):
    if length % 2 != 0:
        if i < mid:
            first_half += text[i]
        elif i == mid:
            middle_character += text[i]
        else:
            second_half += text[i]
    else:
        if i < mid:
            first_half += text[i]
        else:
            second_half += text[i]

if length % 2 != 0:
    print("First Half:", first_half)
    print("Middle:", middle_character)
    print("Second Half:", second_half)
else:
    print("First Half:", first_half)
    print("Second Half:", second_half)

# Q48. Compare Two Halves

text = input("Enter an even-length string: ")
mid = len(text) // 2
first_half = ""
second_half = ""
for i in range(len(text)):
    if i<mid:
        first_half+=text[i]
    else:
        second_half+=text[i]
    
if first_half == second_half:
    print("Equal Halves")
else:
    print("Different Halves")

# Q49. Mirror the String

string=input("Enter String : ")
length =len(string)-1;
flage=True;
for i in range(0,len(string)):
    if(string[i]!=string[length]):
        print("not")
        flage=False
        break
    length = length-1
if flage==True:
   print("yes")

# Q50. Alternate Character Extraction

text = input("Enter a string: ")
for i in range(0,len(text),2):
    print(text[i],end=" ")

# Q51. Count Characters at Even and Odd Indexes

text = input("Enter a string: ")
even_index=0
odd_index=0
for i in range(len(text)):
    if i % 2 == 0:
        even_index=even_index+1
    else:
        odd_index=odd_index+1
print("Even Index : ",even_index)
print("Odd Index : ",odd_index)

# Q52. Swap Adjacent Characters

s = input("Enter an even-length string: ")
swapped_string = ""
for i in range(0, len(s), 2):
    swapped_string += s[i + 1] + s[i]
print(swapped_string)


## Level 7 — Tricky Single-Loop Problems

# Q53. Second Largest Digit

n = int(input("Enter a number: "))
largest = -1
second_largest = -1
import math
for i in range(int(math.log10(n))+1):
    if n == 0:
        break
    digit = n % 10   
    if digit > largest:
        second_largest = largest  
        largest = digit            
    elif digit > second_largest and digit != largest:
        second_largest = digit 
    n = n // 10
print("Second largest distinct digit:", second_largest)
    
# Q54. Longest Consecutive Equal Character Run

s=input("Enter Input : ")
current=1
best=1
for i in range (1,len(s)):
    if s[i]==s[i-1]:
        current+=1
    else:
        current = 1
    if current > best:
        best=current

print(best)

# Q55. Most Frequent Character — Controlled Approach

string=input("Enter Input : ")
target_character=input("target character : ")
count=0
frequency=0
for i in string:
    if i == target_character:
        count+=1
frequency=(count/len(string))*100
print(f"Count = {count}")
print(f"Frequency = {frequency:.2f}%")

# Q56. Running Digit Sum Until the End

N = int(input("Enter a positive integer : "))
N = abs(N)
Total=0
import math
for i in range(int(math.log10(N))+1):
    d=N%10
    Total=Total+d
    N=N//10
    print(Total)

# Q57. Number with Most Even Digits

N = int(input("Enter a positive integer : "))
N = abs(N)
even_count=0
odd_count=0
import math
for i in range(int(math.log10(N))+1):
    d=N%10
    if d % 2 == 0:
        even_count+=1
    else:
        odd_count+=1
    N=N//10
if even_count > odd_count:
    print("More Even Digits")
elif even_count < odd_count:
    print("More Odd Digits")
else:
    print("Equal")


# Q58. Alternating Digit Sum

N = int(input("Enter a positive integer : "))
N = abs(N)
result=0
import math
for i in range(int(math.log10(N))+1):
    d=N%10
    if i % 2 == 0 :
        result+=d
    else:
        result-=d
    N//=10
print(result)

# Q59. Output Prediction — Accumulator Trap

total = 0
for i in range(1, 6):
    total = total + i * 2
    print(total)
# 2
# 6
# 12
# 20
# 30


# Q60. Output Prediction — Condition Inside Loop

count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count = count + 1
print(count) # 5

# Q61. Debug the Accumulator

sum = 0
for i in range(1, 6):
    sum += i
print(sum)


## Level 8 — Real-Life Single-Loop Problems


# Q62. Daily Expense Analyzer

N = int(input("Enter number of days : "))
expense = input("Enter expense for each day : ").split(" ")
total_expense=0
highest_expense=-1
lowest_expense=10000000
for i in range (N):
    Expense=int(expense[i])
    total_expense+=Expense
    if Expense>highest_expense:
        highest_expense=Expense
    if Expense<lowest_expense:
        lowest_expense=Expense
print(f"Total: {total_expense}")
print(f"Highest: {highest_expense}") 
print(f"Lowest: {lowest_expense}")  

# Q63. Student Marks Analyzer

N = int(input("Enter number of subjects : "))
marks = input("Enter enter marks : ").split(" ")
total_marks =  0
avg_marks = 0
highest_marks = -1
lowest_marks = 10000
for i in range (N):
    Marks=int(marks[i])
    total_marks=total_marks+Marks
    avg_marks=total_marks/N
    if Marks>highest_marks:
        highest_marks=Marks
    if Marks<lowest_marks:
        lowest_marks=Marks
print(f"Total: {total_marks}")
print(f"Average: {avg_marks}")
print(f"Highest: {highest_marks}")
print(f"Lowest: {lowest_marks}")

# Q64. Attendance Analyzer

n = int(input("Enter number of working days : "))
attendance = input("Status: ").split(" ")
Present = 0
Absent = 0
attendance_percentage=0
for i in range (n):
    Attendance=attendance[i]
    if Attendance == "P":
        Present=Present+1
    elif Attendance == "A":
        Absent=Absent+1
if n > 0:
    attendance_percentage=(Present/n)*100
else:
    attendance_percentage=00.00
print (f"Present : {Present}")
print (f"Absent : {Absent}")
print (f"Attendance : {attendance_percentage:.2f}%")

# Q65. Electricity Usage Analyzer
n = int(input("Enter number of days : "))
total_units=0
days_above_10=0
electricity_units=input("Units: ").split()
for i in range(n):
    units=int(electricity_units[i])
    total_units=total_units+units
    if units>10:
        days_above_10=days_above_10+1
print(f"Total Units: {total_units}")
print(f"Days Above 10: {days_above_10}")


# Q66. Shopping Bill Analyzer

n = int(input("Enter the number of products: "))
total_bill = 0
products_above_1000 = 0
prices = input("Enter all prices separated by spaces: ").split()
for i in range(n):
    price = int(prices[i])
    total_bill += price
    if price > 1000:
        products_above_1000 += 1
print(f"Total Bill: {total_bill}")
print(f"Products Above 1000: {products_above_1000}")

#Q67. Login Attempt Analyzer

n = int(input("Enter number of attempts: "))

successful_count = 0
failed_count = 0

for i in range(n):
    attempt = input("Enter attempt status (success/failed): ")
    
    if attempt == "success":
        successful_count += 1
    elif attempt == "failed":
        failed_count += 1
if n > 0:
    success_rate = (successful_count / n) * 100
else:
    success_rate = 0.0

print("Successful:", successful_count)
print("Failed:", failed_count)
print("Success Rate:", f"{success_rate:.1f}%")

##Level 9 — Final Challenges


# Q68. Number Profile

N=int(input("Enter Number : "))
N=abs(N)
number_of_digits=0
sum_of_digits=0
largest_digit=-1
smallest_digit=9
even_digits=0
odd_digits=0
import math
for i in range (1,int(math.log10(N))+2):
    if i !=0:
        number_of_digits=number_of_digits+1
    last_digit= N % 10
    sum_of_digits=sum_of_digits+last_digit
    if last_digit > largest_digit:
        largest_digit = last_digit
    if last_digit < smallest_digit:
        smallest_digit=last_digit
    if last_digit%2==0:
        even_digits=even_digits+1
    if last_digit%2!=0:
        odd_digits=odd_digits+1
    N = N // 10 
print("Digits: ",number_of_digits)
print("Sum: ",sum_of_digits)
print("Largest: ",largest_digit)
print("Smallest: ",smallest_digit)
print("Even Digits: ",even_digits)
print("Odd Digits: ",odd_digits)

# Q69. String Balance Challenge

text = input("Enter a string: ")
even_index=0
odd_index=0
vowels=0
consonants=0
total_characters=0
lowercase=0
uppercase=0
for i in range(len(text)):
    total_characters=total_characters+1
    if i % 2 == 0:
        even_index=even_index+1
    else:
        odd_index=odd_index+1
    if text[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":  
        uppercase=uppercase+1
    elif text[i] in "abcdefghijklmnopqrstuvwxyz":
        lowercase=lowercase+1
    if text[i] in "AIEOUaieou":
        vowels=vowels+1
    elif text[i]!= " ":
        consonants=consonants+1
print("Total Characters : ",total_characters)
print("Vowels : ",vowels)
print("Consonants : ",consonants)
print("Uppercase : ",uppercase)
print("Lowercase : ",lowercase)
print("Even Index : ",even_index)
print("Odd Index : ",odd_index)

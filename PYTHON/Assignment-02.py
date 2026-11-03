#question 1
age = "25"
print(age, type(age))

#question 2
marks = "75.5"
print(float(marks), type(float(marks)))

#question 3
number = 50
print(float(number), type(float(number)))

#question 4
marks = 85.9
print(int(marks), type(int(marks)))

#question 5
roll_number = 101
print (str(roll_number), type(str(roll_number)))

#question 6
a="18"
b="92.5"
c=100
d=45.8
print(int(a) , type(int(a)))
print(float(b) , type(float(b)))
print(str(c) , type(str(c)))
print(int(d) , type(int(d)))

#question 7
a = "20"
b = int(a)
c = 10.8
d = int(c)
e = 25
f = str(e)
print(b)
print(d)
print(f)
print(type(b))
print(type(d))
print(type(f))
# OUTPUT
# 20
# 10
# 25
# <class 'int'>
# <class 'int'>
# <class 'str'>

#question 8
# age = "19"
# new_age = age + 1
# print("Age:", new_age)
age = "19"
new_age = int(age) + 1
print("Age:", new_age)

#question 9
marks = "85"
bonous=5
Final_marks=bonous+int(marks)
print("Final Marks:", Final_marks)

#question 10
price = "1499.50"
delivery_charges=99.50
Total_Amount=float(price)+delivery_charges
print("Total Amount:", Total_Amount) 

#question 11 — Basic Arithmetic
a = 20
b = 6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#question 12 — Predict the Output
a = 17
b = 5
print(a / b)
print(a // b)
print(a % b)
#output 
# 3.4
# 3
# 2

#question 13 — Operator Precedence
result = 10 + 5 * 2
print(result)
#output 20

#question 14 - More Precedence Practice
result = 20 - 4 * 3 + 2
print(result)
# Then rewrite the expression using parentheses to make the order of calculation clear.
result = 20 - (4 * 3) + 2
result = 20 - 12 + 2
result = 8 + 2
result = 10
print(result)

#Question 15 — Power Operator
#Predict the output:
print(2 ** 3)
print(3 ** 2)
print(10 ** 2)
#output 
#8
#9
#100
#and calculate the area of a square
side = 5
area = side**2
print("area of square=",area)

#Question 16 — Shopping Bill
#A student buys:
Notebook = 80
Pen = 20
Pencil = 10
Total_Amount= Pencil + Pen + Notebook
print ("Total Amount:", Total_Amount)

#Question 17 — Multiple Quantities
# A student buys:
# 3 notebooks at ₹50 each
# 2 pens at ₹15 each
# 1 calculator at ₹500
# Calculate the cost of each category and the total bill.
Notebook = 50
number_of_Notebook= 3
Notebook_cost = number_of_Notebook*Notebook
Pen = 15
number_of_Pen=2
Pen_cost =number_of_Pen*Pen
calculator = 500
number_of_calculator=1
calculator_cost =calculator*number_of_calculator
Total_Bill=Pen_cost +calculator_cost  + Notebook_cost
print ("Notebook cost :",Notebook_cost)
print ("Pen cost :",Pen_cost)
print ("calculator cost :",calculator_cost)
print("Total Bill :",Total_Bill)

#Question 18 — Complete Groups and Remainder
#A class has 47 students. They are divided into groups of 5.
# Find:
# Complete groups
# Students left over
number_of_students=47
number_of_students_in_each_group=5
number_of_Complete_groups= number_of_students//number_of_students_in_each_group 
number_of_Students_left_over=number_of_students%number_of_students_in_each_group 
print("number of Complete groups:" ,number_of_Complete_groups)
print("number of Students left over:" ,number_of_Students_left_over)

#Question 19 — Average Marks
Python = 85
Mathematics = 78
Physics = 92
Total_Marks = Python + Mathematics + Physics
Total_Subjects=3
Average_Marks= Total_Marks/Total_Subjects
print("Total Marks :",Total_Marks )
print("Average Marks :",Average_Marks )

#Question 20 — Percentage
English = 78
Mathematics = 85
Python = 92
Physics = 81
Chemistry = 74
Total_Marks = English + Mathematics + Python + Physics + Chemistry
Percentage = (Total_Marks/500)*100
print("Total Marks :",Total_Marks )
print("Overall Percentage:",str(Percentage)+ chr(37))

#Question 21 — Ones Digit
number = 583
print(number % 10)

#Question 22 — Tens Digit
number = 583
print((number//10) % 10)

#Question 23 — Hundreds  Digit
number = 583
print((number//100) % 10)

#Question 24 — Three-Digit Number Analyzer
number = 746
hundreds_digit = number // 100
tens_digit = (number // 10) % 10
ones_digit = number % 10
print("Hundreds digit =", hundreds_digit)
print("Tens digit =", tens_digit)
print("Ones digit =", ones_digit)

# Question 25 — Four-Digit Number
number=5829
thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
ones_digit = number % 10
print("Thousands digit =", thousands_digit)
print("Hundreds digit =", hundreds_digit)
print("Tens digit =", tens_digit)
print("Ones digit =", ones_digit)

# Question 26 — Sum of Digits
number = 583
hundreds_digit = number // 100
tens_digit = (number // 10) % 10
ones_digit = number % 10
Sum_of_Digits = hundreds_digit+tens_digit+ones_digit
print("Sum of Digits:" ,Sum_of_Digits)

#Question 27 — Four-Digit Sum
number = 4726
thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
ones_digit = number % 10
Sum_of_Digits = thousands_digit+ hundreds_digit+tens_digit+ones_digit
print("Sum of Digits:" ,Sum_of_Digits)

#Question 28 — Product of Digits
number = 234
hundreds_digit = number // 100
tens_digit = (number // 10) % 10
ones_digit = number % 10
Product_of_Digits=hundreds_digit*tens_digit*ones_digit
print("Product of Digits:", Product_of_Digits)

#Question 29 — Reverse a Three-Digit Number
number = 583
hundreds_digit = number // 100
tens_digit = (number // 10) % 10
ones_digit = number % 10
reversed_number = ones_digit * 100 + tens_digit * 10 + hundreds_digit
print("Original Number:", number)
print("Reversed Number:", reversed_number)

#Question 30 — Reverse a Four-Digit Number
number = 4726
thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
ones_digit = number % 10
# Create the reversed number
reversed_number = ones_digit * 1000 + tens_digit * 100 + hundreds_digit *10 +thousands_digit
print("Original Number:", number)
print("Reversed Number:", reversed_number)

#Question 31 — Place Value
number = 5834
thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
ones_digit = number % 10
print("Thousands digit =", thousands_digit)
print("Hundreds digit =", hundreds_digit)
print("Tens digit =", tens_digit)
print("Ones digit =", ones_digit)

#Question 32 — Difference Between First and Last Digit
number = 583
hundreds_digit = number // 100
tens_digit = (number // 10) % 10
ones_digit = number % 10
Difference=hundreds_digit-ones_digit
print("Difference:",Difference)

#Question 33 — Digit Extraction Debugging
number = 583
ones = number % 10
print("Ones Digit:", ones)

#Question 34 — Four-Digit Extraction
number = 9365
thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
ones_digit = number % 10
print("Thousands digit =", thousands_digit)
print("Hundreds digit =", hundreds_digit)
print("Tens digit =", tens_digit)
print("Ones digit =", ones_digit)

#Question 35 — Build a Number
hundreds = 5
tens = 8
ones = 3
number=hundreds*100+tens*10+ones
print("number:",number)

#Question 36 — Simple Interest
Principal = 50000
Rate = 6
Time = 2
print("Simple Interest =", int((Principal * Rate * Time) / 100))

#Question 37 — Rectangle
Length = 15 
Width = 8 
Area = Length * Width
Perimeter = 2 * (Length + Width)
print("Area:",Area)
print("Perimeter:",Perimeter)

#Question 38 — Circle
r = 7
pi = 3.14
Area = pi *(r**2)
print("Area:",Area)

#Question 39 — Temperature Conversion
Celsius = 35
Fahrenheit=(Celsius * 9/5) + 32
print("Fahrenheit (°F)= ",Fahrenheit )

#Question 40 — Time Conversion
seconds= 185
complete_Minutes=seconds//60
remaining_seconds=seconds%60
print("Complete Minutes=",complete_Minutes)
print("Remaining seconds=",remaining_seconds)

#Question 41 — Hours, Minutes and Seconds
total_seconds = 7384
total_minutes=total_seconds//60
total_hours=total_minutes//60
remaining_seconds=total_seconds%60
remaining_minutes=total_minutes%60
print("Hours:",total_hours)
print("Minutes:",remaining_minutes)
print("Seconds:",remaining_seconds)

#Question 42 — Salary Calculation
Basic_Salary = 25000
HRA = 5000
Travel_Allowance = 2500
Tax_Deduction = 3000
Gross_Salary = Basic_Salary + HRA + Travel_Allowance
Net_Salary = Gross_Salary-Tax_Deduction
print("Gross Salary:",Gross_Salary)
print("Net Salary:",Net_Salary)

#Question 43 — Travel Cost
distance = 120
mileage = 20
fuel_price = 100
fuel_required = distance / mileage
total_cost = fuel_required * fuel_price
print("Fuel Required =", fuel_required, "litres")
print("Total Fuel Cost = ₹", total_cost)

#Question 44 — Shopping Discount
price = 2500
discount =10
Discount_amount=((10/100)*2500)
Final_price=price-Discount_amount
print("Discount amount:",Discount_amount)
print("Final price:",Final_price)

#Question 45 — String Numbers
price = "1200"
quantity = "4"
Total_Price=int(price)*int(quantity)
print("price:",price)
print("quantity:",quantity)
print("Total Price:",Total_Price)

#Question 46 — Student Result
python_marks = "85"
math_marks = "78"
physics_marks = "91"
Total_Subjects=3
Total_Marks = int(python_marks)+int(math_marks)+int(physics_marks)
Average_Marks= Total_Marks/Total_Subjects
print("Total Marks :",Total_Marks )
print("Average Marks :",Average_Marks )

#Question 47 — Bill with Tax
price = "1500"
quantity = "2"
tax_rate = "5"
price = int(price)
quantity = int(quantity)
tax_rate = int(tax_rate)
subtotal = price * quantity
tax_amount = subtotal * tax_rate / 100
final_bill = subtotal + tax_amount
print("Subtotal:", subtotal)
print("Tax Amount:", tax_amount)
print("Final Bill:", final_bill)

#Question 48 — Discount + GST
product_costs=2000
Discount = 15
GST = 18
Discount_amount=((15/100)*2500)
GST_amount=((18/100)*2500)
Price_after_discount=product_costs-Discount_amount
Final_price= price-Discount_amount    
print("Discount amount:",Discount_amount) 
print("Price after discount",Price_after_discount) 
print("GST_amount:",GST_amount)                                                                                                                                                                                                                                                                                                  
print("Final price:",Final_price)

#Question 49 — Debug the Billing Program
price = "500"
quantity = 3
total = int(price) * quantity
print("Total:", total)

#Question 50 — Debug the Marks Program
marks1 = "80"
marks2 = "75"
marks3 = "90"
total = str(marks1) + str(marks2) + str(marks3)
print("Total Marks:", total)

#Question 51 — Type Casting Output
#Predict the output:
a = "50"
b = int(a)
print(a)
print(b)
print(type(a))
print(type(b))
#output
# 50
# 50
# <class 'str'>
# <class 'int'>

#Question 52 — Float to Integer
#Predict the output:
number = 99.99
result = int(number)
print(number)
print(result)
#output
# <class 'str'>
# <class 'int'>
# 99.99
# 99

#Question 53 — Arithmetic Output
#Predict the output:
a = 12
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
#output
# 17
# 7
# 60
# 2.4
# 2
# 2

#Question 54 — Parentheses Challenge
#Predict the outputs:
print(10 + 5 * 2)
print((10 + 5) * 2)
print(20 / 5 + 3)
print(20 / (5 + 3))
#output:
20
30
7.0
2.5

#Question 55 — Digit Challenge
#Predict_the_output:
number = 684
a = number % 10
b = number // 10
c = b % 10
d = number // 100
print(a)
print(c)
print(d)
# solution: d represents  hundreds, c represents tens , d represents ones.

#Question 56 — Debug the Student Program
student_name = "Ravi"
marks = 85
total = marks + 5
print("Student:", student_name)
print("Marks:", total)
print("Type:", type(total))

#Question 57 — Debug the Number Program
number = 746
ones = number / 10
tens = number // 10
hundreds = number // 100
print("Ones:", ones)
print("Tens:", tens)
print("Hundreds:", hundreds)

#Question 58 — Debug the Discount Program
price = 2000
discount = 15
discount_amount = price * discount / 100
final_price = price - discount_amount
print("Discount:", discount_amount)
print("Final Price:", final_price)

#Question 59 — Complete Debugging Challenge
student_name ="Rahul"
marks1 = 85
marks2 = 90
marks3 = 78
total = marks1 + marks2 + marks3
average = (total / 3)
print("Student:", student_name)
print("Total Marks:", total)
print("Average:", average)
print("Marks Type:", type(total))

#Question 60 — Final Challenge: Number + Billing
#Part A — Number Analysis
number=5836
thousand_digit=number//1000
hundred_digit=(number%1000)//100 #pattern follow hota h ki %us jo bhi digit h usee % aur ek zero kam se //100 
tens_digit=(number%100)//10 #tens_digit=(number//10)%10
units_digit=(number%100)%10
print("Thousand digit number=",thousand_digit)
print("Hunderd digit number=",hundred_digit)
print("Tens digit number=",tens_digit)
print("Ones digit number=",units_digit) 
#Part B — Product Billing
price = 1250
quantity = 4
discount = 10
sub_total=(price+quantity)
discount_amount=125
Final_amount=(sub_total - discount_amount)
print(sub_total)
print(discount_amount)
print(Final_amount)

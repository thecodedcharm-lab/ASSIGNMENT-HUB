#Topic-1 — Basic if Statements


# Q1. Positive Number

num=int(input("Enter Number : "))
if num > 0:
    print("Positive Number")

# Q2. Voting Eligibility Check

age = int(input("Enter Age : "))
if age >=18:
    print("Eligible to Vote")

# Q3. Temperature Warning

tem= int(input("Enter Temperature : "))
if tem > 40:
    print("High Temperature")

# Q4. Divisible by 5

num=int(input("Enter Number : "))
if num % 5 == 0:
    print("Divisible by 5")

# Q5. Free Delivery

order_amount=int(input("Enter Order Amount : "))
if order_amount >= 1000 :
    print("Free Delivery")

# Q6. Character Check

Character = input("Enter a Character : ")
if Character == "A":
    print("You entered A")

# Q7. Password Length Check

password = input("Enter Password : ")
if len(password)>=8:
    print("Strong Length")

# Q8. Number of Digits

num=int(input("Enter Number : "))
if 999 >= num >= 100:
    print("Three Digit Number")

# Topic-2 — if-else Statements


# Q9. Even or Odd

num=int(input("Enter Number : "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Q10. Pass or Fail

marks = int (input("Enter Marks : "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Q11. Adult or Minor

age = int(input("Enter Age : "))
if age >=18:
    print("Adult")
else :
    print("Minor")

# Q12. Number Sign

num=int(input("Enter Number : "))
if num >0:
    print("Positive")
else:
    print("Non-Positive")

# Q4. Divisible by 3

num=int(input("Enter Number : "))
if num % 3 == 0:
    print("Divisible by 3")
else:
    print("Not Divisible by 3")

#Q14. Login Password

correct_password = "python123"
password=input("Enter Password : ")
if correct_password==password:
    print("Login Successful")
else:
    print("Invalid Password")

#Q15. Username Check

correct_username = "admin"
username=input("Enter username : ")
if correct_username==username:
    print("Welcome Admin")
else:
    print("Invalid Username")

#Q16. Greater Between Two Numbers

num1, num2 = (int, input().split(","))
if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else:
    print("Both are Equal")

# Q17. Hot or Comfortable

temperature= int(input("Enter Temperature : "))
if temperature > 30:
    print("Hot")
else:
    print("Comfortable")

#Q18. Shopping Discount Eligibility

shopping_amount=int(input("Enter Shopping Amount : "))
if shopping_amount>=5000:
    print("Discount Available")
else:
    print("No Discount")

# Topic-3 — if-elif-else


#Q19. Grade Calculator

Marks=int(input("Enter Your Marks : "))
if Marks>=90:
    print("Grade A")
elif Marks>=80:
    print("Grade B")
elif Marks>=70:
    print("Grade C")
elif Marks>=60:
    print("Grade D")
else:
    print("Grade F")

#Q20. Temperature Category

temperature= int(input("Enter Temperature : "))
if temperature > 40:
    print("Very Hot")
elif 39>=temperature>=30:
    print("Hot")
elif 29>=temperature>=20:
    print("Warm")
else:
    print("Cold")


#Q21. Traffic Signal

color=input("Traffic Colour : ")
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("Go")
else:
    print("Invalid Signal")

#Q22. Electricity Usage Category

electricity_units=int(input("Enter Electricity Units : "))
if electricity_units>500:
    print("Very High Usage")
elif electricity_units>=300:
    print("High Usage")
elif electricity_units>=100:
    print("Medium Usage")
else:
    print("Low Usage")

#Q23. Movie Ticket Category

age = int (input("Enter age : "))
if age >=60:
    print("Senior Ticket")
elif age >=13:
    print("Regular Ticket")
elif age >=5:
    print("Child Ticket")
else:
    print("Free Ticket")

# Q24. BMI Category

BMI = float(input("Enter BMI : "))
if BMI>=30:
    print("Obese")
elif BMI>=24.9:
    print("Overweight")
elif BMI>=18.5:
    print("Normal")
else:
    print("Underweight")

# Q25. Month Days

month_number= int(input("Enter month number : " ))
if month_number == (1 or 3 or 5 or 7 or 8 or 10 or 12):
    print("31 Days")
elif month_number == (4 or 6 or 9 or 11):
    print("30 Days")
elif month_number == 2  :
    print(" 28 or 29 Days")
else:
    print("Invalid Month")

# Q26. Simple Calculator

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
	print("Result:", first_number + second_number)
elif operator == "-":
	print("Result:", first_number - second_number)
elif operator == "*":
	print("Result:", first_number * second_number)
elif operator == "/":
	if second_number == 0:
		print("Cannot divide by zero")
	else:
		print("Result:", first_number / second_number)
else:
	print("Invalid operator")

# Q27. Day Number

week=int(input("Enter Day Number : "))
if week == 1 :
    print("Monday!")
elif week == 2 :
    print("Tuesday!")
elif week == 3 :
    print("Wednesday!")
elif week == 4 :
    print("Thursday!")
elif week == 5 :
    print("Friday!")
elif week == 6 :
    print("Suesday!")
elif week == 7 :
    print("Sunday!")
else :
    print("INVALID DAY NUMBER!")

# Q28. Performance Level

score=int(input("Enter Your Score : "))
if score>=90:
    print("Excellent")
elif score>=75:
    print("Very Good")
elif score>=60:
    print("Good")
elif score>=40:
    print("Average")
else:
    print("Needs Improvement")

# Topic-4 — Logical Conditions


#Q29. College Admission Eligibility


marks=int(input("Enter Marks : "))
attendance=int(input("Enter attendance : "))
if marks>=60:
    if attendance>=75:
        print("Eligible")
    else :
        print ("Not Eligible")
else :
    print ("Not Eligible")

# Q30. Scholarship Eligibility

marks=int(input("Enter Marks : "))
family_income=int(input("Enter family income : "))
if marks>=85:
    if family_income<=300000:
        print("Scholarship Available")
    else:
        print("No Scholarship")
else:
    print("No Scholarship")


#Q31. Weekend Check

day =input("Enter a week day")
if (day == "Saturday" or day == "Sunday"):
    print("Weekend")
else:
    print("Weekday")

#Q32. Online Exam Access

username="student"
password="python123"
enter_username=input("Enter Username : ")
enter_password=input("Enter Password : ")
if username == enter_username :
    print("Access Granted")
else:
    print("Access Denied")

# Q33. Delivery Availability

City=input("Enter City Name : ")
if (City == "Ahmedabad" or City == "Gandhinagar"):
    print("Access Granted")
else:
    print("Access Denied")

#Q34. Number Range Check

integer=input("Enter Integer : ")
if 50 >= integer >= 10 :
    print("Inside Range")
else:
    print("Outside Range")

# Q35. Secure Transaction

amount = int(input("Enter Amount : "))
OTP  = "1234"
otp = (input("Enter OTP : "))
if amount <= 50000:
    if otp == OTP :
        print("Transaction Approved")
    else:
        print("Transaction Declined")
else:
    print("Transaction Declined")

#      Topic-5 — Nested if


# Q36. Login with Role

username="admin"
password="admin123"
enter_username=input("Enter Username : ")
if username == enter_username :
    enter_password=input("Enter Password : ")
    if password == enter_username :
        print("Access Granted")
    else :
        print("Access Denied")
else:
    print("Access Denied")

# Q37. Driving License Eligibility

age = int(input("Enter Age : "))
if age == 18 :
    test_status = input("Enter Test Status : ")
    if test_status=="Pass":
        print ("License Approved")
    else:
        print ("Test Not Passed")
else:
    print ("Age Not Eligible")


# Q38. ATM Withdrawal

account_balance=int(input("Account Balance : "))
withdrawal_balance=int(input("Withdrawal Balance : "))
if account_balance>=withdrawal_balance:
    if withdrawal_balance % 100 == 0 :
        print("Withdrawal Successful")
    else:
        print("Enter Amount in Multiples of 100")
else:
    print("Insufficient Balance")

#Q39. Exam Result with Attendance

marks = int(input("Enter Marks : "))
attendance = int(input("Enter Attendance : "))
if attendance >=75:
    if marks >=40:
        print("pass")
    else:
        print("Fail")
else:
    print("Not Eligible Due to Attendance")

# Q40. Bank Account Verification

account_balance=input("Enter account type : ")
balance=int(input("Enter balance : "))
if account_balance =="savings":
    if balance>=100:
        print("Minimum Balance Maintained")
    else:
        print("Minimum Balance Not Maintained")
else:
    print("Unsupported Account")

# Q41. Online Shopping Eligibility

order_amount = int(input("Enter Order amount : "))
payment_method = (input("Enter Payment method : "))

if order_amount>=500:
    if payment_method == "card":
        print("Card Payment Accepted")
    elif payment_method == "upi":
        print("UPI Payment Accepted") 
    else:
        print("Unsupported Payment Method") 
else:
    print("Minimum Order Amount Not Reached") 

# Q42. Hostel Room Allocation

year_of_study = int(input("Enter year of study: "))
attendance = int(input("Enter attendance: "))
if (year_of_study == 2 or year_of_study == 3 or year_of_study == 4 ):
    if attendance >=75:
        print("Room Eligible")
    else:
        print("Attendance Too Low")
else:
    print("Not Eligible by Year")

# Q43. Internet Plan Upgrade

current_plan = (input("Enter current plan : "))
monthly_usage = int(input("Enter monthly usage : "))
if current_plan == "basic":
    if monthly_usage>100:
        print("Recommend Upgrade")
    else:
        print("Basic Plan Is Sufficient")
else:
    print("Already on Higher Plan")

    #   Topic-6 — Nested if-elif-else


# Q44. Greatest of Three Numbers

a = int(input("Enter integer A : "))
b = int(input("Enter integer B : "))
c = int(input("Enter integer C : "))
if a>b and a>c:
    print("A is Greatest")
elif b>c:
    print("B is Greatest")
elif c>b and c>a:
    print("C is Greatest")
elif a==b and a>c:
    print("A and B are Equal and Greatest")
elif a==c and a>b:
    print("A and C are Equal and Greatest")
elif b==c and b>c:
    print("B and C are Equal and Greatest")
else:
    print("All are Equal")

# Q45. Student Result with Grade

marks=int(input("Enter Marks : "))
attendance=int(input("Enter attendance : "))
if attendance>=75:
    if marks>=90:
        print("Grade A")
    elif marks>=75:
        print("Grade B")
    elif marks>=60:
        print("Grade C")
    elif marks>=40:
        print("Grade D")
    else:
        print("Grade F")
else:
    print("Not Eligible")

# Q46. Employee Bonus

salary = int(input("Enter salary : "))
performance_rating = int(input("Enter performance rating : "))
if salary >=30000:
    if performance_rating==5:
       print("Bonus: 20%") 
    elif performance_rating==4:
        print("Bonus: 15%")
    elif performance_rating==3:
        print("Bonus: 10%") 
    elif performance_rating==2:
        print("Bonus: 5%")  
    else:
        print("Not Eligible for Bonus") 
else:
    print("Not Eligible for Bonus")  

# Q47. Bus Ticket Category 

age = int(input("Enter age : "))
distance = int(input("Enter Distance : "))
if age >= 60:
    print("Senior")
elif age >=5:
    print("Regular", end=" - ")
    if distance>10:
        print("Long Distance")
    else:
        print("Short Distance")
else:
    print("Free")

# Q48. Product Purchase Validation

product_stock = int(input("Enter product stock : "))
payment_status = (input("Enter payment status : "))
if product_stock>0:
    if payment_status ==  "paid":
        print(" Order Confirmed")
    elif payment_status == "pending":
        print("Payment Pending")
    else: 
        print("Invalid Payment Status")
else:
    print("Out of Stock") 

# Q49. Travel Ticket Validation

age = int(input("Enter Age : "))
ticket_type= (input("Enter ticket type : "))
if age >= 60:
    print("Free Travel")
elif age>=5:
    print("Regular Passenger")
    if ticket_type== "AC":
        print("AC Ticket")
    elif ticket_type== "Sleeper":
        print("Sleeper Ticket")
    else:
        print(" Invalid Ticket Type")
else:
    print("Free Travel")

        #   Topic-7 — match-case


# Q50. Basic Menu

menu_number = int(input("Enter Number From 1 to 4 : "))
match menu_number:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Update")
    case 4:
        print("Delete")
    case _:
        print("Invalid Choice")

# Q51. Day Name Using match-case

# day_number =int (input("Enter Day No. : "))
# match day_number :
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thrusday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print ("Invaild User Input!")

# Q52. Calculator Using match-case

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
match operator:
    case "+":
        print("Result:", first_number + second_number)
    case "-":
        print("Result:", first_number - second_number)
    case "*":
        print("Result:", first_number * second_number)
    case "/":
        if second_number == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", first_number / second_number)
    case _:
        print("Invalid operator")

# Q53. Traffic Signal Using match-case

traffic_signal_color=input("Enter traffic signal color")
match traffic_signal_color:
    case "red":
        print("Stop")
    case "yellow":
        print("wait")
    case "green":
        print("go")

# Q54. Grade Message Using match-case

grade=(input("Enter Grade : "))
match grade:
    case "A":
        print("Excellent Performance")
    case "B":
        print("Very Good Performance")
    case "C":
        print("Good Performance")
    case "D":
        print("Needs Improvement")
    case "F":
        print("Failed")
    case _:
        print("Invalid Grade")

# Q55. Mobile Service Menu

service_code = int(input("Enter service code : "))
match service_code:
    case 1:
        print("Check Balance")
    case 2:
        print("Recharge")
    case 3:
        print("Data Usage")
    case 4:
        print("Customer Support")
    case _:
        print("Invalid Service")

# Q56. Month Name Using match-case
month = int(input("Enter month number: "))
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid Month")

# Q57. File Type Detector

extention=input("Enter Extention : ")
match extention:
    case "pdf":
        print("Document")
    case "jpg":
            print("Image")
    case "png":
            print("Image")
    case "mp3":
            print("Audio")
    case "mp4":
            print("Video")

      #Topic-8 — Conditional Statements + Previous Concepts


# Q58. Student ID Validation
student_id = input("Enter Student ID: ")
degree, batch, branch, roll_number = student_id.split("-")
if branch == "CSE":
    print("CSE Student")
else:
    print("Non-CSE Student")

#Q59. Email Domain Checker
email = input("Enter email: ")
username, domain = email.split("@")
if domain == "gmail.com":
    print("Gmail User")
else:
    print("Other Email Provider")

# Q60. Username Generator Validation
full_name = input("Enter full name: ")
first_name, middle_name, last_name = full_name.split()
username = first_name + "." + last_name
if "." in username:
    print("Valid Username Format")
else:
    print("Invalid Username Format")

# Q61. Number Digit Analyzer

number=int(input("Enter Number"))
if number>=1000:
    print("Four or More Digits")
elif number>=100:
    print("Three Digits")
elif number>=10:
    print("Two Digits")
else:
    print("One Digits")

# Q62. Shopping Bill Category

price = int(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
subtotal = price * quantity
if subtotal >= 5000:
    discount = 20
elif subtotal >= 2000:
    discount = 10
else:
    discount = 0
discount_amount = subtotal * discount / 100
final_amount = subtotal - discount_amount
print("Subtotal:", subtotal)
print("Discount:", str(discount) + "%")
print("Final:", f"{final_amount:.2f}")

# Q63. Electricity Bill Category

units = int(input("Enter Units : "))
if units >= 300:
    rate=10
elif units>=100:
    rate=7
else:
    rate=5
bill = units * rate
print("Units:", units)
print("Rate: ₹" + str(rate))
print("Bill: ₹" + str(bill))

#Q64. ATM Menu

option = int (input ("Enter choice : "))
match option:
    case 1 :
        print ("Check Balance")
        balance=int(input("Balance : "))
        print ("Balance : ",balance)
    case 2 :
        print ("Withdraw Money")
        Withdraw_Money=int(input("Withdraw Amount : "))
        print ("Withdraw Amount : ", Withdraw_Money)
    case 3 :
        print ("Deposit Money")
        Deposit_Money=int(input("Deposit Amount : "))
        print ("Deposit Amount : ", Deposit_Money)
    case 4 :
        print("Change PIN")
        old_pin = input("Enter old PIN : ")
        if old_pin == "0000":
            new_pin = input("Enter new PIN : ")
            print("PIN changed successfully")
        else:
            print("Incorrect PIN")
    case 5 :
        print ("Exit")
    case _:
        print("Invalid option Choice")

# Q65. Restaurant Ordering System

choice = int(input("Enter choice: "))
match choice:
    case 1:
        item = "Pizza"
        price = 250
    case 2:
        item = "Burger"
        price = 150
    case 3:
        item = "Pasta"
        price = 200
    case 4:
        item = "Sandwich"
        price = 120
    case _:
        print("Invalid Choice")
        exit()
quantity = int(input("Enter quantity: "))
total = price * quantity
if total >= 500:
    discount = total * 10 / 100
else:
    discount = 0
final_amount = total - discount
print("Item:", item)
print("Quantity:", quantity)
print("Total:", total)
print("Discount:", f"{discount:.2f}")
print("Final:", f"{final_amount:.2f}")

# Q66. Exam Result Analyzer

marks1=int(input("Enter Marks 1 : "))
marks2=int(input("Enter Marks 2 : "))
marks3=int(input("Enter Marks 3 : "))
attendance=int(input("Enter attendance : ")) 
total=marks1+marks2+marks3
avg=total/3
if attendance>=75:
    if avg>=90:
        print("Outstanding")
    elif avg>=75:
        print("Very Good")
    elif avg>=60:
        print("Good")
    elif avg>=40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")

# Q67. Cab Fare Calculator

distance = int(input("Enter distance in km: "))
ride_type = input("Enter ride type: ")
match ride_type:
    case "normal":
        rate = 15
    case "premium":
        rate = 25
    case _:
        print("Invalid Ride Type")
        exit()
fare = distance * rate
if distance > 20:
    surcharge = fare * 10 / 100
else:
    surcharge = 0
final_fare = fare + surcharge
print("Fare:", f"{final_fare:.2f}")

# Q68. College Admission System

entrance_score = int(input("Enter entrance score : "))
percentage = int(input("Enter 12th percentage : "))
category  = (input("Enter category : "))
match category:
    case "General":
        if entrance_score>=80 and percentage>=75:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")
    case "OBC":
        if entrance_score>70 and percentage>=70:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")
    case "SC":
        if entrance_score>60 and percentage>=60:
            print("Admission Eligible")
        else:
            print("Admission Not Eligible")

          #Topic-9 — Debugging Conditional Programs


# Q69. Debug the Condition

age = int(input("Enter age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Q70. Debug the Nested Condition

marks = int(input("Enter marks: "))
if marks >= 40:
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    else:
        print("Pass")
else:
    print("Fail")

          #Topic-10 — Output Prediction & Execution Flow


#Q71. Condition Order

marks = 85
if marks >= 40:
    print("Pass")
elif marks >= 75:
    print("Very Good")
else:
    print("Fail")
# output == "pass"

# Q72. Correct the Condition Order

marks = 85
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
# output == "B"

# Q73. Nested if Execution Flow

age = 20
has_id = True
if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Underage")
# output == "Entry Allowed"

# Q74. match-case and Default Case

choice = 5
match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Delete")
    case _:
        print("Invalid Choice")
# output == "Entry Allowed"

# Q75. Final Execution Challenge

marks = 82
attendance = 80
if attendance >= 75:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")
# # output == "Grade B"

# ======================================================
# Section A — Basic Function Practice
# ======================================================

# --------------------------------------------------------
# Q1. Display a Welcome Message

def display_welcome():
    print("=====================================")
    print("    Welcome to Python Programming    ")
    print("        Let's learn Functions!       ")
    print("=====================================")

display_welcome()
display_welcome()
display_welcome()

# --------------------------------------------------------

# --------------------------------------------------------
# Q2. Student Introduction Card

def display_student_card(name, age, course):
    print("+--------------------------------+")
    print("|         STUDENT CARD           |")
    print("+--------------------------------+")
    print(f"| Name  : {name:<22} |")
    print(f"| Age   : {age:<22} |")
    print(f"| Course: {course:<22} |")
    print("+--------------------------------+")


display_student_card("Rahul", 18, "B.Tech")
display_student_card("Priya", 19, "BCA")
display_student_card("Aman", 20, "B.Sc")

# --------------------------------------------------------

# --------------------------------------------------------
# Q3. Square, Cube, and Double

def calculate_square(number):
    print("Square:", number * number)


def calculate_cube(number):
    print("Cube:", number * number * number)


def calculate_double(number):
    print("Double:", number * 2)


calculate_square(2)
calculate_cube(2)
calculate_double(2)

calculate_square(4)
calculate_cube(4)
calculate_double(4)

calculate_square(5)
calculate_cube(5)
calculate_double(5)

# --------------------------------------------------------

# --------------------------------------------------------
# Q4. Simple Interest Calculator

def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest

    print(f"Principal      : {principal}")
    print(f"Rate           : {rate}%")
    print(f"Time           : {time} years")
    print(f"Simple Interest: {simple_interest}")
    print(f"Total Amount   : {total_amount}")


calculate_simple_interest(5000, 5, 2)
calculate_simple_interest(10000, 7, 3)
calculate_simple_interest(2500, 4, 1)

# --------------------------------------------------------

# --------------------------------------------------------
# Q5. Even or Odd Checker

def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is an Even number.")
    else:
        print(number, "is an Odd number.")


check_even_odd(12)
check_even_odd(7)
check_even_odd(0)
check_even_odd(-5)

# --------------------------------------------------------


# ========================================================
# Section B — Parameters, Arguments, and Return Values
# ========================================================

# --------------------------------------------------------
# Q6. Find the Larger Number

def find_largest(number_1, number_2):
    if number_1 >= number_2:
        return number_1
    else:
        return number_2


result_1 = find_largest(25, 40)
print("Largest number:", result_1)

result_2 = find_largest(90, 15)
print("Largest number:", result_2)

result_3 = find_largest(12, 12)
print("Largest number:", result_3)

result_4 = find_largest(-5, -2)
print("Largest number:", result_4)

# --------------------------------------------------------

# --------------------------------------------------------
# Q7. Temperature Converter

def celsius_to_fahrenheit(celsius):
    return ((9 / 5) * celsius) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


fahrenheit_1 = celsius_to_fahrenheit(0)
print(fahrenheit_1)

fahrenheit_2 = celsius_to_fahrenheit(25)
print(fahrenheit_2)

fahrenheit_3 = celsius_to_fahrenheit(100)
print(fahrenheit_3)

celsius_1 = fahrenheit_to_celsius(32)
print(celsius_1)

celsius_2 = fahrenheit_to_celsius(68)
print(celsius_2)

celsius_3 = fahrenheit_to_celsius(98.6)
print(celsius_3)

# --------------------------------------------------------

# --------------------------------------------------------
# Q8. Understand the Difference Between print() and return

def calculate_sum_1(a, b):
    print(a + b)


def calculate_sum_2(a, b):
    return a + b


# First test case
result_1 = calculate_sum_1(10, 20)
result_2 = calculate_sum_2(10, 20)

print("Result from first function:", result_1)
print("Result from second function:", result_2)


# Second test case
result_3 = calculate_sum_1(5, 7)
result_4 = calculate_sum_2(5, 7)

print("Result from first function:", result_3)
print("Result from second function:", result_4)


# Third test case
result_5 = calculate_sum_1(100, 250)
result_6 = calculate_sum_2(100, 250)

print("Result from first function:", result_5)
print("Result from second function:", result_6)


# Answers:
# First function does not return a value.
# The first variable contains None because print() only displays the result.
# The value displayed by print() cannot be directly stored as a return value.

# --------------------------------------------------------

# --------------------------------------------------------
# Q9. Total Marks and Percentage

def calculate_result(mark_1, mark_2, mark_3, mark_4, mark_5):
    total_marks = mark_1 + mark_2 + mark_3 + mark_4 + mark_5
    percentage = (total_marks / 500) * 100

    return total_marks, percentage


total_1, percentage_1 = calculate_result(75, 80, 65, 90, 70)
print("Total Marks:", total_1)
print("Percentage:", percentage_1, "%")

total_2, percentage_2 = calculate_result(50, 60, 55, 65, 70)
print("Total Marks:", total_2)
print("Percentage:", percentage_2, "%")

total_3, percentage_3 = calculate_result(100, 95, 90, 85, 80)
print("Total Marks:", total_3)
print("Percentage:", percentage_3, "%")

# --------------------------------------------------------

# --------------------------------------------------------
# Q10. Rectangle Area and Perimeter

def rectangle_details(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)

    return area, perimeter


area_1, perimeter_1 = rectangle_details(10, 5)
print("Area:", area_1)
print("Perimeter:", perimeter_1)

area_2, perimeter_2 = rectangle_details(8, 4)
print("Area:", area_2)
print("Perimeter:", perimeter_2)

area_3, perimeter_3 = rectangle_details(7, 7)
print("Area:", area_3)
print("Perimeter:", perimeter_3)

# --------------------------------------------------------


# ========================================================
# Section C — Default and Keyword Arguments
# ========================================================

# --------------------------------------------------------
# Q11. Personalized Greeting

def greet_user(name, message="Welcome to Python!"):
    print("Hello", name + "!")
    print(message)


greet_user("Rahul", "Good Morning!")

greet_user("Priya")

greet_user("Aman", message="Keep Learning!")

greet_user("Neha")

# --------------------------------------------------------

# --------------------------------------------------------
# Q12. Electricity Bill Calculator

def calculate_electricity_bill(units, rate=7):
    bill = units * rate
    return bill


bill_1 = calculate_electricity_bill(100)
print("Bill 1:", bill_1)

bill_2 = calculate_electricity_bill(100, 8)
print("Bill 2:", bill_2)

bill_3 = calculate_electricity_bill(rate=6, units=100)
print("Bill 3:", bill_3)

# --------------------------------------------------------

# --------------------------------------------------------
# Q13. Employee Salary Calculator

def calculate_salary(basic_salary, bonus=2000, deduction=500):
    final_salary = basic_salary + bonus - deduction
    return final_salary


salary_1 = calculate_salary(25000)
print("Final Salary:", salary_1)

salary_2 = calculate_salary(25000, 3000)
print("Final Salary:", salary_2)

salary_3 = calculate_salary(25000, 3000, 1000)
print("Final Salary:", salary_3)

salary_4 = calculate_salary(basic_salary=25000, deduction=800, bonus=4000)
print("Final Salary:", salary_4)


# Parameters with default values are placed after parameters
# without default values so that required arguments are
# received before optional arguments.

# --------------------------------------------------------


# ========================================================
# Section D — Applying Functions with Previously Learned Topics
# ========================================================

# --------------------------------------------------------
# Q14. Number Digit Counter

def count_digits(number):
    number = abs(number)

    if number == 0:
        return 1

    digit_count = 0

    while number > 0:
        number = number // 10
        digit_count = digit_count + 1

    return digit_count


count_1 = count_digits(7)
print("Total digits:", count_1)

count_2 = count_digits(4826)
print("Total digits:", count_2)

count_3 = count_digits(90000)
print("Total digits:", count_3)

count_4 = count_digits(0)
print("Total digits:", count_4)

# --------------------------------------------------------

# --------------------------------------------------------
# Q15. Sum of Digits

def sum_of_digits(number):
    number = abs(number)
    digit_sum = 0

    while number > 0:
        digit = number % 10
        digit_sum = digit_sum + digit
        number = number // 10

    return digit_sum


result_1 = sum_of_digits(123)
print("Sum of digits:", result_1)

result_2 = sum_of_digits(482)
print("Sum of digits:", result_2)

result_3 = sum_of_digits(9005)
print("Sum of digits:", result_3)

result_4 = sum_of_digits(7)
print("Sum of digits:", result_4)

# --------------------------------------------------------

# --------------------------------------------------------
# Q16. Reverse a Number

def reverse_number(number):
    number = abs(number)
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    return reversed_number


result_1 = reverse_number(123)
print("Reversed number:", result_1)

result_2 = reverse_number(4826)
print("Reversed number:", result_2)

result_3 = reverse_number(900)
print("Reversed number:", result_3)

result_4 = reverse_number(7)
print("Reversed number:", result_4)

# --------------------------------------------------------

# --------------------------------------------------------
# Q17. Palindrome Number Checker

def is_palindrome(number):
    original_number = number
    number = abs(number)
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    if original_number >= 0 and original_number == reversed_number:
        return True
    else:
        return False


result_1 = is_palindrome(121)
print(result_1)

result_2 = is_palindrome(1331)
print(result_2)

result_3 = is_palindrome(123)
print(result_3)

result_4 = is_palindrome(7)
print(result_4)

# --------------------------------------------------------

# --------------------------------------------------------
# Q18. Prime Number Checker

def is_prime(number):
    if number <= 1:
        return False

    divisor = 2

    while divisor < number:
        if number % divisor == 0:
            return False

        divisor = divisor + 1

    return True


result_1 = is_prime(2)
print(result_1)

result_2 = is_prime(17)
print(result_2)

result_3 = is_prime(21)
print(result_3)

result_4 = is_prime(1)
print(result_4)

result_5 = is_prime(0)
print(result_5)

# --------------------------------------------------------

# --------------------------------------------------------
# Q19. Display Prime Numbers in a Range

def display_primes(start, end):
    prime_count = 0

    print("Prime numbers:", end=" ")

    for number in range(start, end + 1):
        if number > 1:
            divisor = 2
            is_prime_number = True

            while divisor < number:
                if number % divisor == 0:
                    is_prime_number = False
                    break

                divisor = divisor + 1

            if is_prime_number:
                print(number, end=" ")
                prime_count = prime_count + 1

    if prime_count == 0:
        print("No prime numbers", end="")

    print()
    print("Total prime numbers:", prime_count)


display_primes(1, 10)
display_primes(10, 30)
display_primes(20, 25)
display_primes(14, 16)

# --------------------------------------------------------

# --------------------------------------------------------
# Q20. Student Result Report

def display_student_report(name, mark_1, mark_2, mark_3):
    total_marks = mark_1 + mark_2 + mark_3
    percentage = (total_marks / 300) * 100

    if percentage >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    print("================================")
    print("         STUDENT REPORT")
    print("================================")
    print(f"Name       : {name}")
    print(f"Subject 1  : {mark_1}")
    print(f"Subject 2  : {mark_2}")
    print(f"Subject 3  : {mark_3}")
    print("--------------------------------")
    print(f"Total      : {total_marks} / 300")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Result     : {result}")
    print("================================")


display_student_report("Rahul", 75, 80, 65)

display_student_report("Priya", 35, 45, 40)

display_student_report("Aman", 20, 30, 25)

display_student_report("Neha", 100, 100, 100)

# --------------------------------------------------------

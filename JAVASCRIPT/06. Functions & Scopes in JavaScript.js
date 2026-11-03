//=====================================================================================================================================================================
Section 1: What Is a Function?
//=====================================================================================================================================================================
    
// 1. Why do we use functions instead of writing the same code again and again? Explain with one simple example.

To reuse code and avoid repetition.
Example: Write a welcome message function once and call it whenever needed.
    
// 2. List any four advantages of functions and write one line for each advantage.

Reusability: Use code multiple times.
Less repetition: Avoid duplicate code.
Easy debugging: Find errors easily.
Readability: Makes code clear and organized.
    
// 3. Imagine you have to display a welcome message at 6 different places in your program. How will a function help you here?

Create one welcome() function.
Call it 6 times wherever needed.
    
// 4. Show the same code written twice without a function and once with a function.

Without function:

console.log("Welcome");
console.log("Welcome");

With function:

function welcome() {
    console.log("Welcome");
}
welcome();
welcome();    
    
// 5. Give one real-life analogy that explains the idea of a function.

A washing machine performs the same task whenever we press the start button.
Similarly, a function performs a task whenever called.
    
// 6. Why do functions make debugging easier? Answer in 1–2 lines.

Errors can be found and fixed in one place.
This saves time and effort.

//=====================================================================================================================================================================
// Section 2: Function Declaration
//=====================================================================================================================================================================

// 1. Create a function declaration named displayCourse that returns "JavaScript Fundamentals". Call it and print the result.

function displayCourse(){
    return "JavaScript Fundamentals";
}console.log(displayCourse());

// 2 .Write a function declaration getStudentStatus that returns the string "Active Learner". Store the returned value in a variable and print it.

function getStudentStatus(){
    return "Active Learner";
}console.log(getStudentStatus());

// 3. Write a function declaration and call it before its definition. What happens and why? Explain briefly.

greet()
function greet(){
    console.log("Hello!");
}

//=====================================================================================================================================================================
// Section 3: Function Expression
//=====================================================================================================================================================================

// 1. Create a function expression named showMotto that returns "Code. Learn. Grow.". Call it and print the output.

const showMotto = function(){
    return "Code. Learn. Grow.";
}
console.log(showMotto());

// 2. Write a function expression getSemester that returns the number 3. Print the value returned by the function.

const getSemester = function(){
    return 3;
}
console.log(getSemester());

// 3. Create a function expression and try to call it before writing the expression. What error do you get and why?

console.log(welcomeMessage());
const welcomeMessage = function() {
    return "Welcome to the JavaScript session!";
};// ReferenceError:

//=====================================================================================================================================================================
// Section 4: Function Calling (Invocation)
//=====================================================================================================================================================================

// 1. Write a function declaration greetStudent that returns "All the best for your coding journey!". Call this function four times.

function greetStudent(){
    console.log ("All the best for your coding journey!");
}
greetStudent()
greetStudent()
greetStudent()
greetStudent()

// 2. Create a function expression todayFocus that returns "Focus on functions today". Store the result in a variable and print that variable.

const todayFocus = function(){
    return "Focus on functions today";
}
let xyz = todayFocus()
console.log(xyz);

// 3. Write one function declaration and one function expression. Call each of them twice and print all four results.

const Subject = function(){
    console.log("Mathematics")
}
Subject()
Subject()

function subject(){
    console.log("Python")
}
subject()
subject()

//=====================================================================================================================================================================
// Section 5: Parameters vs Arguments
//=====================================================================================================================================================================

// Practical Questions

// 1. Write a function declaration subtract(a, b) that returns the difference of two numbers. Call it with arguments 50 and 18 and print the result.

function subtract(a, b){
    return a-b;
}console.log(subtract(50, 18))

// 2. Create a function expression greetUser(name) that returns "Welcome, " + name + "!". Call it with the argument "Aarav".

const greetUser = function(name){
    return "Welcome, " + name + "!";
}
console.log(greetUser("Aarav"))

// 3. Write a function calculateArea(length, breadth) that returns the area of a rectangle. Call it twice with different pairs of arguments: (12, 5) and (8, 9).

function calculateArea(length, breadth){
    return length*breadth;
}
console.log(calculateArea(12,5))
console.log(calculateArea(8,9))

// Theory Questions

// 4. What is the difference between a parameter and an argument? Explain with a short example.

Parameter: Variable defined in a function.
Argument: Actual value passed when calling a function.
    
function greet(name) {  // Parameter
    console.log(name);
}
greet("Riya");  // Argument

// 5. Can a function have parameters but be called without arguments? What happens in that case? Explain briefly.

The parameter gets the value undefined.
No error occurs unless the function requires a valid value.
    
function greet(name) {
    console.log(name);
}
greet();  // Output: undefined

//=====================================================================================================================================================================
// Section 6: Return Statement
//=====================================================================================================================================================================

// Practical Questions

// 1. Write a function squareOfNumber(n) that returns the square of the given number. Call it with 9 and print the returned value.

function squareOfNumber(n){
    return n**2;
}console.log(squareOfNumber(9))

// 2. Create a function isAdult(age) that returns true if age is 18 or above, otherwise returns false. Test it with 17 and 20.

function isAdult(age){
    if (age>=18){
        return "True";
    }else{
        return "False"
    }
}
console.log(isAdult(17))
console.log(isAdult(20))


// 3. Write a function getFullName(firstName, lastName) that returns the full name. Call it with "Rohit" and "Sharma" and print the result.

function getFullName(firstName, lastName){
    return firstName+" "+lastName;
}console.log(getFullName("Rohit", "Sharma"))

// Theory Questions

// 4. What does a function return if there is no return statement inside it?

It returns undefined by default.

// 5. Why do we use the return statement in a function instead of just using console.log() inside the function? Explain in 2–3 lines.

return: Sends the result back to the caller for further use.
console.log(): Only displays the result on the console.
return makes the result reusable.

//=====================================================================================================================================================================
// Section 7: Why Use Functions? (Real-world Example)
//=====================================================================================================================================================================

// Practical Questions

// 1. You need to calculate the total marks of three subjects for 4 different students. Write a function getTotal(m1, m2, m3) and call it four times with different marks instead of repeating the addition code.

function getTotal(m1, m2, m3){
    return m1+m2+m3
}
console.log("Student 01 Total Marks ---> ", getTotal(100, 100, 100))
console.log("Student 02 Total Marks ---> ", getTotal(100, 90, 60))
console.log("Student 03 Total Marks ---> ", getTotal(60, 70, 70))

// 2. Create a function calculateSimpleInterest(principal, rate, time) that returns the simple interest. Use the function to find interest for two different sets of values.

function calculateSimpleInterest(principal, rate, time) {
    return (principal*rate*time)/100
}console.log(calculateSimpleInterest(5000,5,2))
console.log(calculateSimpleInterest(10000,4,3))

// 3. Without using a function, write code to find the average of three numbers twice (for two students). Then rewrite the same logic using a single function findAverage(a, b, c) and call it twice.

let m1 = 85, m2 = 92, m3 = 78;
let avg1 = (m1 + m2 + m3) / 3;

let x1 = 70, x2 = 60, x3 = 80;
let avg2 = (x1 + x2 + x3) / 3;

function average(a, b, c) {
    return (a + b + c) / 3;
}

console.log(average(85, 92, 78)); // For Jenil
console.log(average(70, 60, 80)); // For Mahir

// Theory Questions

// 4. How do functions help in reducing code repetition? Explain with one real-world example.

Write code once and reuse it whenever needed.
Example: A calculator uses one addition function for multiple calculations.

// 5. Mention any three advantages of using functions in a program.

Reusability: Use code multiple times.
Less repetition: Avoid writing the same code again.
Easy debugging: Find and fix errors easily.

//=====================================================================================================================================================================

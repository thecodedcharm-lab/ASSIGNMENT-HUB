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
// Section 8: Function Scope
//=====================================================================================================================================================================

// Practical Questions

// 1. Create a function showCity that declares a local variable city = "Ahmedabad" and prints it. After calling the function, try to print city outside and note what happens.

function showCity() {
    let city = "Ahmedabad";
    console.log(city);
}

showCity();

// console.log(city);              // ReferenceError: city is not defined

// 2. Declare a global variable trainer = "CodingGita Mentor". Write a function displayTrainer that prints this global variable. Call the function and also print the variable outside the function.

let trainer = "CodingGita Mentor";

function displayTrainer() {
    console.log(trainer);
}

displayTrainer();

// console.log(trainer);              // ReferenceError: city is not defined

// 3. Write a function demoScope that contains a local variable value = 50. Print the variable inside the function. Then try accessing the same variable outside and explain the output/error.

function demoScope() {
    let value = 50;
    console.log(value);
}

demoScope();

// console.log(value);                 // ReferenceError: city is not defined

// Theory Questions

// 4. A variable declared inside a function cannot be used outside. Why does JavaScript follow this rule? How does it help in writing better programs?

// JavaScript follows this rule to protect local variables from being accessed or changed outside the function. It helps avoid errors, prevents variable name conflicts and makes programs easier to manage.

// 5. What will happen if a global variable and a local variable have the same name? Which one will the function use? Explain briefly.

// If a global and local variable have the same name, the function uses the local variable because it has priority inside that function. The global variable remains unchanged.

let num = 10;

function show() {
    let num = 20;
    console.log(num);
}

show();
console.log(num);

//=====================================================================================================================================================================
// Section 9: Combining Function Concepts
//=====================================================================================================================================================================

// Practical Questions

// 1. Write a function generateMessage(name, score) that calculates whether the student has passed (score ≥ 40) and returns a complete sentence like: "Aarav has scored 65 and the result is Pass".

function generateMessage(name, score) {
    if (score >= 40) {
        return name + " has scored " + score + " and the result is Pass";
    }
    else {
        return name + " has scored " + score + " and the result is Fail";
    }
}

console.log(generateMessage("Aarav", 65));

// 2. Create a function billCalculator(item1, item2, item3) that returns the total amount and also mentions if the customer gets a discount (total ≥ 1000 → "Discount Applied", otherwise "No Discount").

function billCalculator(item1, item2, item3) {
    let total = item1 + item2 + item3;

    if (total >= 1000) {
        return "Total = " + total + " Discount Applied";
    }
    else {
        return "Total = " + total + " No Discount";
    }
}

console.log(billCalculator(400, 350, 300));

// 3. Write a function performanceReport(student, m1, m2, m3) that calculates total and average, then returns a formatted string containing name, total, average and a remark ("Excellent" if average ≥ 80, otherwise "Keep Improving").

function performanceReport(student, m1, m2, m3) {
    let total = m1 + m2 + m3;
    let average = total / 3;

    if (average >= 80) {
        return student + " Total = " + total + " Average = " + average + " Excellent";
    }
    else {
        return student + " Total = " + total + " Average = " + average + " Keep Improving";
    }
}

console.log(performanceReport("Aarav", 90, 85, 95));

// Theory Questions

// 4. Why is it better to perform multiple related tasks (calculation + decision + message) inside one function instead of writing separate pieces of code?

// It is better because it keeps related code together. It makes the program shorter, easier to understand, reusable and easier to maintain.

// 5. How does combining concepts like parameters, return and conditions inside a single function improve code quality?

// Parameters allow us to give different inputs, conditions help make decisions, and return gives the final result. Combining them makes functions reusable, organized and efficient.

//=====================================================================================================================================================================
// Section 10: Nested Functions
//=====================================================================================================================================================================

// Practical Questions

// 1. Write a function mainTask that contains an inner function helperTask. The inner function should return "Task completed successfully". Call the inner function from mainTask and return its result.

function mainTask() {
    function helperTask() {
        return "Task completed successfully";
    }

    return helperTask();
}

console.log(mainTask());

// 2. Create a function calculateFinal(m1, m2) that has an inner function getTotal to add the marks. Use the inner function and return a message: "Final marks = " followed by the total.

function calculateFinal(m1, m2) {
    function getTotal() {
        return m1 + m2;
    }

    return "Final marks = " + getTotal();
}

console.log(calculateFinal(40, 50));

// 3. Write a function studentStatus(name, marks) containing an inner function getGrade. The inner function returns "A" if marks ≥ 80, "B" if marks ≥ 60, otherwise "C". Return a final sentence using the name and grade.

function studentStatus(name, marks) {
    function getGrade() {
        if (marks >= 80) {
            return "A";
        }
        else if (marks >= 60) {
            return "B";
        }
        else {
            return "C";
        }
    }

    return name + " has grade " + getGrade();
}

console.log(studentStatus("Aarav", 85));

// Theory Questions

// 4. What is the main advantage of writing a function inside another function? When should we use nested functions?

// The main advantage is that we can keep helper functions inside the main function. It makes code organized and prevents unnecessary access to helper functions from outside.

// We use nested functions when a smaller task is needed only inside another function.

// 5. Can an inner function access variables of the outer function? What about the reverse (outer accessing inner variables)? Explain.

// Yes, an inner function can access variables of its outer function because of lexical scope.

// But the outer function cannot directly access variables declared inside the inner function.

function outer() {
    let a = 10;

    function inner() {
        let b = 20;
        console.log(a);
        console.log(b);
    }

    inner();

    console.log(a);
    // console.log(b); Error
}

outer();

//=====================================================================================================================================================================

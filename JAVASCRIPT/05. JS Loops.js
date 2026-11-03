//  JavaScript Assignment: for Loop

// Q1. Counting Numbers 🔢

for (let i = 1; i <= 15; i++) {
  console.log(i);
}

// Q2. Even Numbers 🎯

for (let i = 2; i <= 40; i+=2) {
  console.log(i);
}

// Q3. Odd Numbers 🏃

for (let i = 1; i <= 35; i+=2) {
  console.log(i);
}

// Q4. Saving Money 💰

let savings = 0;
for (let i = 1; i <= 10; i++) {
  savings += i*10;
}
console.log("Total savings after 10 days:", "₹" + savings);

// Q5. Multiplication Table 📚

let num = 12;
for (let i =1 ; i<=10;i++){
    console.log(`${num} x ${i} = ${num * i}`)
}

// Q6. Daily Water Intake 💧

let glasses = 0
for (let i = 1 ; i <= 7 ; i++ ){
  glasses+=3
  console.log(`DAY ${i} : ${glasses} Glasses 💧`)
}

// Q7. Shopping Calculation 🛍️

let cost = 0
for ( let i = 1 ; i <= 10; i++ ){
  cost+= 15
  console.log(`${i} Chocolate🍫 = ₹${cost} `)
}

// Q8. Sum of Even Numbers ➕

let sum = 0
for (let i = 2; i <= 30; i+=2) {
  sum+=i
}
console.log(`Sum of even numbers: ${sum} 🧮`);

// Q9. Weekly Exercise 💪

let pushUp = 0
for (let i = 1 ; i <= 7 ; i++ ){
  pushUp+=5
  console.log(`DAY ${i} : ${pushUp} push-ups💪`)
}

// Q10. Movie Tickets 🎬

let Cost = 0
for ( let i = 1 ; i <= 10; i++ ){
  Cost+= 150
  console.log(`${i} people👩‍🦱 = ₹${Cost} `)
}

// Part B] For Loop (Additional advanced questions)

// 1.
// Given an array of temperatures [28, 32, 25, 40, 18, 35],
// use a for loop to count how many days were hotter than 30°C.
let temperature = [28, 32, 25, 40, 18, 35]
let count = 0
for (i=0;i<temperature.length;i++){
    if (temperature[i]>30){
        count+=1
    }
}
console.log(count)

// 2.
// Write a for loop that calculates the sum of all digits 
// of a given number (example: 4729 → 4+7+2+9 = 22).
let number = 4729;
let sum = 0;
for (; number > 0; number = Math.floor(number / 10)) {
    sum += number % 10;
}
console.log("Sum of digits:", sum);

// 3.
// Create a for loop that prints only the numbers between 1 
// and 100 that are divisible by both 3 and 5, but not by 7.
for (i=1;i<=100;i++){
    if(i%3==0 && i%5==0 && i%7!=0){
        console.log(i)
    }
}

// 4.
// Given the string "JavaScript", use a for loop to create a new 
// string that contains only the consonants (remove vowels).
let string="JavaScript";
for(i=0;i<string.length;i++){
    console.log(string[i])
}

// 5.
// Write a for loop that finds the largest number in an array
// of positive integers without using any sorting method.
let numbers = [12, 45, 23, 89, 34, 67];
let largest = numbers[0];
for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > largest) {
        largest = numbers[i];
    }
}
console.log("Largest number:", largest);

// 6.
// Use a for loop to check whether a given number is a perfect
// number (a number equal to the sum of its proper divisors). 
// Example: 28.
let Number = 28;
let Sum = 0;
for (let i = 1; i < Number; i++) {
    if (Number % i === 0) {
        Sum += i;
    }
}
if (Sum === Number) {
    console.log(Number, "is a perfect number");
} else {
    console.log(Number, "is not a perfect number");
}

// 7.
// Print the following series using a single for loop:
// 1 2 4 8 16 32 64 128
let num = 1;
for (let i = 1; i <= 8; i++) {
    console.log(num);
    num *= 2;
}

// 8.
// Write a for loop that prints the first 20 Fibonacci 
// numbers (starting with 0 and 1).
let first = 0;
let second = 1;
for (let i = 1; i <= 20; i++) {
    console.log(first);
    let next = first + second;
    first = second;
    second = next;
}

// 9.
// Given an array of student scores [45, 78, 90, 32, 56, 88],
// use a for loop to calculate the average and also count how 
// many students scored above the average.
let scores = [45, 78, 90, 32, 56, 88];
let SUM = 0;
for (let i = 0; i < scores.length; i++) {
    SUM += scores[i];
}
let average = SUM / scores.length;
let Count = 0;
for (let i = 0; i < scores.length; i++) {
    if (scores[i] > average) {
        Count++;
    }
}
console.log("Average score:", average);
console.log("Students scoring above average:", Count);

// 10.
// Write a for loop that converts a decimal number to its binary 
// representation (without using built-in methods like toString(2)).
let NUM = 13;
let binary = "";
for (; NUM > 0; NUM = Math.floor(number / 2)) {
    binary = (NUM % 2) + binary;
}
console.log("Binary:", binary);

// Part C-a: `break` Inside a `for` Loop

// Q1. Find the First Occurrence of Number 7


let numbers = [3, 5, 7, 9, 7, 2];

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] === 7) {
        console.log("Number 7 found at index:", i);
        break;
    }
}



// Number 7 found at index: 2


// Q2. Password Checker


let password = 1234;
let flag = false
for ( let i =1 ; i <= 5 ; i++ ){
    let enterPasword = prompt("Enter the Password : ");
    if (parseInt(enterPasword)===password){
        console.log("Access Granted")
        flag = true;
        break
    }
}

if (!flag){
    console.log("Account Locked")
}


// Q3. Add Numbers Until the Sum Exceeds 100

let sum = 0;

for (let i = 1; ; i++) {
    sum += i;

    if (sum > 100) {
        console.log("Last number added:", i);
        console.log("Sum:", sum);
        break;
    }
}


//Q4. Find the First Name Starting with S

let names = ["Riya", "Aman", "Sneha", "Karan", "Sahil"];

for (let i = 0; i < names.length; i++) {
    if (names[i][0] === "S") {
        console.log("First name starting with S:", names[i]);
        break;
    }
}


// Q5. Stop at the First Perfect Square Greater Than 20


for (let i = 1; i <= 50; i++) {
    if (i > 20 && Number.isInteger(Math.sqrt(i))) {
        console.log("First perfect square greater than 20:", i);
        break;
    }
}


// // Part C-b: `continue` Inside a `for` Loop

// Q1. Print Numbers from 1 to 30, Skipping Multiples of 4

for (let i = 1; i <= 30; i++) {
    if (i % 4 === 0) {
        continue;
    }

    console.log(i);
}

// Q2. Sum of Positive Numbers

let num = [10, -5, 20, -8, 15, -3];
let Sum = 0;

for (let i = 0; i < num.length; i++) {
    if (num[i] <= 0) {
        continue;
    }

    Sum += num[i];
}

console.log("Sum of positive numbers:", sum);

// Q3. Print Characters of Hello World, Skipping Spaces

let str = "Hello World";
for (let i = 0; i < str.length; i++) {
    if (str[i] === " ") {
        continue;
    }

    console.log(str[i]);
}

// Q4. Multiplication Table of 6, Skipping Products Divisible by 5

for (let i = 1; i <= 12; i++) {
    let product = 6 * i;

    if (product % 5 === 0) {
        continue;
    }

    console.log("6 x " + i + " = " + product);
}
// Q5. Print Ages of People Eligible to Vote

let ages = [12, 18, 25, 15, 30, 17, 22];

for (let i = 0; i < ages.length; i++) {
    if (ages[i] < 18) {
        continue;
    }
    console.log("Eligible age:", ages[i]);
}

// Part D] Reverse For Loop

// 1.
// Write a reverse for loop that prints all numbers from 50 
// down to 1 that are divisible by 3 but not divisible by 9.

for (let i=50 ; i>=1;i--){
    if(i%3==0 && i%9!=0){
        console.log(i)
    }
}

// 2.
// Write a reverse for loop that calculates the product of 
// all odd digits of a given number (example: 4729 → 7 × 9 = 63).

let givenNumber = "4729"
let product = 1
for(let i=givenNumber.length ; i>0 ; i-- ){
    if (i % 2 != 0){
        product=product*Number(givenNumber[i])
    }
}
console.log("Product of all odd digits : ", product)

//3.
// Given the string "Programming", use a reverse for loop 
// to create a  new string that contains only the consonants 
// in reverse order.

let string = "Programming"
let bag = ""

for (let i = string.length - 1; i >= 0; i--) {
    if (string[i] != "A" && string[i] != "E" && string[i] != "I" && string[i] != "O" && string[i] != "U" && string[i] != "a" && string[i] != "e" && string[i] != "i" && string[i] != "o" && string[i] != "u") {
        bag += string[i]
    }
}

console.log(bag)

// 4.
// Write a reverse for loop that prints the first 15 Fibonacci numbers
// in reverse order (starting from the 15th number down to 0).

// 5.
// Use a reverse for loop to check whether a given number is a
// palindrome by comparing digits from both ends (without converting 
// the number to a string)

// // 6.
// // Given an array [12, 45, 7, 23, 56, 89, 34], use a reverse
// // for loop to find the largest number that is less than 50 
// // (do not use any built-in methods).
const arr = [12, 45, 7, 23, 56, 89, 34];
let largest = -1; 
for (let i = arr.length - 1; i >= 0; i--) {
  if (arr[i] < 50 && arr[i] > largest) {
    largest = arr[i];
  }
}

if (largest !== -1) {
  console.log("The largest number less than 50 is:", largest);
} else {
  console.log("No number is less than 50.");
}

// Part F]: Do-While Loop

// Q1. Print Numbers in Reverse
let i = 10
do{
    console.log(i)
    i--
}while(i>=1)

// Q2. Print Even Numbers
let i = 2
do{
    console.log(i)
    i+=2
}while(i<=20)

// Q3. Sum of Natural Numbers
let sum = 0
let n = Number(prompt("Input : "))
do{
  sum+=n
  n--
}while(n>=1)
console.log("The sum is : "+ sum)

// Q4. Product of Digits
let product = 1
let n = Number(prompt("Input : "))
do{
  let d = n % 10
  product *= d
  n=Math.floor(n/10)
}while(n>0)
console.log("The product of digit is :" +product)

// Q5. Find the First Digit
let firstDigit;
let n = Number(prompt("Input : "));
do{
  n=Math.floor(n/10)
    firstDigit=n%10
  }while(n>10)
console.log(firstDigit)

// Q6. Calculate a Power
let base = Number(prompt("Base = "));
let Exponent = Number(prompt("Exponent = "));
let result = 1;
do{result*=base
  Exponent--
}while(Exponent >=1)
console.log(result)

// Q7. Print Multiples with Conditions
let i = 1
do{
    if (i % 4 == 0 && i % 8 != 0){
        console.log(i)
    }
    i++
}while(i<=100)

//Q8. Check a Palindrome Number
let n = Number(prompt("Input: "))
let originalNumber = n
reverseNumber = 0
do{
  let d = n % 10;
  reverseNumber = (reverseNumber*10)+d;
  n=Math.floor(n/10)
}while(n>0)
if (reverseNumber === originalNumber){
  console.log(`${originalNumber} is a Palindrome number`)
}else{
  console.log(`${originalNumber} is not a Palindrome number`)
}

// Q9. Find the Greatest Common Divisor (GCD)
let a = 12;
let b = 18;
let smallest;
if (a<=b){
    smallest=a
}else{
    smallest=b
}

let i = 1;
let hcf = 1;
do{
    if (a % i == 0 && b % i == 0){
        hcf=i
    }
    i++
}while (i<=smallest )
console.log(hcf)

// Q10. Convert Decimal to Binary

let num = 13; 
let binary = "";
let originalNum=13

do {
    binary = (num % 2) + binary;
    num = Math.floor(num / 2);
} while (num > 0);

if (originalNum === 0) {
    binary = "0";
}

console.log("Input:", originalNum);
console.log("Output:", binary);

// A] Arithmetic Operators

// 1. Addition (+)

// Q1
let classOneCollection = 15000;
let classTwoCollection = 12500;
console.log(classOneCollection + classTwoCollection);

// Q2
let morningPages = 18;
let eveningPages = 25;
console.log(morningPages + eveningPages);

// Q3
let mondaySales = 125;
let tuesdaySales = 178;
console.log(mondaySales + tuesdaySales);

// Q4. Predict the output
let a = "10";
let b = 5;
let result = a + b;
console.log(result); // 105, number + string produces string concatenation

// Q5. Predict the output
let x = 5;
let y = "3";
let result2 = x + y;
console.log(result2); // 53, number + string produces string concatenation

// Q6
console.log(15 + 27);

// Q7
let bookPrice = 350;
let penPrice = 45;
console.log(bookPrice + penPrice);

// Q8. What is the result and why?
console.log("25" + 10); // 2510, string concatenation occurs

// Q9
let walletBalance = 2000;
let totalSpent = 750 + 320;
console.log(totalSpent);
console.log(walletBalance - totalSpent);

// Q10. Predict and explain the outputs
console.log(5 + "5" + 5); // 555, operations proceed left to right and concatenate strings
console.log(5 + 5 + "5"); // 105, numbers are added first, then concatenated
console.log("5" + 5 + 5); // 555, operations proceed left to right and concatenate strings


// 2. Subtraction (-)

// Q1
let busSeats = 80;
let occupiedSeats = 53;
console.log(busSeats - occupiedSeats);

// Q2
let initialMarks = 500;
let lostMarks = 35;
console.log(initialMarks - lostMarks);

// Q3
let warehouseBoxes = 2500;
let sentBoxes = 875;
console.log(warehouseBoxes - sentBoxes);

// Q4. Predict the output
let a = "10";
let b = 3;
let result = a - b;
console.log(result); // 7, the string is converted to a number

// Q5. Predict the output
let x = "20";
let y = "5";
let result2 = x - y;
console.log(result2); // 15, both strings are converted to numbers

// Q6
console.log(100 - 37);

// Q7
let tankWater = 500;
let waterUsed = 175;
console.log(tankWater - waterUsed);

// Q8. What is the result and why?
console.log("50" - 20); // 30, the string is converted to a number
console.log("50" - "20"); // 30, both strings are converted to numbers

// Q9
let apples = 240;
let morningSales = 95;
let eveningSales = 67;
console.log(apples - morningSales - eveningSales);

// Q10. Predict and explain the outputs
console.log("100" - 50); // 50, the string is converted to a number
console.log("abc" - 10); // NaN, abc cannot be converted to a number
console.log(10 - "5" - "2"); // 3, both strings are converted to numbers
console.log("10" - "5" - "2"); // 3, both strings are converted to numbers


// 3. Multiplication (*)

// Q1
let notebookPrice = 45;
let notebookQuantity = 8;
console.log(notebookPrice * notebookQuantity);

// Q2
let bottlesPerHour = 120;
let productionHours = 6;
console.log(bottlesPerHour * productionHours);

// Q3
let gardenRows = 7;
let plantsPerRow = 15;
console.log(gardenRows * plantsPerRow);

// Q4. Predict the output
let a = "5";
let b = 4;
let result = a * b;
console.log(result); // 20, the string is converted to a number

// Q5. Predict the output
let x = "10";
let y = "2";
let result2 = x * y;
console.log(result2); // 20, both strings are converted to numbers

// Q6
console.log(12 * 8);

// Q7
let pizzaPrice = 299;
let pizzaQuantity = 4;
console.log(pizzaPrice * pizzaQuantity);

// Q8. What is the result and why?
console.log("7" * 6); // 42, the string is converted to a number
console.log("7" * "6"); // 42, both strings are converted to numbers

// Q9
let unitsPerHour = 45;
let factoryHours = 8;
console.log(unitsPerHour * factoryHours);

// Q10. Predict and explain the outputs
console.log("5" * 3 * "2"); // 30, numeric strings are converted to numbers
console.log("abc" * 4); // NaN, abc cannot be converted to a number
console.log(10 * "2.5"); // 25, the string is converted to a number
console.log("10" * "2.5" * "0"); // 0, numeric strings are converted to numbers


// 4. Division (/)

// Q1
let pencils = 144;
let students = 12;
console.log(pencils / students);

// Q2
let trainDistance = 360;
let trainHours = 6;
console.log(trainDistance / trainHours);

// Q3
let companyMoney = 72000;
let departments = 9;
console.log(companyMoney / departments);

// Q4. Predict the output
let a = "20";
let b = 4;
let result = a / b;
console.log(result); // 5, the string is converted to a number

// Q5. Predict the output
let x = "100";
let y = "5";
let result2 = x / y;
console.log(result2); // 20, both strings are converted to numbers

// Q6
console.log(144 / 12);

// Q7
let totalStudents = 360;
let classrooms = 9;
console.log(totalStudents / classrooms);

// Q8
console.log("100" / 4); // 25
console.log("100" / "4"); // 25

// Q9
let totalBill = 2400;
let friends = 6;
console.log(totalBill / friends);

// Q10. Predict and explain the outputs
console.log(10 / 0); // Infinity, positive number divided by positive zero
console.log(-10 / 0); // -Infinity, negative number divided by positive zero
console.log(0 / 0); // NaN, zero divided by zero is undefined
console.log("20" / "4" / 2); // 2.5, numeric strings are converted to numbers
console.log("abc" / 5); // NaN, abc cannot be converted to a number


// 5. Modulus (%)

// Q1
let students = 53;
let groupSize = 5;
console.log(students % groupSize);

// Q2
let candies = 128;
let candiesPerBox = 10;
console.log(candies % candiesPerBox);

// Q3
let toys = 237;
let toysPerBox = 6;
console.log(toys % toysPerBox);

// Q4
let passengers = 185;
let busCapacity = 40;
console.log(passengers % busCapacity);

// Q5. Predict the output
let a = 10;
let b = 0;
let result = a % b;
console.log(result); // NaN, remainder with zero is undefined

// Q6
console.log(29 % 5);

// Q7
let chocolates = 23;
let chocolatesPerBox = 4;
console.log(chocolates % chocolatesPerBox);

// Q8. What is the result and why?
console.log(0 % 7); // 0, zero divided by seven has remainder zero
console.log(15 % 0); // NaN, remainder with zero is undefined

// Q9
let pages = 47;
let pagesPerSheet = 6;
console.log(Math.floor(pages / pagesPerSheet));
console.log(pages % pagesPerSheet);

// Q10. Predict and explain the outputs
console.log(17 % 5); // 2, remainder has the same sign as the dividend
console.log(-17 % 5); // -2, remainder has the same sign as the dividend
console.log(17 % -5); // 2, remainder has the same sign as the dividend
console.log(-17 % -5); // -2, remainder has the same sign as the dividend
console.log(10 % 0); // NaN, remainder with zero is undefined


// 6. Exponentiation (**)

// Q1
let side = 6;
console.log(side ** 3);

// Q2
let cellsPerSide = 9;
console.log(cellsPerSide ** 2);

// Q3
console.log(5 ** 4);

// Q4
let pixels = 1024;
console.log(pixels ** 2);

// Q5. Predict the output
let base = 2;
let power = -1;
let result = base ** power;
console.log(result); // 0.5, a negative exponent gives the reciprocal

// Q6
console.log(3 ** 4);

// Q7
let squareSide = 9;
console.log(squareSide ** 2);

// Q8. What is the result and are they the same?
console.log(2 ** 5); // 32
console.log(5 ** 2); // 25
// They are not the same because the base and exponent are different

// Q9. Predict and explain the outputs
console.log(2 ** 3 ** 2); // 512, exponentiation is right-associative: 2 ** (3 ** 2)
console.log((2 ** 3) ** 2); // 64, parentheses make the first exponentiation happen first
console.log(2 ** -3); // 0.125, a negative exponent gives the reciprocal
// console.log(-2 ** 2); // SyntaxError, parentheses are required around the negative base
console.log((-2) ** 2); // 4, the negative base is squared
console.log(4 ** 0.5); // 2, exponent 0.5 gives the square root

// Q10. Predict the output
let a = 10;
let b = 0;
let result = a ** b;
console.log(result); // 1, any nonzero number raised to the power zero is 1


// B] Assignment Operators

// 1. Simple Assignment (=)

// Q1
let studentName = "Priya";
let marks = 92;

// Q2
let score = 0;

// Q3
let a = 50;
let b = 50;
let c = 50;

// Q4. Predict the output
let x;
x = 100;
console.log(x); // 100, x is assigned the value 100

// Q5. Predict the output
let p = 15;
let q = p;
q = 30;
console.log(p, q); // 15 30, changing q does not change p


// 2. Add and Assign (+=)

// Q1
let playerScore = 80;
playerScore += 25;
console.log(playerScore);

// Q2
let walletBalance = 1500;
walletBalance += 120;
console.log(walletBalance);

// Q3. Predict the output
let count = 10;
count += 5;
console.log(count); // 15, adds five to count

// Q4. Predict the output
let msg = "Good";
msg += " Morning";
console.log(msg); // Good Morning, strings are concatenated

// Q5. What is the result and why?
let n = 20;
n += "5";
console.log(n); // 205, += concatenates when the right operand is a string


// 3. Subtract and Assign (-=)

// Q1
let health = 100;
health -= 35;
console.log(health);

// Q2
let stock = 300;
stock -= 45;
console.log(stock);

// Q3. Predict the output
let lives = 5;
lives -= 2;
console.log(lives); // 3, subtracts two from lives

// Q4. Predict the output
let num = "40";
num -= 15;
console.log(num); // 25, the string is converted to a number

// Q5. What is the result and why?
let x = "abc";
x -= 5;
console.log(x); // NaN, abc cannot be converted to a number


// 4. Multiply and Assign (*=)

// Q1
let price = 500;
price *= 1.18;
console.log(price);

// Q2
let quantity = 8;
quantity *= 3;
console.log(quantity);

// Q3. Predict the output
let amount = 200;
amount *= 1.1;
console.log(amount); // 220.00000000000003 may occur because of floating-point precision

// Q4. Predict the output
let val = "7";
val *= 3;
console.log(val); // 21, the string is converted to a number

// Q5. What is the result and why?
let y = "hello";
y *= 2;
console.log(y); // NaN, hello cannot be converted to a number


// 5. Divide and Assign (/=)

// Q1
let chocolates = 180;
chocolates /= 6;
console.log(chocolates);

// Q2
let distance = 300;
distance /= 5;
console.log(distance);

// Q3. Predict the output
let total = 400;
total /= 8;
console.log(total); // 50, divides total by eight

// Q4. Predict the output
let num = "100";
num /= 4;
console.log(num); // 25, the string is converted to a number

// Q5. What is the result and why?
let z = 50;
z /= 0;
console.log(z); // Infinity, a positive number divided by positive zero


// 6. Modulus and Assign (%=)

// Q1
let number = 47;
number %= 6;
console.log(number);

// Q2
let counter = 23;
counter %= 12;
console.log(counter);

// Q3. Predict the output
let num = 29;
num %= 5;
console.log(num); // 4, stores the remainder

// Q4. Predict the output
let x = "17";
x %= 3;
console.log(x); // 2, the string is converted to a number

// Q5. What is the result and why?
let m = 15;
m %= 0;
console.log(m); // NaN, remainder with zero is undefined


// 7. Exponentiation and Assign (**=)

// Q1
let side = 5;
side **= 3;
console.log(side);

// Q2
let number = 4;
number **= 2;
console.log(number);

// Q3. Predict the output
let base = 2;
base **= 5;
console.log(base); // 32, two is raised to the power five

// Q4. Predict the output
let n = 4;
n **= 0.5;
console.log(n); // 2, exponent 0.5 gives the square root

// Q5. What is the result and why?
let p = 2;
p **= -1;
console.log(p); // 0.5, a negative exponent gives the reciprocal


// C] Comparison Operators

// 1. Loose Equality (==)

// Q1
console.log("25" == 25);

// Q2
console.log(0 == false);

// Q3. Predict the output
console.log(10 == "10"); // true, loose equality converts the string to a number
console.log(null == undefined); // true, null and undefined are loosely equal

// Q4. Predict the output
console.log("" == 0); // true, an empty string converts to zero
console.log([] == false); // true, both sides are converted through loose equality rules

// Q5. Why does NaN == NaN return false?
console.log(NaN == NaN); // false, NaN is not equal to any value, including itself


// 2. Loose Inequality (!=)

// Q1
console.log("18" != 18);

// Q2
let password = "1234";
let userInput = 1234;
console.log(password != userInput);

// Q3. Predict the output
console.log(5 != "5"); // false, loose inequality converts the string to a number
console.log(0 != false); // false, loose inequality treats zero and false as equal

// Q4. Predict the output
console.log(null != undefined); // false, null and undefined are loosely equal
console.log("" != 0); // false, an empty string converts to zero

// Q5. What does NaN != NaN return and why?
console.log(NaN != NaN); // true, NaN is not equal to itself


// 3. Strict Equality (===)

// Q1
console.log("25" === 25); // false, strict equality does not convert different types

// Q2
console.log(0 === false);
console.log(null === undefined);

// Q3. Predict the output
console.log(10 === "10"); // false, number and string have different types
console.log(true === 1); // false, boolean and number have different types

// Q4. Predict the output
console.log("" === 0); // false, string and number have different types
console.log([] === false); // false, array and boolean have different types

// Q5. Why is === preferred over ==?
// Strict equality avoids implicit type conversion and gives more predictable comparisons.


// 4. Strict Inequality (!==)

// Q1
console.log("18" !== 18);

// Q2
console.log(0 !== false);
console.log(null !== undefined);

// Q3. Predict the output
console.log(5 !== "5"); // true, number and string have different types
console.log(true !== 1); // true, boolean and number have different types

// Q4. Predict the output
console.log("" !== 0); // true, string and number have different types
console.log(NaN !== NaN); // true, NaN is not strictly equal to itself

// Q5
let input = "5";
console.log(input !== "0");


// Part C] Relational Operators

// 5. Greater Than (>)

// Q1
let studentMarks = 78;
let passingMarks = 40;
console.log(studentMarks > passingMarks);

// Q2
let todayTemperature = 35;
let yesterdayTemperature = 28;
console.log(todayTemperature > yesterdayTemperature);

// Q3. Predict the output
console.log(15 > 10); // true
console.log(10 > 15); // false
console.log(10 > 10); // false

// Q4. Predict the output
console.log("20" > 15); // true, the string is converted to a number
console.log("5" > "10"); // true, strings are compared lexicographically
console.log("abc" > 10); // false, abc converts to NaN

// Q5. What is the result and why?
console.log(null > 0); // false, null converts to zero
console.log(undefined > 0); // false, undefined converts to NaN

// Q6
let stock = 120;
let itemsWanted = 85;
console.log(stock > itemsWanted);

// Q7. Predict and explain the outputs
console.log(true > false); // true, true converts to 1 and false converts to 0
console.log("10" > "2"); // false, the first character 1 comes before 2
console.log(NaN > 5); // false, comparisons involving NaN return false


// 6. Less Than (<)

// Q1
let boxCapacity = 50;
let currentWeight = 42;
console.log(currentWeight < boxCapacity);

// Q2
let age = 16;
let minimumAge = 18;
console.log(age < minimumAge);

// Q3. Predict the output
console.log(8 < 12); // true
console.log(20 < 10); // false
console.log(7 < 7); // false

// Q4. Predict the output
console.log("8" < 10); // true, the string is converted to a number
console.log("20" < "3"); // true, strings are compared lexicographically
console.log("hello" < 5); // false, hello converts to NaN

// Q5. What is the result and why?
console.log(null < 0); // false, null converts to zero
console.log(undefined < 0); // false, undefined converts to NaN

// Q6
let tankCapacity = 500;
let waterLevel = 375;
console.log(waterLevel < tankCapacity);

// Q7. Predict and explain the outputs
console.log(false < true); // true, false converts to 0 and true converts to 1
console.log("5" < "15"); // false, the first character 5 comes after 1
console.log(NaN < 10); // false, comparisons involving NaN return false


// 7. Greater Than or Equal To (>=)

// Q1
let distinctionMarks = 75;
let scoredMarks = 75;
console.log(scoredMarks >= distinctionMarks);

// Q2
let ticketPrice = 300;
let availableMoney = 300;
console.log(availableMoney >= ticketPrice);

// Q3. Predict the output
console.log(25 >= 25); // true
console.log(30 >= 25); // true
console.log(20 >= 25); // false

// Q4. Predict the output
console.log("25" >= 25); // true, the string is converted to a number
console.log("10" >= "2"); // false, strings are compared lexicographically
console.log(null >= 0); // true, null converts to zero

// Q5. What is the result and why?
console.log(undefined >= 0); // false, undefined converts to NaN

// Q6
let liftCapacity = 8;
let peopleInside = 8;
console.log(peopleInside >= liftCapacity);

// Q7. Predict and explain the outputs
console.log(true >= 1); // true, true converts to 1
console.log("" >= 0); // true, an empty string converts to zero
console.log(NaN >= NaN); // false, comparisons involving NaN return false


// 8. Less Than or Equal To (<=)

// Q1
let speedLimit = 60;
let vehicleSpeed = 60;
console.log(vehicleSpeed <= speedLimit);

// Q2
let studentScore = 39;
let passingScore = 40;
console.log(studentScore < passingScore);

// Q3. Predict the output
console.log(15 <= 20); // true
console.log(20 <= 15); // false
console.log(15 <= 15); // true

// Q4. Predict the output
console.log("15" <= 20); // true, the string is converted to a number
console.log("30" <= "5"); // true, strings are compared lexicographically
console.log(null <= 0); // true, null converts to zero

// Q5. What is the result and why?
console.log(undefined <= 0); // false, undefined converts to NaN

// Q6
let bagCapacity = 10;
let booksInside = 10;
console.log(booksInside < bagCapacity);

// Q7. Predict and explain the outputs
console.log(false <= 0); // true, false converts to zero
console.log("" <= 0); // true, an empty string converts to zero
console.log(NaN <= 5); // false, comparisons involving NaN return false


// Mixed Practice (>, <, >=, <=)

// Q1
let votingAge = 18;
console.log(18 >= votingAge);

let temperature = 32;
console.log(temperature < 35);

let score = 90;
console.log(score > 85);

// Q2. Predict the outputs
console.log(10 > 5 && 5 < 10); // true, both conditions are true
console.log("10" >= 10); // true, the string is converted to a number
console.log(null <= undefined); // false, undefined converts to NaN
console.log("5" < "10" && 5 > 2); // false, string comparison is false, so the whole AND expression is false

// Q3
let productPrice = 499;
let customerMoney = 500;
console.log(customerMoney >= productPrice);
console.log(customerMoney < productPrice);

let change = customerMoney - productPrice;
console.log(change);

// Q4. Explain why
console.log("10" > "2"); // false, strings are compared lexicographically, and 1 comes before 2
console.log(10 > 2); // true, numbers are compared by numerical value


// Part E: Increment / Decrement Operators (++ / --)

// Part a

// Q1. Increment Counter
let counter = 5;
counter++;
console.log(counter);

// Q2. Decrement Lives
let lives = 3;
lives--;
console.log(lives);

// Q3. Increment Score
let score = 10;
score++;
console.log(score);

// Q4. Decrement Items
let items = 8;
items--;
console.log(items);

// Q5. Increment Count Twice
let count = 0;
count++;
count++;
console.log(count);


// Part b

// Q6. Post-Increment
let x = 5;
let y = x++;
console.log(x, y); // 6 5, post-increment uses the old value before increasing x

// Q7. Pre-Increment
let a = 5;
let b = ++a;
console.log(a, b); // 6 6, pre-increment increases a before assigning its value to b

// Q8. Post-Decrement
let lives = 3;
let previousLives = lives--;
console.log(lives, previousLives); // 2 3, post-decrement uses the old value before decreasing lives

// Q9. Pre-Increment
let attempts = 0;
let currentAttempts = ++attempts;
console.log(attempts, currentAttempts); // 1 1, pre-increment increases attempts before assigning its value

// Q10. Increment and Decrement Points
let points = 100;
points++;
points--;
console.log(points);


// Part c

// Q11. Predict the Output
let x = 10;
let y = x++;
let z = ++x;
console.log(x, y, z); // 12 10 12, post-increment uses the old value and pre-increment increases x first

// Q12. Predict the Output
let a = 5;
let b = a-- + ++a;
console.log(a, b); // 5 10, a-- uses 5 then decreases a, and ++a increases it back to 5 before using it

// Q13. Predict the Output
let m = 7;
let n = --m + m++;
console.log(m, n); // 6 12, --m decreases m to 6 first, then m++ uses 6 and increases m to 7

// Q14. Predict the Output
let p = 3;
let q = p++ + ++p + p;
console.log(p, q); // 5 13, p++ uses 3, ++p increases p to 5, and the final p is 5

// Q15. Predict the Output
let val = 0;
val = val++ + ++val;
console.log(val); // 2, val++ uses 0 and ++val increases val to 2 before using it

// Part F]: Logical Operators

//  1. Logical AND &&

// 1.

let StoredUsername = "admin" ;
let StoredPassword = 1234 ;
let EnteredUsername =  "admin" ;
let EnteredPassword = 1234 ;
let correctUsername = StoredUsername===EnteredUsername;
let correctPassword = StoredPassword===EnteredPassword;
let valid = correctPassword && correctUsername;
console.log(valid)
if (valid == true){
    console.log("Correct Login Details! ")
}else{
    console.log("Invaild Login Details! ")
}

// 2.

let isLoggedIn = true;
let hasPermission = true;
let canAccess= isLoggedIn && hasPermission;
console.log(canAccess)

// 3.

let inStock = true
let price = 800
let inBuget = price <= 1000;
let canBeBought = inStock && inBuget;
console.log(canBeBought)

// 4.

let studentMarks = 75 ;
let studentAttendance = 80;
let passingMarks = studentMarks >= 65;
let passingAttendance = studentAttendance >= 70;
let isPassing = passingAttendance && passingMarks;
console.log(isPassing)

// 5.

let isWeekend = true;
let isHoliday = false;
let isParty = isHoliday && isWeekend;
console.log(isParty) 

// 6.

let a = 0;
let b = 10;
let result = a && b;
console.log(result); 
//0

// 7.

let x = 5;
let y = 10;
let result = (x > 3 && y) || 0;
console.log(result);
// 10

// 8.

let p = "Hello";
let q = "";
let r = "World";
let result = p && q && r;
console.log(result);
// empty space ""

// 9.

let val = 5;
let condition = val && (val = 0);
console.log(condition);
console.log(val);
// 0
// 0

// 10.

let x = 10;
let y = 20;
let result = (x && y) && (x > y);
console.log(result);
//false

// 2. Logical OR ||

// 1.

let passwordCorrect = true;
let otpValid = false;
let login = passwordCorrect || otpValid;
console.log(login);

// 2.

let isMember = false;
let hasCoupon = true;
let discountApplies = isMember || hasCoupon;
console.log(discountApplies);

// 3.

let age = 16;
let height = 155;
let isEntryAllowed = age > 18 || height > 150;
console.log( isEntryAllowed );

// 4.

let emailGiven = true;
let phoneGiven = false;
let isForValid = emailGiven || phoneGiven;
console.log( isForValid );

// 5.

let score = 900;
let timeBonus = true;
let gameLevelOpens = score>=1000 || timeBonus
console.log( gameLevelOpens );

// 6.

let a = 0;
let b = false;
let c = "";
let d = null;
let e = 42;
let result = a || b || c || d || e;
console.log(result);
//42

// 7.

let x = "Hello" || 0;
let y = 0 || "Hi";
console.log(x, y);
// Hello Hi

// 8.

let a = 10;
let b = 20;
let result = (a < 5) || (b > 15);
console.log(result);
// true

// 9. 

let val = 5;
let condition = val || (val = 0);
console.log(condition);
console.log(val);
// 5
// 5

// 10.

let x = "" || 0 || false || null || undefined || "OK";
console.log(x);
// OK

//Part G]: typeof Operator

//Part a:

//1.Declare a variable name = "Rahul" and print its type using typeof.
let name="Shreya";
console.log(typeof(name));

//2.Declare a variable age = 25 and print its type.
let age=25;
console.log(typeof(age));

//3.Declare a variable isStudent = true and print its type.
let isStudent=true;
console.log(typeof(isStudent));

//4.Declare a variable city (without assigning a value) and print its type.
let city;
console.log(typeof(city));

//5.Print the type of the value null.
let result=null;
console.log(typeof(result));

//part b

//6.Predict the output:
console.log(typeof 42);
console.log(typeof "Hello");
console.log(typeof true);
console.log(typeof undefined);

//7.Predict the output:
console.log(typeof null);
console.log(typeof {});
console.log(typeof []);

//8.Predict the output:
console.log(typeof NaN);
console.log(typeof Infinity);
console.log(typeof function(){});

//9.Create three variables:
price = 99.99
message = "Welcome"
isActive = false
//Print the type of each variable with a clear message.
console.log(typeof(price));
console.log(typeof(message));
console.log(typeof(isActive));

//10.Predict the output:
let value = null;
console.log(typeof value);
console.log(typeof value === "object");

//Part c:

//11.Predict the output:
console.log(typeof typeof 100);
console.log(typeof typeof "Hi");
console.log(typeof typeof true);

//12.Predict the output:
let a = 10;
let b = "10";
console.log(typeof a === typeof b);
console.log(typeof a == typeof b);

//13.Predict the output:
console.log(typeof null === "object");
console.log(typeof [] === "object");
console.log(typeof {} === "object");

//14.Predict the output:
let x;
console.log(typeof x);
x = null;
console.log(typeof x);
x = 0;
console.log(typeof x);

//15.Predict the output:
console.log(typeof NaN === "number");
console.log(typeof Infinity === "number");
console.log(typeof (1 / 0));


//Part H]: Type Coercion

//Part a:

//1.Convert the string "25" into a number using Number() and add 10 to it. Print the result.
let num="25";
let total=Number(num)+10;
console.log(total);

//2.Convert the number 100 into a string using String() and join it with " rupees". Print the result.
let price=100;
let amount=String(price) + "rupees";
console.log(amount);

//3.Convert the value 0 into a boolean using Boolean() and print it.
let value=0;
let conditions=Boolean(value);
console.log(conditions);

//4.Convert the value "Hello" into a boolean and print it.
let text="Hello";
let txt=Boolean(text);
console.log(txt);

//5.Use the unary + operator to convert "50" into a number and multiply it by 2.
let number="50";
let number2=+(50)*2;
console.log(number2)

//Part b:

//6.Predict the output:
console.log("10" - 5);
console.log("10" + 5);
console.log("10" * 2);
console.log("10" / 2);

//7.Predict the output:
console.log("5" - "2");
console.log("5" + "2");
console.log("5" * "2");
console.log("5" / "2");

//8.Predict the output:
console.log(Number("123"));
console.log(Number("123abc"));
console.log(Number(true));
console.log(Number(false));
console.log(Number(null));
console.log(Number(undefined));

//9.Predict the output:
console.log(Boolean(0));
console.log(Boolean(""));
console.log(Boolean("0"));
console.log(Boolean([]));
console.log(Boolean({}));
console.log(Boolean(null));

//10.Predict the output:
console.log(String(100));
console.log(String(true));
console.log(String(null));
console.log(String(undefined));
console.log(100 + "");

//Part c:

//11.Predict the output:
console.log("5" + 3 + 2);
console.log(5 + 3 + "2");
console.log("5" - 3 + 2);
console.log(5 - "3" + "2");

//12.Predict the output:
console.log(true + true);
console.log(true + false);
console.log(true + "false");
console.log(false + "true");

//13.Predict the output:
console.log(null + 5);
console.log(undefined + 5);
console.log(null + "5");
console.log(undefined + "5");

//14.Predict the output:
console.log([] + []);
console.log([] + {});
console.log({} + []);
console.log({} + {});

//15.Predict the output:
let a = "10";
let b = 5;
let c = a + b;
let d = a - b;
let e = +a + b;
console.log(c, typeof c);
console.log(d, typeof d);
console.log(e, typeof e);

//16.Predict the output:
console.log(!!"Hello");
console.log(!!"");
console.log(!!0);
console.log(!!1);
console.log(!!null);
console.log(!!undefined);

//17.Predict the output:
console.log(Number(""));
console.log(Number(" "));
console.log(Number("0"));
console.log(Number("  25  "));
console.log(Number("25px"));

//18.Predict the output:
let val1 = "5";
let val2 = 2;
console.log(val1 + val2);
console.log(+val1 + val2);
console.log(val1 - val2);
console.log(val1 * val2);
console.log(val1 / val2);

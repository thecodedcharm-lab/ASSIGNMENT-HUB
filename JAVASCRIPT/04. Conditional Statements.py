// ==================== A] if Statement ====================

// Q1. Divisible by 5
let number1 = 25;

if (number1 % 5 === 0) {
    console.log("Divisible by 5");
}


// Q2. Senior Citizen
let age1 = 65;

if (age1 >= 60) {
    console.log("Senior Citizen");
}


// Q3. Big Number
let number2 = 150;

if (number2 > 100) {
    console.log("Big Number");
}


// Q4. Very Cold
let temperature = 5;

if (temperature < 10) {
    console.log("Very Cold");
}


// Q5. Perfect Score
let marks1 = 100;

if (marks1 === 100) {
    console.log("Perfect Score");
}


// Q6. Negative Number
let number3 = -10;

if (number3 < 0) {
    console.log("Negative Number");
}


// Q7. Empty String
let userInput = "";

if (userInput === "") {
    console.log("No input provided");
}


// Q8. Century Year
let year1 = 2000;

if (year1 % 100 === 0) {
    console.log("Century Year");
}


// Q9. Positive Even Number
let number4 = 8;

if (number4 > 0 && number4 % 2 === 0) {
    console.log("Positive Even Number");
}


// Q10. Valid Marks
let marks2 = 75;

if (marks2 >= 35 && marks2 <= 100) {
    console.log("Valid Marks");
}



// ==================== B] if...else Statement ====================

// Q1. Even or Odd
let number5 = 7;

if (number5 % 2 === 0) {
    console.log("Even");
} else {
    console.log("Odd");
}


// Q2. Voting Eligibility
let age2 = 20;

if (age2 >= 18) {
    console.log("Eligible");
} else {
    console.log("Not Eligible");
}


// Q3. Positive or Negative
let number6 = -5;

if (number6 >= 0) {
    console.log("Positive");
} else {
    console.log("Negative");
}


// Q4. Pass or Fail
let marks3 = 60;

if (marks3 >= 35) {
    console.log("Passed");
} else {
    console.log("Failed");
}


// Q5. Uppercase Letter
let character = "A";

if (character >= "A" && character <= "Z") {
    console.log("Uppercase Letter");
} else {
    console.log("Not an Uppercase Letter");
}


// Q6. Divisible by 3
let number7 = 12;

if (number7 % 3 === 0) {
    console.log("Divisible by 3");
} else {
    console.log("Not Divisible by 3");
}


// Q7. Password Check
let password = "admin123";

if (password === "admin123") {
    console.log("Login Successful");
} else {
    console.log("Incorrect Password");
}


// Q8. Leap Year (Basic Rule)
let year2 = 2024;

if (year2 % 4 === 0) {
    console.log("Leap Year");
} else {
    console.log("Not a Leap Year");
}


// Q9. Greater of Two Numbers
let number8 = 25;
let number9 = 40;

if (number8 > number9) {
    console.log(number8 + " is Greater");
} else {
    console.log(number9 + " is Greater or Equal");
}


// Q10. Positive, Negative, or Zero
let number10 = 0;

if (number10 > 0) {
    console.log("Positive");
} else {
    if (number10 < 0) {
        console.log("Negative");
    } else {
        console.log("Zero");
    }
}



// ==================== C] if...else if...else Statement ====================

// Q1. Season Based on Month
let month = 4;

if (month === 12 || month === 1 || month === 2) {
    console.log("Winter");
} else if (month >= 3 && month <= 5) {
    console.log("Summer");
} else if (month >= 6 && month <= 8) {
    console.log("Monsoon");
} else if (month >= 9 && month <= 11) {
    console.log("Autumn");
} else {
    console.log("Invalid Month");
}


// Q2. Income Tax Calculator
let income = 500000;
let tax;

if (income < 300000) {
    tax = 0;
} else if (income <= 700000) {
    tax = income * 0.05;
} else if (income <= 1000000) {
    tax = income * 0.10;
} else {
    tax = income * 0.15;
}

console.log("Tax Amount: ₹" + tax);


// Q3. Student Score
let score = 85;

if (score >= 90) {
    console.log("Outstanding");
} else if (score >= 70) {
    console.log("Good");
} else if (score >= 40) {
    console.log("Average");
} else {
    console.log("Needs Improvement");
}


// Q4. Vehicle Speed
let speed = 60;

if (speed < 40) {
    console.log("Slow");
} else if (speed <= 80) {
    console.log("Normal");
} else {
    console.log("Fast");
}


// Q5. Height Category
let height = 165;

if (height < 150) {
    console.log("Short");
} else if (height <= 170) {
    console.log("Average");
} else {
    console.log("Tall");
}


// Q6. Weekday or Weekend
let day = 6;

if (day >= 1 && day <= 5) {
    console.log("Weekday");
} else if (day === 6 || day === 7) {
    console.log("Weekend");
} else {
    console.log("Invalid Day");
}


// Q7. Electricity Bill
let units = 120;
let bill;

if (units <= 50) {
    bill = units * 2;
} else if (units <= 150) {
    bill = units * 4;
} else {
    bill = units * 6;
}

console.log("Electricity Bill: ₹" + bill);


// Q8. Attendance Percentage
let attendance = 82;

if (attendance >= 90) {
    console.log("Excellent");
} else if (attendance >= 75) {
    console.log("Good");
} else if (attendance >= 50) {
    console.log("Satisfactory");
} else {
    console.log("Poor");
}


// Q9. Highest of Three Subject Marks
let subject1 = 78;
let subject2 = 92;
let subject3 = 85;

if (subject1 >= subject2 && subject1 >= subject3) {
    console.log("Highest Marks: " + subject1);
} else if (subject2 >= subject1 && subject2 >= subject3) {
    console.log("Highest Marks: " + subject2);
} else {
    console.log("Highest Marks: " + subject3);
}


// Q10. Number Type
let number11 = -7;

if (number11 === 0) {
    console.log("Zero");
} else if (number11 > 0 && number11 % 2 === 0) {
    console.log("Positive Even");
} else if (number11 > 0 && number11 % 2 !== 0) {
    console.log("Positive Odd");
} else if (number11 < 0 && number11 % 2 === 0) {
    console.log("Negative Even");
} else {
    console.log("Negative Odd");
}



// ==================== D] Nested if Statement ====================

// Q1. Greater Than 10 and Divisible by 3
let number12 = 15;

if (number12 > 10) {
    if (number12 % 3 === 0) {
        console.log("Greater than 10 and Divisible by 3");
    } else {
        console.log("Greater than 10 but Not Divisible by 3");
    }
}


// Q2. Voting with Voter ID
let age3 = 22;
let hasVoterId = true;

if (age3 >= 18) {
    if (hasVoterId) {
        console.log("Can Vote");
    }
}


// Q3. Passed with Distinction
let marks4 = 85;

if (marks4 >= 40) {
    if (marks4 >= 80) {
        console.log("Passed with Distinction");
    } else {
        console.log("Passed");
    }
} else {
    console.log("Failed");
}


// Q4. ATM System
let enteredPin = 1234;
let correctPin = 1234;
let balance = 5000;
let withdrawal = 2000;

if (enteredPin === correctPin) {
    if (balance >= withdrawal) {
        balance = balance - withdrawal;
        console.log("Withdrawal Successful");
        console.log("Remaining Balance: ₹" + balance);
    } else {
        console.log("Insufficient Balance");
    }
} else {
    console.log("Incorrect PIN");
}


// Q5. Leap Year
let year3 = 2024;

if (year3 % 4 === 0) {
    if (year3 % 100 === 0) {
        if (year3 % 400 === 0) {
            console.log("Leap Year");
        } else {
            console.log("Not a Leap Year");
        }
    } else {
        console.log("Leap Year");
    }
} else {
    console.log("Not a Leap Year");
}


// Q6. Valid Email
let email = "student@example.com";
let l = email.length

if (email.includes("@")) {
    let lastChar=email[l-4]+email[l-3]+email[l-2]+email[l-1];
    if (lastChar ==".com") {
        if (l > 10) {
            console.log("Valid Email");
        }
    }
}


// Q7. Online Shopping Discount
let cartTotal = 2000;
let isPremiumMember = true;
let finalAmount;

if (cartTotal >= 1000) {
    if (isPremiumMember == true) {
        finalAmount = cartTotal - cartTotal * 0.20;
    } else {
        finalAmount = cartTotal - cartTotal * 0.10;
    }
} else {
    finalAmount = cartTotal;
}

console.log("Final Amount: ₹" + finalAmount);


// Q8. Positive, Even, and Divisible by 4
let number13 = 12;

if (number13 > 0) {
    if (number13 % 2 === 0) {
        if (number13 % 4 === 0) {
            console.log("Positive Even and Divisible by 4");
        }
    }
}


// Q9. Job Eligibility
let age4 = 25;
let hasDegree = true;
let experience = 3;

if (age4 >= 21 && age4 <= 30) {
    if (hasDegree) {
        if (experience >= 2) {
            console.log("Eligible for Interview");
        }
    }
}


// Q10. Exam Eligibility
let isPresent = true;
let internalMarks = 35;
let externalMarks = 40;

if (isPresent) {
    if (internalMarks >= 30) {
        if (externalMarks >= 35) {
            console.log("Eligible for Final Exam");
        }
    }
}

```javascript
// ==================== D] Nested if Statement ====================

// Q1. Greater Than 10 and Divisible by 3
let number1 = 15;

if (number1 > 10) {
    if (number1 % 3 === 0) {
        console.log("Divisible by 3");
    } else {
        console.log("Not Divisible by 3");
    }
}


// Q2. Voting Eligibility
let age1 = 20;
let hasVoterId = true;

if (age1 >= 18) {
    if (hasVoterId) {
        console.log("Can Vote");
    }
}


// Q3. Passed with Distinction
let marks1 = 85;

if (marks1 >= 40) {
    if (marks1 >= 80) {
        console.log("Passed with Distinction");
    }
}


// Q4. ATM System
let enteredPin = 1234;
let correctPin = 1234;
let balance = 5000;
let withdrawal = 2000;

if (enteredPin === correctPin) {
    if (balance >= withdrawal) {
        console.log("Withdrawal Successful");
        balance = balance - withdrawal;
        console.log("Remaining Balance: ₹" + balance);
    } else {
        console.log("Insufficient Balance");
    }
} else {
    console.log("Incorrect PIN");
}


// Q5. Leap Year
let year1 = 2024;

if (year1 % 4 === 0) {
    if (year1 % 100 === 0) {
        if (year1 % 400 === 0) {
            console.log("Leap Year");
        } else {
            console.log("Not a Leap Year");
        }
    } else {
        console.log("Leap Year");
    }
} else {
    console.log("Not a Leap Year");
}


// Q6. Valid Email
let email = "student@example.com";

if (email.includes("@")) {
    if (email.endsWith(".com")) {
        if (email.length > 10) {
            console.log("Valid Email");
        }
    }
}


// Q7. Online Shopping Discount
let cartTotal1 = 2000;
let isPremiumMember = true;
let finalAmount1;

if (cartTotal1 >= 1000) {
    if (isPremiumMember) {
        finalAmount1 = cartTotal1 - cartTotal1 * 0.20;
    } else {
        finalAmount1 = cartTotal1 - cartTotal1 * 0.10;
    }
} else {
    finalAmount1 = cartTotal1;
}

console.log("Final Amount: ₹" + finalAmount1);


// Q8. Positive Even and Divisible by 4
let number2 = 12;

if (number2 > 0) {
    if (number2 % 2 === 0) {
        if (number2 % 4 === 0) {
            console.log("Positive Even and Divisible by 4");
        }
    }
}


// Q9. Job Eligibility
let age2 = 25;
let hasDegree = true;
let experience = 3;

if (age2 >= 21 && age2 <= 30) {
    if (hasDegree) {
        if (experience >= 2) {
            console.log("Eligible for Interview");
        }
    }
}


// Q10. Exam Eligibility
let isPresent = true;
let internalMarks = 35;
let externalMarks = 40;

if (isPresent) {
    if (internalMarks >= 30) {
        if (externalMarks >= 35) {
            console.log("Eligible for Final Exam");
        }
    }
}



// ==================== E] switch Statement ====================

// Q1. Days in a Month
let month = 2;

switch (month) {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        console.log("31 Days");
        break;

    case 4:
    case 6:
    case 9:
    case 11:
        console.log("30 Days");
        break;

    case 2:
        console.log("28 Days");
        break;

    default:
        console.log("Invalid Month");
}


// Q2. Vowel or Consonant
let character = "e";

switch (character.toLowerCase()) {
    case "a":
    case "e":
    case "i":
    case "o":
    case "u":
        console.log("Vowel");
        break;

    default:
        console.log("Consonant");
}


// Q3. Season Using Multiple Cases
let seasonNumber = 3;

switch (seasonNumber) {
    case 1:
    case 2:
        console.log("Winter");
        break;

    case 3:
    case 4:
        console.log("Summer");
        break;

    default:
        console.log("Invalid Number");
}


// Q4. Class Based on Marks
let marks2 = 78;
let studentClass;

switch (true) {
    case marks2 >= 75:
        studentClass = "Distinction";
        break;

    case marks2 >= 60:
        studentClass = "1st Class";
        break;

    case marks2 >= 50:
        studentClass = "2nd Class";
        break;

    case marks2 >= 35:
        studentClass = "3rd Class";
        break;

    default:
        studentClass = "Failed";
}

console.log(studentClass);


// Q5. Nested Switch for Role and Action
let role = "admin";
let action = "edit";

switch (role) {
    case "admin":
        switch (action) {
            case "create":
                console.log("Create Successful");
                break;

            case "edit":
                console.log("Edit Successful");
                break;

            case "delete":
                console.log("Delete Successful");
                break;

            default:
                console.log("Invalid Action");
        }
        break;

    case "user":
        console.log("Limited Access");
        break;

    default:
        console.log("Invalid Role");
}


// Q6. Predict and Correct the Output
let fruit = "mango";

switch (fruit) {
    case "apple":
        console.log("Apple is red");

    case "mango":
        console.log("Mango is yellow");

    case "banana":
        console.log("Banana is yellow");

    default:
        console.log("Unknown fruit");
}

// Output:
// Mango is yellow
// Banana is yellow
// Unknown fruit
// Explanation: Without break, execution continues into the following cases.

// Corrected Code
switch (fruit) {
    case "apple":
        console.log("Apple is red");
        break;

    case "mango":
        console.log("Mango is yellow");
        break;

    case "banana":
        console.log("Banana is yellow");
        break;

    default:
        console.log("Unknown fruit");
        break;
}


// Q7. Identify Different Values Using switch
let value = "0";

switch (value) {
    case 0:
        console.log("Number Zero");
        break;

    case "0":
        console.log("String Zero");
        break;

    case false:
        console.log("Boolean False");
        break;

    case null:
        console.log("Null Value");
        break;

    case undefined:
        console.log("Undefined Value");
        break;

    default:
        console.log("Other Value");
}

// Explanation: switch uses strict equality for matching.
// Therefore, 0, "0", false, null, and undefined are different values.


// Q8. Calculator
let number3 = 10;
let number4 = 3;
let operator = "**";

switch (operator) {
    case "+":
        console.log(number3 + number4);
        break;

    case "-":
        console.log(number3 - number4);
        break;

    case "*":
        console.log(number3 * number4);
        break;

    case "/":
        if (number4 !== 0) {
            console.log(number3 / number4);
        } else {
            console.log("Cannot divide by zero");
        }
        break;

    case "%":
        console.log(number3 % number4);
        break;

    case "**":
        console.log(number3 ** number4);
        break;

    default:
        console.log("Invalid Operator");
}


// Q9. Beginning, Middle, or End of Month
let date = 15;
let datePeriod;

switch (true) {
    case date >= 1 && date <= 10:
        datePeriod = "Beginning of the month";
        break;

    case date >= 11 && date <= 20:
        datePeriod = "Middle of the month";
        break;

    case date >= 21 && date <= 31:
        datePeriod = "End of the month";
        break;

    default:
        datePeriod = "Invalid Date";
}

console.log(datePeriod);


// Q10. Online Food Ordering System
let category = "veg";
let item = "pizza";
let size = "full";
let price;

switch (category) {
    case "veg":
        switch (item) {
            case "pizza":
                switch (size) {
                    case "half":
                        price = 150;
                        break;

                    case "full":
                        price = 250;
                        break;

                    default:
                        price = 0;
                }
                break;

            case "burger":
                switch (size) {
                    case "half":
                        price = 60;
                        break;

                    case "full":
                        price = 100;
                        break;

                    default:
                        price = 0;
                }
                break;

            default:
                price = 0;
        }
        break;

    case "nonveg":
        switch (item) {
            case "pizza":
                switch (size) {
                    case "half":
                        price = 200;
                        break;

                    case "full":
                        price = 350;
                        break;

                    default:
                        price = 0;
                }
                break;

            case "burger":
                switch (size) {
                    case "half":
                        price = 100;
                        break;

                    case "full":
                        price = 160;
                        break;

                    default:
                        price = 0;
                }
                break;

            default:
                price = 0;
        }
        break;

    default:
        price = 0;
}

if (price > 0) {
    console.log("Category: " + category);
    console.log("Item: " + item);
    console.log("Size: " + size);
    console.log("Final Price: ₹" + price);
} else {
    console.log("Invalid Order");
}



// ==================== F] Ternary Operator ====================

// Q1. Divisible by 7
let number5 = 21;

let result1 = number5 % 7 === 0
    ? "Divisible by 7"
    : "Not Divisible by 7";

console.log(result1);


// Q2. Temperature Check
let temperature = 32;

let result2 = temperature >= 30
    ? "Hot Day"
    : "Pleasant Day";

console.log(result2);


// Q3. Empty String
let text = "";

let result3 = text === ""
    ? "Empty String"
    : "String has content";

console.log(result3);


// Q4. Age Category
let age3 = 16;

let result4 = age3 < 13
    ? "Child"
    : age3 <= 19
        ? "Teenager"
        : "Adult";

console.log(result4);


// Q5. Greatest of Three Numbers
let a = 20;
let b = 35;
let c = 15;

let greatest = a >= b
    ? (a >= c ? a : c)
    : (b >= c ? b : c);

console.log(greatest);


// Q6. Student Marks Classification
let marks3 = 65;

let result5 = marks3 >= 75
    ? "Distinction"
    : marks3 >= 60
        ? "First Class"
        : marks3 >= 50
            ? "Second Class"
            : marks3 >= 35
                ? "Pass"
                : "Fail";

console.log(result5);


// Q7. Number Type
let number6 = -8;

let result6 = number6 === 0
    ? "Zero"
    : number6 > 0
        ? (number6 % 2 === 0 ? "Positive Even" : "Positive Odd")
        : (number6 % 2 === 0 ? "Negative Even" : "Negative Odd");

console.log(result6);


// Q8. Leap Year
let year2 = 2000;

let result7 = year2 % 4 === 0
    ? (year2 % 100 === 0
        ? (year2 % 400 === 0 ? "Leap Year" : "Not a Leap Year")
        : "Leap Year")
    : "Not a Leap Year";

console.log(result7);


// Q9. Role and Action
let userRole = "admin";
let userAction = "delete";

let result8 = userRole === "admin"
    ? (userAction === "delete"
        ? "Admin Delete"
        : userAction === "edit"
            ? "Admin Edit"
            : "Admin Other")
    : userRole === "user"
        ? (userAction === "view" ? "User View" : "User Restricted")
        : "Invalid Role";

console.log(result8);


// Q10. Discount and Final Amount
let cartTotal = 6000;

let discountDetails = {
    discountPercentage: cartTotal >= 5000
        ? 20
        : cartTotal >= 2000
            ? 10
            : cartTotal >= 1000
                ? 5
                : 0,

    finalAmount: cartTotal - cartTotal * (
        cartTotal >= 5000
            ? 0.20
            : cartTotal >= 2000
                ? 0.10
                : cartTotal >= 1000
                    ? 0.05
                    : 0
    )
};

console.log(discountDetails);

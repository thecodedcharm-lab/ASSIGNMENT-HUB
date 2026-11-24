// ==================== 1. push() ====================

// 1. Create an array of 3 colors. Use push() to add two more colors and print the final array.

let colors = ["Red", "Blue", "Green"];
colors.push("Yellow", "Pink");
console.log(colors);


// 2. Start with an empty array. Use push() three times to add the numbers 5, 10 and 15. Print the array.

let numbers = [];
numbers.push(5);
numbers.push(10);
numbers.push(15);
console.log(numbers);


// 3. Create an array ["Pen", "Book"]. Add "Eraser" and "Scale" using a single push() call and print the result.

let items = ["Pen", "Book"];
items.push("Eraser", "Scale");
console.log(items);


// 4. Where does push() add the new element(s) in the array?

// push() adds new elements at the end of the array.


// 5. Does push() change the original array? Explain in one sentence.

// Yes, push() modifies the original array by adding elements at the end.


// ==================== 2. pop() ====================

// 1. Create an array of 5 numbers. Use pop() twice and print the modified array and the two removed values.

let numbers1 = [10, 20, 30, 40, 50];
let removed1 = numbers1.pop();
let removed2 = numbers1.pop();

console.log(numbers1);
console.log(removed1);
console.log(removed2);


// 2. Create an array ["Red", "Blue", "Green"]. Remove the last element using pop() and print both the array and the removed element.

let colors1 = ["Red", "Blue", "Green"];
let removedColor = colors1.pop();

console.log(colors1);
console.log(removedColor);


// 3. Start with [100, 200, 300, 400]. Call pop() once and store the returned value in a variable. Print the variable and the array.

let numbers2 = [100, 200, 300, 400];
let removedNumber = numbers2.pop();

console.log(removedNumber);
console.log(numbers2);


// 4. What does pop() return?

// pop() returns the removed last element of the array.


// 5. What happens if you call pop() on an empty array?

// It returns undefined and the array remains empty.


// ==================== 3. unshift() ====================

// 1. Start with ["CSS", "JavaScript"]. Use unshift() to add "HTML" at the beginning and print the array.

let subjects1 = ["CSS", "JavaScript"];
subjects1.unshift("HTML");
console.log(subjects1);


// 2. Create an array [20, 30]. Add 5 and 10 at the beginning using unshift() and print the result.

let numbers3 = [20, 30];
numbers3.unshift(5, 10);
console.log(numbers3);


// 3. Create an empty array. Use unshift() to add three city names one by one and print the final array.

let cities1 = [];
cities1.unshift("Ahmedabad");
cities1.unshift("Mumbai");
cities1.unshift("Delhi");
console.log(cities1);


// 4. Where does unshift() add the new element(s)?

// unshift() adds new elements at the beginning of the array.


// 5. Can unshift() add more than one element at the same time? Give a short explanation.

// Yes, unshift() can add multiple elements at the beginning of an array using a single call.


// ==================== 4. shift() ====================

// 1. Create an array of 4 city names. Remove the first city using shift() and print the remaining array and the removed city.

let cities2 = ["Ahmedabad", "Mumbai", "Delhi", "Surat"];
let removedCity = cities2.shift();

console.log(cities2);
console.log(removedCity);


// 2. Create [10, 20, 30, 40]. Call shift() twice and print the final array and both removed values.

let numbers4 = [10, 20, 30, 40];
let removed3 = numbers4.shift();
let removed4 = numbers4.shift();

console.log(numbers4);
console.log(removed3);
console.log(removed4);


// 3. Start with ["Apple", "Banana", "Mango"]. Remove the first element and store it in a variable. Print the variable and the array.

let fruits1 = ["Apple", "Banana", "Mango"];
let removedFruit = fruits1.shift();

console.log(removedFruit);
console.log(fruits1);


// 4. How is shift() different from pop()?

// shift() removes the first element, whereas pop() removes the last element.


// 5. What does shift() return?

// shift() returns the removed first element of the array.


// ==================== 5. indexOf() ====================

// 1. Create an array of 6 fruits. Find the index of a fruit that exists and one that does not exist using indexOf().

let fruits2 = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Kiwi"];

console.log(fruits2.indexOf("Mango"));
console.log(fruits2.indexOf("Papaya"));


// 2. Create an array ["A", "B", "C", "B", "D"]. Print the index of "B" using indexOf().

let letters1 = ["A", "B", "C", "B", "D"];
console.log(letters1.indexOf("B"));


// 3. Create an array of 4 student names. Check the index of your name (or any name) and print the result.

let students1 = ["Jenil", "Mahir", "Arjun", "Krishna"];
console.log(students1.indexOf("Arjun"));


// 4. What does indexOf() return if the element is not found?

// indexOf() returns -1 if the specified element is not found.


// 5. What will indexOf() return if the element appears more than once in the array?

// indexOf() returns the index of the first occurrence of the element.


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


// ==================== 6. lastIndexOf() ====================

// 1. Create an array where one element is repeated 3 times. Use lastIndexOf() to find the last occurrence of that element.

let numbers5 = [10, 20, 10, 30, 10];
console.log(numbers5.lastIndexOf(10));


// 2. Create ["X", "Y", "Z", "Y", "X"]. Print the last index of "Y" and "X".

let letters2 = ["X", "Y", "Z", "Y", "X"];

console.log(letters2.lastIndexOf("Y"));
console.log(letters2.lastIndexOf("X"));


// 3. Create an array of 5 numbers with one number repeated. Find its last index using lastIndexOf().

let numbers6 = [5, 10, 20, 10, 30];
console.log(numbers6.lastIndexOf(10));


// 4. How is lastIndexOf() different from indexOf()?

// indexOf() returns the first occurrence of an element, whereas lastIndexOf() returns the last occurrence.


// 5. When would you prefer lastIndexOf() over indexOf()?

// We prefer lastIndexOf() when we want to find the last occurrence of an element in an array.


// ==================== 7. includes() ====================

// 1. Create an array of your friends' names. Check whether a particular name is present using includes() and print a suitable message.

let friends = ["Jenil", "Mahir", "Arjun", "Krishna"];

if (friends.includes("Mahir")) {
    console.log("Name found");
} else {
    console.log("Name not found");
}


// 2. Create an array of numbers [11, 22, 33, 44]. Check if 33 and 55 are present using includes().

let numbers7 = [11, 22, 33, 44];

console.log(numbers7.includes(33));
console.log(numbers7.includes(55));


// 3. Create an array of 4 subjects. Use includes() to check for one subject that exists and one that does not.

let subjects2 = ["Python", "JavaScript", "Maths", "English"];

console.log(subjects2.includes("Maths"));
console.log(subjects2.includes("Physics"));


// 4. What does includes() return?

// includes() returns true if the specified element exists in the array, otherwise it returns false.


// 5. Does includes() work the same way for both numbers and strings?

// Yes, includes() works with both numbers and strings.


// ==================== 8. reverse() ====================

// 1. Create an array of 5 numbers and reverse it. Print the array before and after reversing.

let numbers8 = [10, 20, 30, 40, 50];

console.log("Before:", numbers8);

numbers8.reverse();

console.log("After:", numbers8);


// 2. Create ["A", "B", "C", "D"]. Reverse the array and print the result.

let letters3 = ["A", "B", "C", "D"];
letters3.reverse();
console.log(letters3);


// 3. Create an array of 4 city names, reverse it, and print the final array.

let cities3 = ["Ahmedabad", "Mumbai", "Delhi", "Surat"];
cities3.reverse();
console.log(cities3);


// 4. Does reverse() create a new array or modify the original one?

// reverse() modifies the original array.


/* 5. What is the meaning of "in-place" when we say reverse() works in-place?

In-place means that the method modifies the original array directly instead of creating a new array. */


// ==================== 9. sort() – Basic Version ====================

// 1. Sort an array of 5 student names alphabetically and print the result.

let students2 = ["Mahir", "Jenil", "Arjun", "Krishna", "Dhruv"];
students2.sort();
console.log(students2);


// 2. Create an array ["Dog", "Cat", "Elephant", "Ant"] and sort it. Print the sorted array.

let animals = ["Dog", "Cat", "Elephant", "Ant"];
animals.sort();
console.log(animals);


// 3. Create the array [40, 100, 5, 25] and sort it. Print the result.

let numbers9 = [40, 100, 5, 25];
numbers9.sort();
console.log(numbers9);


// 4. Why does sort() give an incorrect order for the numbers [40, 100, 5, 25]?

// By default, sort() converts elements into strings and sorts them according to their Unicode values.


// 5. Does sort() change the original array?

// Yes, sort() modifies the original array.


// ==================== 10. join() ====================

// 1. Convert an array of 4 programming languages into a string separated by " | ".

let languages1 = ["Python", "JavaScript", "Java", "C++"];
let result1 = languages1.join(" | ");
console.log(result1);


// 2. Create ["HTML", "CSS", "JavaScript"]. Join them with " - " and print the string.

let languages2 = ["HTML", "CSS", "JavaScript"];
let result2 = languages2.join(" - ");
console.log(result2);


// 3. Create an array of 3 of your favorite subjects and join them using " / ".

let subjects3 = ["Python", "Maths", "English"];
let result3 = subjects3.join(" / ");
console.log(result3);


// 4. What happens if you do not pass any separator to join()?

// If no separator is passed, join() uses a comma between the elements.


// 5. What does join() return – an array or a string?

// join() returns a string.


// ==================== 11. concat() ====================

// 1. Create two arrays of numbers and combine them using concat(). Print the new array and both original arrays.

let arr1 = [10, 20];
let arr2 = [30, 40];

let result4 = arr1.concat(arr2);

console.log(result4);
console.log(arr1);
console.log(arr2);


// 2. Create arr1 = [1, 2] and arr2 = [3, 4]. Use concat() and print the result.

let arr3 = [1, 2];
let arr4 = [3, 4];

let result5 = arr3.concat(arr4);
console.log(result5);


// 3. Create three small arrays and combine all of them using a single concat() call.

let arr5 = [1, 2];
let arr6 = [3, 4];
let arr7 = [5, 6];

let result6 = arr5.concat(arr6, arr7);
console.log(result6);


// 4. Does concat() change the original arrays?

// No, concat() creates a new array without modifying the original arrays.


// 5. Can you combine more than two arrays using one concat() call?

// Yes, concat() can combine multiple arrays using a single call.


// ==================== 12. slice() ====================

// 1. From the array [5, 10, 15, 20, 25, 30], extract elements from index 2 to 5 using slice().

let numbers10 = [5, 10, 15, 20, 25, 30];
let result7 = numbers10.slice(2, 5);
console.log(result7);


// 2. Create [10, 20, 30, 40, 50]. Use slice(1, 4) and print both the new array and the original array.

let numbers11 = [10, 20, 30, 40, 50];
let result8 = numbers11.slice(1, 4);

console.log(result8);
console.log(numbers11);


// 3. Create an array of 6 numbers. Extract the first 3 elements using slice() and print them.

let numbers12 = [10, 20, 30, 40, 50, 60];
let result9 = numbers12.slice(0, 3);
console.log(result9);


// 4. Does slice() modify the original array?

// No, slice() creates a new array without modifying the original array.


// 5. What happens if you omit the second argument in slice()?

// It extracts elements from the specified starting index to the end of the array.


// ==================== 13. splice() ====================

// 1. Start with ["Jenil", "Mahir", "Arjun"]. Use splice() to insert "Krishna" between Jenil and Mahir.

let names = ["Jenil", "Mahir", "Arjun"];
names.splice(1, 0, "Krishna");
console.log(names);


// 2. Create [10, 20, 30, 40, 50]. Remove two elements starting from index 1 and insert a new number at that position. Print the final array.

let numbers13 = [10, 20, 30, 40, 50];
numbers13.splice(1, 2, 25);
console.log(numbers13);


// 3. Create [100, 200, 300]. Use splice() to replace 200 with 250 and print the array.

let numbers14 = [100, 200, 300];
numbers14.splice(1, 1, 250);
console.log(numbers14);


// 4. What is the main difference between slice() and splice()?

// slice() extracts elements without modifying the original array, whereas splice() adds, removes or replaces elements and modifies the original array.


// 5. Does splice() change the original array?

// Yes, splice() modifies the original array.


// ==================== 14. toString() ====================

// 1. Convert an array of your 4 favorite movies into a string using toString() and print it.

let movies = ["Avatar", "Titanic", "Interstellar", "Inception"];
let result10 = movies.toString();
console.log(result10);


// 2. Create [1, 2, 3, 4] and convert it to a string using toString(). Print the result.

let numbers15 = [1, 2, 3, 4];
let result11 = numbers15.toString();
console.log(result11);


// 3. Create an array of 3 subject names and convert it using toString().

let subjects4 = ["Python", "Maths", "English"];
let result12 = subjects4.toString();
console.log(result12);


// 4. How is toString() different from join()?

// toString() converts array elements into a string separated by commas, whereas join() allows us to specify a custom separator.


// 5. What separator does toString() use by default?

// toString() uses a comma as the separator.


// ==================== 15. fill() ====================

// 1. Create an array of 6 numbers and fill the entire array with the value 10.

let numbers16 = [1, 2, 3, 4, 5, 6];
numbers16.fill(10);
console.log(numbers16);


// 2. Create [1, 2, 3, 4, 5] and fill it with 0. Print the result.

let numbers17 = [1, 2, 3, 4, 5];
numbers17.fill(0);
console.log(numbers17);


// 3. Create an array of 4 elements and fill it with the string "Hello".

let words = [1, 2, 3, 4];
words.fill("Hello");
console.log(words);


// 4. Does fill() change the original array?

// Yes, fill() modifies the original array by replacing its elements with the specified value.


// 5. Can fill() change only a part of the array?

// Yes, fill() can replace elements within a specified range using starting and ending indexes.

let numbers18 = [1, 2, 3, 4, 5];
numbers18.fill(0, 1, 4);
console.log(numbers18);


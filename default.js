var lineBreak = "<br/>";

document.write("Hello world");
document.write("<h1>Welcome to JS practice</h1>");
document.write("<h2>Welcome to JS practice</h2>");

console.log("Welcome to JS program");

console.log("Welcome to JS practice stage");

document.write("<h3>Check this out</h3>");

alert("Welcome JS Program");

console.info("Welcome to JS program with info");
console.warn("Welcome to JS program with warn");
console.error("Welcome to JS program with error");

////////////////////////////////////////////////
var a = prompt("Welcome to JS program from var a");
console.log(a);

console.log(123, typeof 123);
console.log(123.5, typeof 123.5);

var car;
console.log(car);

var car = "";
console.log(typeof car);

var person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyecolor: "blue",
};

console.log(typeof person, person);
person = null;
console.log(typeof person, person);

////////////////////////////////////////////////
var name = "이승훈";
var age = 29;
var cgpa = 3.92;

document.write("이름 : " + name + lineBreak);
document.write("나이 : " + age + lineBreak);
document.write("성적 : " + cgpa + lineBreak);

var lastName = "홍";
var firstName = "길동";

var fullName = lastName + firstName;

console.log(fullName);
console.log("Today is " + "a" + "beautiful day");
console.log("My name is " + fullName);

////////////////////////////////////////////////
var num1 = 20;
var num2 = 30;
var sum = num1 + num2;
console.log(num1 + num2);
console.log("" + num1 + num2);

console.log(num1 + " + " + num2 + " = " + sum);

var text = prompt("Enter your name : ");
document.write("your name : " + text + lineBreak);

var len = text.length;
document.write("Number of characters : " + len + lineBreak);
document.write(text.charAt(2) + lineBreak);

document.write(text.toUpperCase() + lineBreak);
document.write(text.toLowerCase() + lineBreak);

////////////////////////////////////////////////
var text1 = "hi, ";
var text2 = "bye";
var text3 = text1.concat(text2);
document.write(text3 + lineBreak);
var text4 = "helloWorldThisIs";
var result = text4.slice(3, 5);
document.write(result + lineBreak);

////////////////////////////////////////////////
var num = 20;
num = num.toString();
console.log(typeof num);

var number = 20;
console.log(typeof number);

number = number.toString();
console.log(number, typeof number);

var x = 2.56789;
// 소수점 둘째 자리 수 까지 표현
console.log(x.toFixed(1), typeof x.toFixed(1));
console.log(x.toFixed(2));

console.log(x.toPrecision(1), typeof x.toPrecision(1));
console.log(x.toPrecision(2));

console.log(Number(true));
console.log(Number(false));
console.log(Number(" 10"));
console.log(Number(" 10 "));
console.log(Number("10.25"));

////////////////////////////////////////////////
var num1 = parseInt(prompt("Enter frist number : "));
var num2 = parseInt(prompt("Enter second number : "));

var result = num1 + num2;

document.write("the sum is : " + result + lineBreak);

////////////////////////////////////////////////
var input1 = prompt("Enter frist number : ");
var num1 = parseInt(input1);

var num2 = parseInt(prompt("Enter second number : "));

var result = num1 + num2;
document.write("the sum is : " + result + lineBreak);

result = num1 - num2;
document.write("the sub is : " + result + lineBreak);

result = num1 * num2;
document.write("the mul is : " + result + lineBreak);

result = num1 / num2;
document.write("the div is : " + result + lineBreak);

result = num1 % num2;
document.write("the remainer is : " + result + lineBreak);

////////////////////////////////////////////////
var base = parseFloat(prompt("밑변의 길이 입력 : "));
var height = parseFloat(prompt("높이 입력 : "));

var area = base * height * 0.5;

document.write("삼각형의 넓이 : " + area);

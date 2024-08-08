// TypeScript Practice File
// https://www.learn-ts.org/en/Introduction

//
// Run the file using ts-node typeScript1.ts in the terminal
//

// One big difference is the need to declare what data type a variable is such as string, number, etc
// let name: string = "John";

// number: For numeric values.
// string: For textual data.
// boolean: For true/false values.
// any: A wildcard type that can be anything.
// arrays: For collections of values, denoted by Type[] or Array<Type>.

// A variable can also hold a specific range of types 
// let numberOrNull: number | null;

// TypeScript is statically typed. This means that the type of a variable is known at compile time. 
// This is different from JavaScript, where types are understood dynamically at runtime.

// // Types of number types
// let decimal: number = 6;
// let hex: number = 0xf00d;
// let binary: number = 0b1010;
// let octal: number = 0o744;


// Any: It can be any type of value. It is useful when you don't want to write a specific type, but its use should be 
// limited to when you really don't know what type there will be.
// let notSure: any = 4;
// notSure = "maybe a string instead";
// notSure = false;

// // Functions in TypeScript
const addition = (a: number, b: number): number => {
    return a + b;
}
console.log(addition(2, 2))
// or 
// const newnum = (a: number, b: number): number => a + b;
// newnum(2,2)

// Arrays can be defined in TypeScript using either the array type syntax or the generic array type:

let names: string[] = ["Alice", "Bob", "Charlie"];
let ids: Array<number> = [101, 102, 103];

console.log(names);
// Arrays offer several methods to add or remove items:

// push(): Adds one or more elements to the end of an array.
// unshift(): Inserts one or more elements at the beginning.
// pop(): Removes the last element.
// shift(): Removes the first element.

// names.push("Angel");
// console.log(names);

// In TypeScript, interfaces play a pivotal role in defining the shape or structure that objects should adhere to. They don't get compiled into
// JavaScript and exist only for static type checking. When you define an object based on an interface, the object must fulfill the shape required by that interface.

interface Dog {
    name: string;
    age: number;
}

// An interface may also have optional fields, denoted using the ? operator, as follows:
interface Dog {
    name: string;
    age: number;
    vaccinated?: boolean;
}



// Modules in TypeScript allow you to organize and split your code across multiple files. You can use the export keyword to expose parts of your module to other modules.
// in math.ts
export function add(x: number, y: number): number {
    return x + y;
}
// in main.ts
// import {add} from './math';


// You can also export a default export, if you have a main variable you want to export from a module. This is useful for modules which export a single class or function. 
// For example:
// in Component.ts
export default function Component(): string {
    return "hello!";
}
// To use the default export, use the following notation (without the curly braces):
// in main.ts
// import Component from './Component';


// Sometimes you might know a more specific type than TypeScript can infer. In these cases, you can use type assertions to specify the type you're confident about.

let someValue: any = "This is a string";
let strLength: number = (<string>someValue).length;
// Or using as-syntax
let strLengthAs: number = (someValue as string).length;

type aStringOrNumber = string | number;
let aStringOrNumber = 20
console.log(aStringOrNumber)

// // Intersection types allow you to combine multiple types into one, enabling objects to have properties of all intersected types.
type Name = { name: string };
type Age = { age: number };
type schoolYear = {schoolYear: string}
type Person1 = Name & Age | schoolYear;
let Person1 = {"Angel": "20" };
console.log(Person1);

// // Tutorial Type
// type Car = { type: "car", doors: number };
// type Bike = { type: "bike", hasBell: boolean };

// type Vehicle = Car | Bike;

// function identifyVehicle(vehicle: Vehicle): string {
//     let Vehicle;
//     if (Vehicle == "Car") {
//         return "Car"
//     } else {
//         return "Bike"
//     }
// }
// console.log(identifyVehicle({ type: "bike", hasBell: true }));


// Conditional types help in expressing types in relation to other types, particularly in generic types. 
// It has the syntax T extends U ? X : Y.
type TypeName<T> = 
    T extends string ? "string" :
    T extends number ? "number" :
    T extends boolean ? "boolean" :
    "object";

// 
type IsString<T> = T extends string ? "Yes" : "No";


// Enums are a way of giving friendly names to sets of numeric values. They can make code more readable and less error-prone.
enum Color {Red, Green, Blue}
// By default, Red is 0, Green is 1, and so on. You can also manually set values.
// enum Color {Red = 1, Green = 2, Blue = 4}
let c: Color = Color.Red;
console.log(c);


// enum Days{Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday}
// function classifyDay(day: Days): string  {
//     if (day < 5) {
//         return "Weekday" 
//     } else {
//         return "Weekend";
//     };
// };
// console.log(classifyDay(Days.Monday));
// console.log(classifyDay(Days.Saturday));

// Generics provide a way to make components work over a variety of types rather than a single one.
function echo<T>(arg: T): T {
    return arg;
}
let input = "string"
console.log(echo(input))
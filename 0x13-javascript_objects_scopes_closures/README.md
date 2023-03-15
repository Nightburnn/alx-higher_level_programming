<img src="https://www.freecodecamp.org/news/content/images/2019/07/arrays-are-objects.jpg">

## JavaScript Objects, Scopes, and Closures

### Objects
In JavaScript, an object is a collection of properties. Properties can be added, modified, or deleted from an object. There are several ways to create objects in JavaScript, including:
* Object literals

* Constructor functions

* ES6 classes
Object literals are the most common way to create objects in JavaScript. Here's an example:
```javascript
const person = {
  firstName: 'John',
  lastName: 'Doe',
  age: 30,
  address: {
    street: '123 Main St',
    city: 'Anytown',
    state: 'CA',
    zip: '12345'
  }
};
```
### Scopes
In JavaScript, scopes define where variables and functions are accessible. There are two main types of scopes in JavaScript:
* Global scope

* Local scope

Variables and functions declared outside of a function are in the global scope and can be accessed from anywhere in the code. Variables and functions declared inside a function are in the local scope and can only be accessed within that function.

```javascript
const globalVariable = 'I am in the global scope';

function myFunction() {
  const localVariable = 'I am in the local scope';

  console.log(globalVariable); // 'I am in the global scope'
  console.log(localVariable); // 'I am in the local scope'
}

myFunction();
console.log(globalVariable); // 'I am in the global scope'
console.log(localVariable); // Uncaught ReferenceError: localVariable is not defined
```
### Closures
A closure is a function that has access to variables in its outer scope, even after the outer function has returned. Closures are created when a function is returned from another function, and the returned function still has access to the variables in the outer function's scope.

```javascript
function outerFunction() {
  const outerVariable = 'I am in the outer function';

  function innerFunction() {
    console.log(outerVariable);
  }

  return innerFunction;
}

const innerFunc = outerFunction();
innerFunc(); // 'I am in the outer function'
```

In the above example, innerFunction is returned from outerFunction and assigned to innerFunc. When innerFunc is called, it still has access to outerVariable, even though outerFunction has already returned.

#### Conclusion
Understanding JavaScript objects, scopes, and closures is essential for writing efficient and effective JavaScript code.

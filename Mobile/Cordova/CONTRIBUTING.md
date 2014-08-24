#Language rule


* Always use semicolons.

```javascript
//NO
MyClass.prototype.myMethod = function() {
  return 42;
} //semicolon missing here

//YES
MyClass.prototype.myMethod = function() {
  return 42;
};

//NO
function foo() {

};
```

* Prefer the use of `===` over `==`

* Prefer the use of `!==` over `!=`

* Always declare variable with the keyword `var`

* Always use exceptions where needed and do not exit function without proper control of the workflow

* Avoid using the delete keyword and prefer assigning `null` to the variable, unless removing the variable from and object's iterated list of keys is needed

* Do not use `for ... in` loops to iterate over an Array, only use for iterating over keys in an object/map/hash

* Use string concatenation instead of escaping the end of the line for multi-line string literals

* Always use the keyword `this` when accessing an object's properties within its scope

#Style rules

##Naming

* Names should be short and explicit.

* Never use `$` or `\` in names

* Name should only be composed of letters and `_`

* Do not use `_` as the first or last character of a name.

* Always use `snake_case` for variable names

* Always use `camelCase` for function names

* Always use `UpperCamelCase` for object names

* Global varaibles should be in all caps

* Optional function arguments start with `opt_`

* Parenthesis and braces

* Always use parenthesis around `return` statements.

* Always add a whitespace before the parenthesis after a keyword

* Opening curly brace should be on the same line as the statement

```javascript
//NO
while (True)
{
 ..
}

//YES
while (True) {
  ...
  }
```

##Whitespaces

* Do not mix tabs and spaces for indenting

* Do not use tabs for indenting

* The indentation unit is 4 spaces

* Remove trailing whitespaces

## Comments

* Comment blocks should look like

```javascript
/*
** This is a comment
** that goes on
** several lines
*/
```

* Inline comments must be before the line it is commenting and should look like

```javascript
//YES
//this is a comment about the if statement
if (foo == 'bar') {
 ...
}

//NO
if (food == 'bar') {  //this is a comment about the if statement
 ...
}
```

* Always comment functions and code snippets

* Avoid adding unecessary comments

```javascript
//NO
//set i to 0
var i = 0;
```

* Lines should be 80 col long at most


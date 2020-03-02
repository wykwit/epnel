# epnel
A simple lispy programming language without parentheses.

## description
### operators
Each operator takes two arguments (numbers) and works the way you'd expect.
 - `+` - addition
 - `-` - subtraction
 - `*` - multiplication
 - `/` - division
 - `<` - comparison (lower than)
 - `>` - comparison (bigger than)
 - `|` - alternation (or)
 - `^` - disjunction (xor)
 - `&` - conjunction (and)
 - `=` - equation (is equal to?)
 - `.` - assignment operator

> Comparison operators return boolean types.

> Logical operators work either on number's bits or booleans.

> The assignment binds a value to a name and returns a value of the second argument. This means you can also rebind the value of numbers.

### conditionals
Conditional takes three arguments: (test, then, else).
If "test" evaluates to True, then the "then" branch is executed. Otherwise the "else" branch is executed.
 - `?` - conditional

### booleans
You can produce booleans using comparison operators. True is equal to 1 and False is equal to 0.
The boolean primitive evaluates to False.
 - `!` - boolean (false)

### numbers
Decimal numbers are composed of digits or passed around as variables.
The variable name can be anything which is not an operator.
The default value for any variable is zero: 0 or False.
You can use the assignment operator to bind names with values.

## inspiration
[Polish Notation](https://pl.wikipedia.org/wiki/Notacja_polska) was the inspiration to write this language, therefore I name the language "epnel".
```
E - Educational
P - Polish
N - Notation
E - Evaluation
L - Language
```

## wishlist
A few things that might be nice to have:
 - functions
 - loops
 - compiler to C


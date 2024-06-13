Sure! Here is a step-by-step algorithm for the script you provided:

### Algorithm for a Simple Calculator Script

1. **Define Functions:**
   - Create a function `addition(x, y)` that returns the sum of `x` and `y`.
   - Create a function `subtract(x, y)` that returns the difference between `x` and `y`.
   - Create a function `multiply(x, y)` that returns the product of `x` and `y`.
   - Create a function `divide(x, y)` that:
     - Checks if `y` is zero. If it is, return an error message "Error! Division by Zero".
     - Otherwise, returns the quotient of `x` divided by `y`.

2. **Display Menu:**
   - Print a message asking the user to enter a number for the desired operation.
   - Print the following options:
     1. Add
     2. Subtract
     3. Multiply
     4. Divide

3. **Get User Input:**
   - Prompt the user to enter their choice (1, 2, 3, or 4).
   - Convert the user input to an integer.
   - Prompt the user to enter the first number and store it in `num1`.
   - Prompt the user to enter the second number and store it in `num2`.

4. **Perform Calculation:**
   - If the user's choice is `1`, call the `addition` function with `num1` and `num2` and print the result.
   - If the user's choice is `2`, call the `subtract` function with `num1` and `num2` and print the result.
   - If the user's choice is `3`, call the `multiply` function with `num1` and `num2` and print the result.
   - If the user's choice is `4`, call the `divide` function with `num1` and `num2` and print the result.
   - If the user's choice is not `1`, `2`, `3`, or `4`, print an error message indicating an invalid choice.

5. **End:**

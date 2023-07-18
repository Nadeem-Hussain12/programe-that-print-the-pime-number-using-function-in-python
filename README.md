# programe-that-print-the-pime-number-using-function-in-python
The is_prime(n) function checks whether a number n is prime or not. It first checks if n is less than 2 because prime numbers are defined as numbers greater than 1. If n is less than 2, the function immediately returns False.

The function uses a for loop to iterate through the numbers from 2 to the square root of n (inclusive). It checks if n is divisible evenly by any number within this range. The range is defined as range(2, int(n**0.5) + 1). The int(n**0.5) expression calculates the square root of n and +1 is added to include the upper bound in the range.

Inside the loop, the code checks if n is divisible by the current number i using the modulo operator %. If n is divisible by i, it means that n is not a prime number and the function immediately returns False.

If the loop completes without finding any factors of n, it means that n is a prime number. In that case, the function returns True.

The main part of the program uses a for loop to iterate through the numbers from 1 to 19 (inclusive) using range(1, 20).

For each number in the range, the program calls the is_prime() function to check if the number is prime. If the number is prime, it is printed using the print() function.

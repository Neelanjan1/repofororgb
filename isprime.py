def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        # Check for factors from 3 to the square root of n, skipping even numbers
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

# Example usage:
number = 17

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


#If a number 'n' has a factor 'a' that is greater than its square root,
#then the other factor 'b' (where n = a * b) must be less than or equal to the square root of 'n'.
#For example, to check if 29 is prime, calculate its square root, which is approximately 5.39.
#You only need to check for factors up to 5. Since 29 is not divisible by 2, 3, 4, or 5, it is a prime number.


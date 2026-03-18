num = int(input("Enter a number: "))

# Find number of digits
num_digits = len(str(num))

# Initialize sum
sum_of_powers = 0

# Temporary variable
temp = num

# Calculate sum of digits raised to power
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10

# Check Armstrong condition
if num == sum_of_powers:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

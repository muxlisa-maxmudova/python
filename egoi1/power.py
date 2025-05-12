import math

# Function to check if a number is a power of 2 and return the exponent d
def is_power_of_two(x):
    if x <= 0:
        return -1  # not a power of 2
    return math.log2(x) if x == int(x) else -1  # Check if it's an integer power of 2

# Main logic
def max_power_of_pair(a):
    n = len(a)
    max_power = -1  # Start with -1, because if no power is found, return -1
    for i in range(n):
        for j in range(n):
            if i != j:  # Skip if i == j (no self-pairing)
                ratio = a[j] / a[i]
                power = is_power_of_two(ratio)
                max_power = max(max_power, power)  # Update the maximum power if a higher one is found
    return max_power

# Example usage
a = [2, 4, 8, 16]
print(max_power_of_pair(a))  # Output: 3




















main()




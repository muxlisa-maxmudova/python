def main():
    n = int(input())  # Read the size of the array
    numbers = list(map(int, input().split()))  # Read the array elements as integers

    count = 0  # Moves counter
    for i in range(1, n):  # Start from the second element
        if numbers[i] < numbers[i - 1]:  # If the current number is smaller than the previous
            count += (numbers[i - 1] - numbers[i])  # Increase it to match the previous
            numbers[i] = numbers[i - 1]  # Modify the number in-place

    print(count)  # Output the total moves

main()

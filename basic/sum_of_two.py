
#take two number from user
# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")


# num1 = float(num1)
# num2 = float(num2)

# Perform addition
# sum_result = num1 + num2

# Display the result
# print(f"The sum of {num1} and {num2} is {sum_result}")

# Enhance Programe 

print("Welcome to Sum of Numbers")

# Take the first two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Initialize the sum with the first two numbers
sum_result = num1 + num2

# Ask if the user wants to add more numbers
while True:
    flag = input("Do you want to add more numbers? (y/n): ").strip().lower()
    
    if flag == 'y':
        # Take additional numbers as input
        num = float(input("Enter the number: "))
        sum_result += num
    elif flag == 'n':
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# Print the total sum
print("Total sum:", sum_result)

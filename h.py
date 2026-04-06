# Ask the user for a number
num = int(input("Enter a number to see its multiplication table: "))

# Print multiplication table for the entered number
print(f"\nMultiplication Table for {num}:\n")

for i in range(1, 11):  # 1 to 10
    print(f"{num} x {i} = {num * i}")
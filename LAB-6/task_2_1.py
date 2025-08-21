def print_multiples_for(n):
    print(f"First 10 multiples of {n} using a for loop:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Example usage
number = int(input("Enter a number: "))
print_multiples_for(number)
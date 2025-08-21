def print_multiples_while(n):
    print(f"First 10 multiples of {n} using a while loop:")
    i = 1
    while i <= 10:
        print(f"{n} x {i} = {n * i}")
        i += 1

# Example usage
number = int(input("Enter a number: "))
print_multiples_while(number)
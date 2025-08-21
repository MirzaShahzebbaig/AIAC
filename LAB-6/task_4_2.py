def sum_to_n_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Sum of first {n} natural numbers is: {sum_to_n_while(n)}")
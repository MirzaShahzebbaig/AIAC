def sum_to_n_recursive(n):
    if n <= 0:
        return 0
    else:
        return n + sum_to_n_recursive(n - 1)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Sum of first {n} natural numbers is: {sum_to_n_recursive(n)}")
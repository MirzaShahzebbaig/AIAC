def sum_to_n_for(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Sum of first {n} natural numbers is: {sum_to_n_for(n)}")
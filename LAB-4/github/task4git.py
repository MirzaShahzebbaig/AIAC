def count_vowels():
    s = input("Enter a string : ")
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    print("Count of vowels :", count)

# Example usage
if __name__ == "__main__":
    count_vowels()
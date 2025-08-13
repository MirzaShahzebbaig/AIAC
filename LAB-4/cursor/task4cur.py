def count_vowels_in_string():
    input_str = input("Enter a string : ")
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in input_str if char in vowels)
    print(f"Count of vowels : {count}")

# Example usage:
if __name__ == "__main__":
    count_vowels_in_string()

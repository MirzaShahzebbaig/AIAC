def format_full_name():
    full_name = input("Enter the Full Name : ").strip()
    # Split the name into parts
    name_parts = full_name.split()
    if len(name_parts) >= 2:
        first_name = name_parts[0]
        last_name = name_parts[-1]
        print(f"First Name : {first_name}")
        print(f"Last Name : {last_name}")
    else:
        print("Please enter both first and last name.")

# Example usage:
if __name__ == "__main__":
    format_full_name()

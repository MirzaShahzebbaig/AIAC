def count_lines_in_file():
    file_path = input("Enter the path to the .txt file: ")
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines in the file: {len(lines)}")
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# count_lines_in_file()
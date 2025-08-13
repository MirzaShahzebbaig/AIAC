def count_lines_in_file():
    file_path = input("Enter the path to your .txt file: ")
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            print(f"The file '{file_path}' contains {line_count} lines.")
    except FileNotFoundError:
        print("Error: File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

import base64

def collect_user_data():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    return name, age, email

def encrypt_email(email):
    # Simple base64 encoding for demonstration
    encoded_bytes = base64.b64encode(email.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def save_to_file(filename, name, age, encrypted_email):
    with open(filename, 'w') as f:
        f.write(f"Name: {name}\n")
        f.write(f"Age: {age}\n")
        f.write(f"Encrypted Email: {encrypted_email}\n")

if __name__ == "__main__":
    name, age, email = collect_user_data()
    encrypted_email = encrypt_email(email)
    save_to_file("txt1_2.txt", name, age, encrypted_email)
    print("User data saved to txt1_2.txt")
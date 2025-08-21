# task1_1.py

def collect_user_data():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    data = f"Name: {name}\nAge: {age}\nEmail: {email}\n"

    with open("user_data.txt", "w") as file:
        file.write(data)
    print("User data saved to user_data.txt.")

if __name__ == "__main__":
    collect_user_data()
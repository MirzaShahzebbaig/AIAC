def classify_age(age):
    if age >= 0:
        if age <= 2:
            print("Infant")
        elif age <= 12:
            print("Child")
        elif age <= 19:
            print("Teenager")
        elif age <= 60:
            print("Adult")
        else:
            print("Senior Citizen")
    else:
        print("Invalid age")

if __name__ == "__main__":
    try:
        age = int(input("Enter age: "))
        classify_age(age)
    except ValueError:
        print("Please enter a valid integer for age.")
def classify_age(age):
    if age < 0:
        print("Invalid age")
        return

    match age:
        case age if age <= 2:
            print("Infant")
        case age if age <= 12:
            print("Child")
        case age if age <= 19:
            print("Teenager")
        case age if age <= 60:
            print("Adult")
        case _:
            print("Senior Citizen")

if __name__ == "__main__":
    try:
        age = int(input("Enter age: "))
        classify_age(age)
    except ValueError:
        print("Please enter a valid integer for age.")
def cm_to_inches(cm):
    return cm / 2.54

if __name__ == "__main__":
    try:
        cm_value = float(input("Enter value in centimeters: "))
        inches = cm_to_inches(cm_value)
        print(f"{cm_value} cm is equal to {inches:.2f} inches.")
    except ValueError:
        print("Please enter a valid number.")
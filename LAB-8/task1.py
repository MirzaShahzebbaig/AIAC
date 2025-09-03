def is_valid_email(email):
    # Check for presence of '@' and '.'
    if '@' not in email or '.' not in email:
        return False

    # Must not start or end with special characters
    special_chars = {'@', '.'}
    if email[0] in special_chars or email[-1] in special_chars:
        return False

    # Should not allow multiple '@'
    if email.count('@') != 1:
        return False

    return True

email = input("Enter an email address: ")
print(is_valid_email(email))



import string

def check_password_strength(password):

    score = 0
    feedback = []

    # 1. Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # 2. Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # 3. Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # 4. Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")

    # 5. Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%).")

    # Classify password strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    # Display results
    print("\n----- Password Strength Report -----")
    print("Password Strength:", strength)
    print("Score:", score, "/ 5")

    if feedback:
        print("\nSuggestions to improve your password:")
        for suggestion in feedback:
            print("-", suggestion)
    else:
        print("\nExcellent! Your password meets all five checks.")

# Main program
password = input("Enter your password: ")

check_password_strength(password)

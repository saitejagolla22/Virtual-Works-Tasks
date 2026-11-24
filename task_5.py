
import time
import getpass

# Login credentials (demo purpose)
USERNAME = "admin"
PASSWORD = "Admin@123"

MAX_ATTEMPTS = 3
LOCKOUT_TIME = 30

failed_attempts = 0
lockout_until = 0

def login_system():

    global failed_attempts, lockout_until

    while True:

        # Check account lockout
        current_time = time.time()

        if current_time < lockout_until:
            remaining_time = int(lockout_until - current_time) + 1

            print("\nAccount temporarily locked!")
            print("Try again after", remaining_time, "seconds.")

            time.sleep(min(remaining_time, 5))
            continue

        print("\n===== LOGIN SYSTEM =====")

        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        # Validate credentials
        if username == USERNAME and password == PASSWORD:

            print("\nLogin successful!")
            print("Welcome,", username)

            failed_attempts = 0
            break

        else:

            failed_attempts += 1

            remaining_attempts = MAX_ATTEMPTS - failed_attempts

            print("\nInvalid username or password!")

            if remaining_attempts > 0:

                print("Attempts remaining:", remaining_attempts)

            else:

                print("\nMaximum login attempts exceeded!")
                print("Account locked for", LOCKOUT_TIME, "seconds.")

                lockout_until = time.time() + LOCKOUT_TIME
                failed_attempts = 0


# Main program
login_system()

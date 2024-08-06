import random
import string

def generate_password(length=12):
    # Define character sets for the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Secure Password Generator!")
    print("-----------------------------------------")

    while True:
        try:
            num_passwords = int(input("How many passwords would you like to generate?"))
            password_length = int(input("Enter the length of each password:"))
            
            if num_passwords <= 0 or password_length <= 0:
                print("Please enter valid numbers greater than zero. ")
                continue
            
            print("\nGenerating Passwords...")
            for i in range(num_passwords):
                password = generate_password(password_length)
                print(f"Password {i+1}: {password}")

            # Ask user if they want to generate more passwords or exit
            choice = input("\nDo you want to generate more passwords? (yes/no):").lower()
            if choice != 'yes':
                print("Thank you for using the Secure Password Generator!")
                break

        except ValueError:
            print("Please enter valid integers for number of passwords and password length.")

if __name__ == "__main__":
    main()
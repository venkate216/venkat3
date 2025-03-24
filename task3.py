
import random
import string

def generate_password(length):
    # Define the character sets
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    # Ask the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 8:
                print("Password length should be at least 8 characters for security purposes.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Generate and display the password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()

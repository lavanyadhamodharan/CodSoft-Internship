import random
import string

def main():
    print("--- PASSWORD GENERATOR ---")

    try:
        #Password length
        length = int(input("Enter the desired password length: "))

        if length <= 0:
            print("Password length must be greater than 0.")
            return

        #Complexity options
        print("\nPassword Complexity Levels:")
        print("1. Weak (Letters only)")
        print("2. Medium (Letters and Numbers)")
        print("3. Strong (Letters, Numbers, and Symbols)")

        complexity = input("Choose a complexity level (1-3): ").strip()
        
        if complexity == "1":
            characters = string.ascii_letters

        elif complexity == "2":
            characters = string.ascii_letters + string.digits

        elif complexity == "3":
            characters = (
                string.ascii_letters +
                string.digits +
                string.punctuation
            )

        else:
            print("Invalid complexity level selected.")
            return

        #Generate password
        password = "".join(random.choice(characters) for _ in range(length))

        #Display generated password
        print(f"\nGenerated Password: {password}")

    except ValueError:
        print("Please enter a valid password length.")

if __name__ == "__main__":
    main()

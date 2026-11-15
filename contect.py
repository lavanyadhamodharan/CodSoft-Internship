def main():
    #Store contacts as dictionaries
    contacts = []

    print("--- CONTACT BOOK ---")

    while True:
        print("\nMain Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        #Add Contact
        if choice == "1":
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone Number: ").strip()
            email = input("Enter Email: ").strip()
            address = input("Enter Address: ").strip()

            contacts.append({
                "name": name, "phone": phone, "email": email, "address": address
            })

            print(f"Contact '{name}' added successfully.")

        #View Contacts
        elif choice == "2":
            if not contacts:
                print("\nNo contacts available.")
            else:
                print("\nContact List")
                for index, contact in enumerate(contacts, start=1):
                    print(f"{index}. {contact['name']} - {contact['phone']}")

        #Search Contact
        elif choice == "3":
            if not contacts:
                print("\nNo contacts available.")
                continue

            search = input("Enter Name or Phone Number: ").strip().lower()

            found = False

            for contact in contacts:
                if (search == contact["name"].lower() or
                        search == contact["phone"]):

                    print("\nContact Found")
                    print(f"Name    : {contact['name']}")
                    print(f"Phone   : {contact['phone']}")
                    print(f"Email   : {contact['email']}")
                    print(f"Address : {contact['address']}")
                    found = True

            if not found:
                print("Contact not found.")

        # Update Contact
        elif choice == "4":
            if not contacts:
                print("\nNo contacts available.")
                continue

            name = input("Enter the contact name to update: ").strip().lower()

            found = False

            for contact in contacts:
                if contact["name"].lower() == name:

                    print("\nLeave a field blank to keep the current value.")

                    new_name = input(f"Name ({contact['name']}): ").strip()
                    new_phone = input(f"Phone ({contact['phone']}): ").strip()
                    new_email = input(f"Email ({contact['email']}): ").strip()
                    new_address = input(f"Address ({contact['address']}): ").strip()

                    if new_name:
                        contact["name"] = new_name
                    if new_phone:
                        contact["phone"] = new_phone
                    if new_email:
                        contact["email"] = new_email
                    if new_address:
                        contact["address"] = new_address

                    print("Contact updated successfully.")
                    found = True
                    break

            if not found:
                print("Contact not found.")

        #Delete Contact
        elif choice == "5":
            if not contacts:
                print("\nNo contacts available.")
                continue

            name = input("Enter the contact name to delete: ").strip().lower()

            found = False

            for contact in contacts:
                if contact["name"].lower() == name:
                    contacts.remove(contact)
                    print(f"Contact '{contact['name']}' deleted successfully.")
                    found = True
                    break

            if not found:
                print("Contact not found.")

        #Exit Program
        elif choice == "6":
            print("\nThank you for using Contact Book!")
            break

        #Invalid Menu Choice
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
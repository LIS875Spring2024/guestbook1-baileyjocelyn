guestbook_entries ={}

def write_to_guestbook(name,message):
    global guestbook_entries
    if name not in guestbook_entries:
        guestbook_entries[name] = [message]
    else:
        guestbook_entries[name].append(message)

def view_guestbook():
    if not guestbook_entries:
        print("Guestbook is empty.")
    else:
        print("Guestbook Entries")
        for name, messages in guestbook_entries.items():
            print("Name: {name}")
            print("Messages:")
            for message in messages:
                print(f"- {message}")
            print()

def main():
    print("Welcome to our Guestbook")
    while True:
        print("What would you like to do?")
        print("1: Sign the Guestbook")
        print("2. View the Guestbook")
        print("3. Exit the Guestbook")

        choice =input("Enter your selection")

        if choice =='1':
            name = input("Name:")
            message = input("Message:")
            write_to_guestbook(name,message)
            print("Thank you for signing the Guestbook!")

        elif choice =='2':
            view_guestbook()

        elif choice =='3':
            print("Thank you. Goobye.")
            break
        
    else:
        print("Invalid choice. Please try again")
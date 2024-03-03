import turtle

#Set Scree Size for Turtle
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Guestbook Turtle")

#Using t to sub for typing turtle 
t = turtle.Turtle()
t.speed (1)

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
        t.penup()
        t.goto(-300,200)
        t.pendown()
        t.write("Guestbook Entries", font=("Edwardian Script", 16))
        t.penup()
        t.goto(-300, 180)
        t.pendown()
        for name, messages in guestbook_entries.items():
            t.penup()
            t.goto(-300, t.ycor() - 20)
            t.pendown()
            t.write(f"Name: {name},", font=("Arial", 12))
            for message in messages:
                t.penup()
                t.goto(-280,t.ycor() - 20)
                t.pendown()
                t.write(f" - {message}", font=("Arial", 10))

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
            screen.mainloop()

        elif choice =='3':
            print("Thank you. Goobye.")
            break
        
        else:
            print("Invalid choice. Please try again")

    screen.mainloop()
if __name__ == "__main__":
    main()

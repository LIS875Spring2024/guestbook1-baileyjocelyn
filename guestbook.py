import turtle

#Set Screen and Screen Size for Turtle
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Guestbook")
screen.bgcolor("light blue")

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
    t.clear()
    if not guestbook_entries:
        t.penup()
        t.goto(-200, 0)
        t.pendown()
        t.write("Guestbook is empty.", font=("Arial", 16))
    else:
        t.penup()
        t.goto(-300,200)
        t.pendown()
        t.write("Guestbook", font=("Brush Script MT", 30))
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
    screen.update()

#For the Spade drawing from previous assignment, but had to add t. 
def spade():
    t.fillcolor("black")
    t.setheading(0)
    t.begin_fill()
    t.forward(15)
    t.left(120)
    t.forward(30)
    t.left(120)
    t.forward(30)
    t.left(120)
    t.forward(15)
    t.end_fill()

    t.setheading(90)
    t.forward(25)
    t.left(180)
    t.left(45)
    t.begin_fill()
    t.circle(18,180)
    t.forward(36)
    t.left(90)
    t.forward(36)
    t.circle(18, 180)
    t.end_fill()
    t.left(45)
    t.back(25)
    t.setheading(0)

#Before user enters their choice
def main():
    print("Welcome to our Guestbook")
    t.penup()
    t.goto(-300,220)
    t.pendown()
    spade()
    screen.update()
    t.penup()
    t.goto(-200,200)
    t.write("Guestbook", font=("Brush Script MT", 30))
    t.goto(-300,180)
    screen.update()

#User has to enter their selection. Had use lots for forums, Reddit, etc. to figure our that I needed to do turtle.textinput to get a prompt for the users. This took the majority of our time.
    while True:
        try:
            choice = turtle.textinput("Guestbook", "What would you like to do?\n1: Sign the Guestbook\n2: View the Guestbook\n3: Exit")

            if choice =='1':
                name = turtle.textinput("Guestbook Entry", "Name:")
                message = turtle.textinput("Guestbook Entry", "Message:")
                write_to_guestbook(name, message)
                print("Thank you for signing the Guestbook!", flush=True)
                screen.update()

            elif choice =='2':
                view_guestbook()
                screen.update()

            elif choice =='3':
                print("Thank you. Goobye.", flush=True)
                break
        
            else:
                print("Invalid choice. Please try again", flush=True)

#Had to add this is because I couldnt figure out why Python application was "not responding" at first.     
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    
    turtle.mainloop()

if __name__ == "__main__":
    main()
from turtle import Turtle, Screen


def setup():
    turtle.goto(0, 200)
    turtle.write("Shift Cipher", align="center", font=("courier", 60, "normal"))
    shift_direction = screen.textinput(title="Shift Direction",
                                       prompt="Type 'encode' to encrypt, type 'decode' to decrypt")
    turtle.goto(-300, 150)
    return shift_direction


def load_gui():
    turtle.goto(0, 50)
    turtle.showturtle()
    for _ in range(3):
        turtle.speed(1)
        turtle.circle(17)


def data():
    text_input = screen.textinput(title="Message", prompt="Type your message")
    shift_num = int(screen.textinput(title="Shift Number", prompt="Type the shift number:"))
    shift_num = shift_num % 26
    turtle.goto(-300, 120)
    return text_input, shift_num


def cipher(plain_text, shift_amount, directional_encryption):
    turtle.hideturtle()
    end_letter = ""
    for every_letter in plain_text:
        if every_letter in alphabet:
            initial_position = alphabet.index(every_letter)
            if directional_encryption == "encode":
                new_position = initial_position + shift_amount
            else:
                new_position = initial_position - shift_amount
            new_letter = alphabet[new_position]
            end_letter += new_letter
        else:
            end_letter += every_letter
    turtle.goto(-300, 95)
    turtle.write(f"The new word is: ", align="left", font=("courier", 15, "normal"))
    turtle.goto(-300, 70)
    turtle.write(f"{end_letter}", align="left", font=("courier", 15, "normal"))
    print(end_letter)
    ask_again = screen.textinput(title="Continue....",
                                 prompt="Do you want to continue? (Type 'yes' to continue, type 'no' to end program)")
    if ask_again == "no":
        quit()
    else:
        print("")
        turtle.clear()


turtle = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=900, height=700)
turtle.hideturtle()
turtle.color("white")
turtle.penup()
turtle.shape("turtle")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'
            , 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:

    direction = setup()

    if direction == "encode":

        turtle.write("Encoding your message", align="left", font=("courier", 15, "normal"))
        text, shift = data()
        turtle.write("Please wait while the turtle is encoding the message", align="left",
                     font=("courier", 15, "normal"))
        load_gui()
        cipher(plain_text=text, directional_encryption=direction, shift_amount=shift)

    elif direction == "decode":
        turtle.write("Decoding your message", align="left", font=("courier", 15, "normal"))
        text, shift = data()
        turtle.write("Please wait while the turtle is decoding the message", align="left",
                     font=("courier", 15, "normal"))
        load_gui()
        cipher(plain_text=text, directional_encryption=direction, shift_amount=shift)

screen.exitonclick()

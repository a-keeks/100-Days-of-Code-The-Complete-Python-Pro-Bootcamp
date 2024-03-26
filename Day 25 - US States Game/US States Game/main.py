import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
screen.setup(width = 750,height = 520, startx = None, starty = 90)

states_info = pandas.read_csv("50_states.csv")
all_states = states_info.state.to_list()
states_dict = dict(zip(states_info['state'], list(zip(states_info.x, states_info.y))))

correct_states = 0
states_named = []

game_is_on = True

if game_is_on:
    guess = screen.textinput("Guess The State", "Name a state: ").title()

    for _ in range(len(all_states)):
        if guess in all_states:
            cordinate = states_dict[guess]
            turtle.penup()
            turtle.speed(7)
            turtle.goto(cordinate)
            turtle.ht()
            turtle.write(guess, align = "center", font = ("Calibri", 8))

            if guess == "New Hampshire":
                turtle.pendown()
                turtle.goto(302,133)
                turtle.dot(5, "black")    

            if guess == "Vermont":
                turtle.pendown()
                turtle.goto(287,135)
                turtle.dot(5, "black")

            if guess == "Connecticut":
                turtle.pendown()
                turtle.goto(298,97)
                turtle.dot(5, "black")

            if guess == "Massachusetts":
                turtle.pendown()
                turtle.goto(303,111)
                turtle.dot(5, "black")
                
            if guess == "Rhode Island":
                turtle.pendown()
                turtle.goto(311,100)
                turtle.dot(3, "black")

            if guess == "New Jersey":
                turtle.teleport(295,73)
                turtle.pendown()
                turtle.goto(282,65)
                turtle.dot(4, "black")

            if guess == "Delaware":
                turtle.teleport(300,22)
                turtle.pendown()
                turtle.goto(276,41)
                turtle.dot(4, "black")

            if guess == "Maryland":
                turtle.teleport(316,-22)
                turtle.pendown()
                turtle.goto(254,47)
                turtle.dot(5, "black")


            correct_states  += 1
            states_named.append(guess)
            guess = screen.textinput(f"{correct_states} / {len(all_states)} Named" , "Name another state: ").title()
        
        if guess == "Exit":
            game_is_on = False
            turtle.bye()

        # States to Learn
            missing_states_list = [states for states in all_states if states not in states_named]
                    
            missing_states = pandas.DataFrame()
            missing_states["states"] = missing_states_list
            missing_states.to_csv("States_to_Learn.csv")

            break
        
        if guess not in all_states:
            guess = screen.textinput(f"{correct_states} / {len(all_states)} Named" , "Guess Again: ").title()



turtle.exitonclick()


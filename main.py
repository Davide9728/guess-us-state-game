from turtle import Turtle, Screen
import pandas
import time

#game screen
screen = Screen()
tim = Turtle()
screen.title('U.S States Game')
#screen.tracer(0)
image = 'blank_states_img.gif'
screen.addshape(image)
tim.shape(image)

data = pandas.read_csv("50_states.csv") #read state's data form 50_states
screen.update()

#scoreboard
score = 0
scoreboar = Turtle()
scoreboar.hideturtle()
scoreboar.penup()
scoreboar.goto(0, 280)
scoreboar.write(f"score {score}", False, 'center', ('Arial', 24, 'normal'))
correct_gessues = []#recor the correct guesses

#start game


while len(correct_gessues) < 50:
    answer_state = screen.textinput(title='Guess the state', prompt="what's another state", )
    if answer_state == 'exit': #print all' missed state
        missed_state = [state for state in data.state if state not in correct_gessues]
        #create a new dataframe to save missed state in csv file
        missed_data = pandas.DataFrame(missed_state) #new data frame
        missed_data.to_csv('missed_satate.csv') #new file
        break #end game
    if len(data[data['state'] == answer_state]) == 1 and answer_state not in correct_gessues:

        #update scoreboard
        score += 1
        scoreboar.clear()
        scoreboar.write(f"score {score}", False, 'center', ('Arial', 24, 'normal'))

        correct_gessues.append(answer_state)

        # convert  guess to title case
        title = Turtle()
        title.penup()
        title.hideturtle()

        state_data = data[data.state == answer_state]
        title.goto(int(state_data.x), int(state_data.y))
        title.write(answer_state)



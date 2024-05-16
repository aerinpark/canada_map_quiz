import turtle
import pandas
import random

TITLE = "Canadian Map Quiz"
IMAGE_PATH = "canadian_map.gif"
MAPPING_DATA_PATH = "mapping_data.csv"
ALIGNMENT = "center"
END_FONT = ('Courier New', 30, "bold")
LARGE_FONT = ('Courier New', 12, "bold")
SMALL_FONT = ('Courier New', 7, "bold")
COUNT = 13

screen = turtle.Screen()
screen.setup(width=1100, height=850)
screen.title(TITLE)

# Upload the map onto the screen
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)
mapping_data = pandas.read_csv(MAPPING_DATA_PATH)
capitals = mapping_data.capital.to_list()
provinces = mapping_data.province.to_list()

label = turtle.Turtle()
label.penup()
label.hideturtle()

correct_guesses = []

correct_answer = 0

while correct_answer < COUNT:
    answer = (turtle.textinput(title=f"{correct_answer}/{COUNT} correct", prompt="Type a name of province/territory")).title()
    if answer not in correct_guesses and answer in provinces:
        x = mapping_data.loc[mapping_data.province==answer, 'province_x'].item()
        y = mapping_data.loc[mapping_data.province==answer, 'province_y'].item()
        if answer == "Newfoundland":
            answer = "Newfoundland and Labrador"
        elif answer == "Prince Edward Island":
            answer = "P.E.I"
        answer = answer.split()
        correct_answer += 1
        for word in answer:
            label.goto(x,y)
            label.write(f"{word}", True, align=ALIGNMENT, font=LARGE_FONT)
            print(word)
            y -= 15

# capital cities
correct_answer = 0

random.shuffle(capitals)

for city in capitals:
    x = mapping_data.loc[mapping_data.capital==city, 'capital_x'].item()
    y = mapping_data.loc[mapping_data.capital==city, 'capital_y'].item()
    capital_city = turtle.Turtle()
    capital_city.hideturtle()
    capital_city.color("red")
    capital_city.shape("circle")
    capital_city.shapesize(0.2)
    capital_city.penup()
    capital_city.goto(x, y)
    capital_city.showturtle()
    
    answer = ""
    while answer != city:
        answer = (turtle.textinput(title=f"{correct_answer}/{COUNT} correct", prompt="Type the name of the marked capital city")).lower()
        print(city)
        print(answer)
        if answer == city.lower() or answer == "skip":
            if answer == city.lower():
                correct_answer += 1
            label.goto(x, y-15)
            label.write(f"{city}", True, align=ALIGNMENT, font=SMALL_FONT)
            break    
        elif answer == "exit":
            break
    if answer == "exit":
        break

label.goto(0,0)
if correct_answer == COUNT:
    label.write("GREAT WORK! YOU'VE COMPLETED THE MAP!", True, align=ALIGNMENT, font=END_FONT)
else:
    label.write("BOOO! PRACTICE MORE AND COME BACK! ", True, align=ALIGNMENT, font=END_FONT)
screen.exitonclick()

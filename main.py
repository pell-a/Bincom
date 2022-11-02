import random
from random import randint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///colors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def shirts():
    colors = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE',
               'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN', 'ASH', 'BROWN', 'GREEN', 'BROWN',
               'BLUE', 'BLUE', 'BLUE', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE',
               'BLUE', 'BLUE', 'BLUE', 'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE',
               'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE',
               'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE',
               'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN', 'GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK',
               'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']

    green = colors.count('GREEN')
    yellow = colors.count('YELLOW')
    brown = colors.count('BROWN')
    blue = colors.count('BLUE')
    pink = colors.count('PINK')
    orange = colors.count('ORANGE')
    red = colors.count('RED')
    white = colors.count('WHITE')
    ash = colors.count('ASH')
    cream = colors.count('CREAM')

    frequency = [green, yellow, brown, blue, pink, orange, red, white, ash, cream]

    #mean
    mean = (sum(frequency))/10
    print(mean)

    #colour of shirt worn the most
    highest = 0
    for color in frequency:
        if color > highest:
            highest = color
    most_worn = highest
    print(most_worn)


    #median colour
    middle = int(sum(frequency)/2)
    median = colors[middle+1]
    print(median)


    #variance
    sum_and_square = 0
    for color in frequency:
        sum_and_square += (color-mean)**2
    variance = sum_and_square/10
    print(variance)


    #probability a color is red
    probability = red/sum(frequency)
    print(probability)

    #save in database
    app = Flask(__name__)
    app.app_context().push()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///colors.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    class Colors(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        color = db.Column(db.String(200), nullable=False)
        frequency = db.Column(db.Integer)

    db.create_all()

    colour = Colors(color='Green', frequency=green)
    db.session.add(colour)
    db.session.commit()
    colour = Colors(color='Yellow', frequency=yellow)
    db.session.add(colour)
    db.session.commit()
    colour = Colors(color='Brown', frequency=brown)
    db.session.add(colour)
    db.session.commit()
    colour = Colors(color='Blue', frequency=blue)
    db.session.add(colour)
    db.session.commit()
    colour = Colors(color='Pink', frequency=pink)
    db.session.add(colour)
    db.session.commit()
    colour = Colors(color='Orange', frequency=orange)
    db.session.add(colour)
    db.session.commit()
    colour = Colors(color='Red', frequency=red)
    db.session.add(colour)
    db.session.commit()
    colour = Colors(color='White', frequency=white)
    db.session.add(colour)
    db.session.commit()
    colour = Colors(color='Ash', frequency=ash)
    db.session.add(colour)
    db.session.commit()
    colour = Colors(color='Cream', frequency=cream)
    db.session.add(colour)
    db.session.commit()


def convert_to_base_10():
    number = ""
    for i in range(4):
        num = str(randint(0, 1))
        number+=num
    my_list = list(map(int, number))
    converted = 0
    length = len(my_list)
    for digit in my_list:
        converted += digit * (2**(length-1))
        length-=1
    return f"Base 2: {number}\nBase 10: {converted}"


def search_for_number():
    number_list = []
    for i in range(1, 101):
        number_list.append(i)
    user_input = int(input("Enter a number from 1-100: "))
    if user_input in number_list:
        return True
    else:
        return False


def fibonacci():
    count = 0
    num1 = 0
    num2 = 1
    sum = 0
    while count <= 50:
        term = num1 + num2
        num1 = num2
        num2 = term
        sum+=num1
        count += 1
    return sum

shirts()
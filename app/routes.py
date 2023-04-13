from app import app
from flask import render_template



#  specify routes:

@app.route('/')
def myDecks():
    """displays/returns list of decks upon signing in"""


    return render_template('mydecks.html')
    # when adding keys and values to the return, you will be using that key to access values in html
    # to access, use {{ ____ }} in html file. to create for loops, use {% ____ %} in html file
    
@app.route('/flashcard')
def flashCard():
    """returns empty flash card?"""
    return render_template('flashcard.html')


@app.route('/practice')
def practice():
    """returns completed flash card"""
    return render_template('practice.html')


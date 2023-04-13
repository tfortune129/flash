from app import app
from flask import render_template



#  specify routes:

@app.route('/mydecks')
def myDecks():
    """displays/returns list of decks upon signing in"""
    return render_template('mydecks.html')
    
    
# @app.route('/flashcard')
# def flashCard():
#     """returns empty flash card?"""
#     return 


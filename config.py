# avoid having to close and repopen server connection
import os 
# os = operating system


basedir = os.path.abspath(os.path.dirname(__name__))

class Config():
    # how do you get to your application:
    FLASK_APP = os.environ.get('FLASK_APP')
    # what is the environment you're workign with:
    FLASK_ENV = os.environ.get('FLASK_ENV')


    # this is always the same accross applications
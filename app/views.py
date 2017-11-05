from flask import * #TODO: actually look at imports

views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    return render_template('homepage.html')

@views.route('/about')
def about():
    return render_template('about.html')




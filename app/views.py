from flask import * #TODO: actually look at imports

views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    if request.method == "POST":
        return render_template('homepage.html', WordCount = "We Win!!")
    else:
        return render_template('homepage.html', WordCount = "Did we win yet?")

@views.route('/about')
def about():
    return render_template('about.html')




from flask import * #TODO: actually look at imports
import imagen-ocr

views = Blueprint('views', __name__)

extensions = set(['jpg'])

def file_allowed(file):
    return '.' in file and \
           file.rsplit('.', 1)[1] in extensions

@views.route('/', methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        if not request.form.get("input-b1"):
            return render_template('homepage.html', WordCount = "No File Found")
        return render_template('homepage.html', WordCount = imagen-ocr.ocr_space_url(url='http://i.imgur.com/31d5L5y.jpg'))
        #return render_template('homepage.html', WordCount = "We Win!!")
    else:
        return render_template('homepage.html', WordCount = "")

@views.route('/about')
def about():
    return render_template('about.html')




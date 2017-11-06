from flask import * #TODO: actually look at imports

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
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['input-b1']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            return render_template('homepage.html', WordCount = "File Received!")
        return render_template('homepage.html', WordCount = "We Win!!")
    else:
        return render_template('homepage.html', WordCount = "Did we win yet?")

@views.route('/about')
def about():
    return render_template('about.html')




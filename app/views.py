from flask import * #TODO: actually look at imports

views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    return render_template('homepage.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/factorial')
def factorial():
    return render_template('factorial.html')

@views.route('/lesson1')
def lesson1():
	return render_template('lesson1.html')

@views.route('/sorting')
def sorting():
	return render_template('sorting.html')

@views.route('/selectionsort')
def selectionsort():
	return render_template('selectionsort.html')

@views.route('/bubblesort')
def bubblesort():
	return render_template('bubblesort.html')

@views.route('/datastructures')
def datastructures():
	return render_template('datastructures.html')

@views.route('/bstconstruction')
def bstconstruction():
	return render_template('bst.html')

@views.route('/bstsearch')
def bstsearch():
	return render_template('bstsearch.html')

@views.route('/binarysearch')
def binarysearch():
	return render_template('binarysearch.html')

@views.route('/yay')
def yay():
	return render_template('yay.html')

@views.route('/classes')
def classes():
	return render_template('classes.html')


@views.route('/recurse')
def recurse():
	return render_template('recursion.html')



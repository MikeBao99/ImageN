from flask import * #TODO: actually look at imports

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')




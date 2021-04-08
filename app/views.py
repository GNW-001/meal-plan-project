"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash

from app.models import User, Recipe
from app.forms import ProfileForm, RecipeForm, LoginForm
from app.models import User, Recipe

###
# Routing for your application.
###


@app.route('/')
def home():
    """Render website's home page."""
    if not session.get('logged_in'):
        return redirect(url_for('welcome'))
    return render_template('home.html', filename="yarg.jpg")


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="COMP3161")

@app.route('/recipe', methods=['POST', 'GET'])
def recipe():
    if not session.get('logged_in'):
        return redirect(url_for('welcome'))
    reciList = Recipe.query.all()
    return render_template('recipe.html', recipes=reciList)


@app.route('/addRecipe', methods=['POST', 'GET'])
def addRecipe():
    form = RecipeForm()
    if not session.get('logged_in'):
        return redirect(url_for('welcome'))
    if request.method == 'POST':
        # Get file data and save to your uploads folder
        if form.validate_on_submit():
            name = form.name.data;
            instruction = form.instruction.data
            numInstruction = form.numInstruction.data
            ingredients = form.ingredients.data
            measurement = form.measurement.data

            recipe = Recipe(name, instruction, ingredients)

            db.session.add(recipe)
            db.session.commit()

            flash('File Saved', 'success')
        return redirect(url_for('home'))
    return render_template('addRecipe.html', form=form)

@app.route('/mealplan', methods=['GET'])
def mealplan():
    if not session.get('logged_in'):
        return redirect(url_for('welcome'))
    return render_template('mealplan.html')

@app.route('/grocery', methods=['GET'])
def grocery():
    if not session.get('logged_in'):
        return redirect(url_for('welcome'))
    return render_template('grocery.html')

@app.route('/profile', methods=['GET'])
def profile():
    if not session.get('logged_in'):
        return redirect(url_for('welcome'))
    return render_template('profile.html', filename="yarg.jpg")


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if not session.get('logged_in'):
        abort(401)

    # Instantiate your form class
    filefolder = './uploads'
    form = ProfileForm()
    # Validate file upload on submit
    if request.method == 'POST':
        # Get file data and save to your uploads folder
        if form.validate_on_submit():
            file = form.upload.data
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            flash('File Saved', 'success')
        return redirect(url_for('home'))

    return render_template('upload.html', form=form)

@app.route("/uploads/<filename>")
def get_image(filename):
    root_dir = os.getcwd()

    try:
        return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route("/uploads/ProfilePic/<filename>")
def get_profile_image(filename):
    root_dir = os.getcwd()

    try:
        return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_PROFILE']), filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)

def get_uploaded_images():
    rootdir = os.getcwd()
    images=[]
    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            images.append(file)
    return images

@app.route("/files")
def files():
    if not session.get('logged_in'):
        abort(401)
    lisst = get_uploaded_images()
    return render_template('files.html', lisst=lisst)



@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit:
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user is not None and check_password_hash(user.password, password):
            print("yes")
            session['logged_in'] = True
            error = 'Invalid username or password'
            flash('You were logged in', 'success')
            return redirect(url_for('home'))
        else:
            error = 'Invalid username or password'

    return render_template('login.html', error=error, form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    error = None
    # Instantiate your form class
    filefolder = './uploads'
    form = ProfileForm()
    # Validate file upload on submit
    if request.method == 'POST':
        print("commit")
        if form.validate_on_submit():
            fname = form.fname.data
            lname = form.lname.data
            email = form.email.data
            password = form.password.data
            weight = form.weight.data
            height = form.height.data
            user = User(fname, lname, email, password, weight, height)
            print(user)

            db.session.add(user)
            db.session.commit()
            print("commit")
            return redirect(url_for('login'))
        else:
            print(form.errors)

    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out', 'success')
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")

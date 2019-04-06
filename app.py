#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os, time
from flask import Flask, render_template, flash, request, jsonify, Response
from camera import VideoCamera
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    # email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    # password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
 



#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')

response=[]
counter=0
image_dict={
    'a_1.jpg':'a_2.jpg',
    'a_2.jpg':'a_3.jpg',
    'a_3.jpg':'a_4.jpg',
    'a_4.jpg':'a_5.jpg',
    'a_5.jpg':'a_6.jpg',
    'a_6.jpg':'a_1.jpg',
}
spell_dict={
    'a_1.jpg':'MWDBEF',
    'a_2.jpg':'KLMNCG',
    'a_3.jpg':'KTPAFE',
    'a_4.jpg':'UVOQKW',
    'a_5.jpg':'ILFEGC',
    'a_6.jpg':'POIKMN',
}

def calculate():
    sum=0
    for j in response:
        sum = sum+(int)(j)
    return sum

def gen(camera):
    while True:
        frame,dist = camera.get_frame()
        time.sleep(0.2)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/process', methods=['POST'])
def process():
    name=request.form['name']
    img_name = request.form['hidden_img']
    flag = (name == spell_dict[img_name])
    # if (not flag):
    #     return jsonify({'error':'ERROR'})
    # flash('Error: All the form fields are required. ')
    return jsonify({'name':image_dict[img_name], 'flag':flag})

@app.route('/20-20', methods=['GET', 'POST'])
def twenty():
    return render_template('pages/20-20.html')

@app.route('/color_vision', methods=['GET', 'POST'])
def color_vision():
    return render_template('pages/color_vision.html')

@app.route('/side_vision', methods=['GET', 'POST'])
def side_vision():
    return render_template('pages/side_vision.html')

@app.route('/simon', methods=['GET', 'POST'])
def simon():
    return render_template('pages/simon.html')

@app.route('/eye_coordination', methods=['GET', 'POST'])
def eye_coordination():
    return render_template('pages/eye_coordination.html')

@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)



@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''

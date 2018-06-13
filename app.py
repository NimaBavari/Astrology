from flask import Flask, redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

from birthday import Birthday

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nZBGgngdYX4AHuSiFSYrOUfNCfTsHQKx'


class AngleBetweenBirthdaysForm(FlaskForm):
    first_birthday = DateField('First birthday', validators=[DataRequired()])
    second_birthday = DateField('Second birthday', validators=[DataRequired()])
    calculate_angle = SubmitField('Calculate')


def get_angle_between(d, e):
    bd_d = Birthday(d)
    bd_e = Birthday(e)
    angle = abs(bd_d.dist_deg - bd_e.dist_deg)
    return angle if angle < 180 else 360 - angle


@app.route('/', methods=['GET', 'POST'])
def index():
    angle_form = AngleBetweenBirthdaysForm()
    angle = 0
    if angle_form.validate_on_submit():
        first_birthday = angle_form.first_birthday.data.strftime('%m-%d')
        second_birthday = angle_form.second_birthday.data.strftime('%m-%d')
        angle = round(get_angle_between(first_birthday, second_birthday), 2)
    return render_template('index.html', form=angle_form, angle=angle)


if __name__ == '__main__':
    app.run(debug=True)

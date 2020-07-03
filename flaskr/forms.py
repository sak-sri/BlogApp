from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileField
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError,Email
from flaskr.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()
    ,Length(min=2,max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    password_confirmation=PasswordField('Password Confirmation',
    validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('SignUp')
    
    def validate_username(self,username):
        if(User.query.filter_by(username=username.data).first()):
            raise ValidationError("Username already exists! Please Try another One")
    
    def validate_email(self,email):
        if(User.query.filter_by(email=email.data).first()):
            raise ValidationError("Email already exists!")

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')

class UpdateForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()
    ,Length(min=2,max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    about=TextAreaField('About')
    picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Update')
    def validate_username(self,username):
        if(username.data != current_user.username):
            if(User.query.filter_by(username=username.data).first()):
                raise ValidationError("Username already exists! Please Try another One")
    def validate_email(self,email):
        if(email.data != current_user.email):
            if(User.query.filter_by(email=email.data).first()):
                raise ValidationError("Email already exists!")

class PostForm(FlaskForm):
    title=StringField('Title',validators=[DataRequired()])
    content=TextAreaField('Content',validators=[DataRequired()])
    submit=SubmitField('Submit')
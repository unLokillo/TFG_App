import datetime
import email
from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import current_user, login_required, logout_user
from flask_cors import cross_origin
from flask_api import status
from numpy import source
from . import mail, db
from flask_mail import Message
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from .models import Description, Neologismo, Source, Usuario


# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@main_bp.route('/nothing', methods=['GET', 'POST'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def nothing():
    return "", 200

@main_bp.route("/logout", methods=['GET', 'POST'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def logout():
    logout_user()
    return "logged out succesfully",204

def send_mail(user):
    token = user.get_token()
    msg = Message('Password reset request', recipients=[user.email], sender='noreply@pescaneo.com')
    msg.body = f"""
    To reset your password please follow the link below.
    
    http://127.0.0.1:5000/reset_password/{token}

    If you didn't send a password reset request ignore this.
    """
    mail.send(msg)

@main_bp.route("/reset_password", methods=['POST'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
def reset_request():
    user = Usuario.query.filter_by(email=request.json['email']).first()
    if user:
        send_mail(user)
        return "ok",status.HTTP_200_OK
    return "no user found", status.HTTP_204_NO_CONTENT

class ResetPasswordForm(FlaskForm):
    password = PasswordField(label='Nueva contraseña',validators=[
        DataRequired(),
        Length(min=8, message='LA contraseña debe tener al menos %(min)d caracteres')])
    confirm_password = PasswordField(label='Confirma la nueva contraseña',validators=[
        DataRequired(),
        EqualTo('password', message='Las contraseñas deben coincidir')])
    submit = SubmitField(label='Restablecer contraseña', validators=[DataRequired()])

@main_bp.route("/reset_password/<token>", methods=['GET', 'POST'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
def reset_token(token):
    user = Usuario.verify_token(token)
    if user is None:
        return redirect('http://localhost:8080/forgot-password')
    
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        return redirect('http://localhost:8080/login')
    return render_template('reset_request.html', title="Change password", legend="Reset password",form=form)
    
@main_bp.route("/create-neologisme", methods=['POST'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def create_neologisme():
    name = request.form['neologisme']
    likes = request.form['liked']
    state = request.form['state']
    user = current_user.id
    date = datetime.date.today()

    descriptions = []
    for i in range(int(request.form['numDescr'])):
        descriptions.append(request.form['description'+str(i)])

    sources = []
    for i in range(int(request.form['numSources'])):
        sources.append(request.form['source'+str(i)])

    if request.form['imageno'] == 'default':
        with open('./assets/default_profile.png', 'rb') as file:
            image = file.read()
    else:
        image = request.files['imagen'].read()

    new_neo = Neologismo(name=name,likes=likes,image=image,id_user=user,state=state,date_approved=date)
    db.session.add(new_neo)
    try:
        db.session.commit()
    except:
        db.session.rollback()

    db.session.refresh(new_neo)

    for i in range(len(sources)):
        new_source = Source(link=sources[i],id_neologisme=new_neo.id_neologisme)
        db.session.add(new_source)

    for i in range(len(descriptions)):
        new_description = Description(text=descriptions[i],id_neologisme=new_neo.id_neologisme)
        db.session.add(new_description)

    try:
        db.session.commit()
    except:
        db.session.rollback()

    return "Neologisme created",status.HTTP_201_CREATED
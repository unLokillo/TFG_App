import datetime
import email
from posixpath import supports_unicode_filenames
from turtle import position
from unicodedata import name
from flask import Blueprint, jsonify, render_template, redirect, request, url_for
from flask_login import current_user, login_required, logout_user
from flask_cors import cross_origin
from flask_api import status
from numpy import source
from . import mail, db
from flask_mail import Message
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from .models import Description, Neologismo, Source, UserlikesNeologisme, Usuario
from sorcery import dict_of
from sqlalchemy import func


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
    return "logged out succesfully", 204


def send_mail(user):
    token = user.get_token()
    msg = Message('Password reset request', recipients=[
                  user.email], sender='noreply@pescaneo.com')
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
        return "ok", status.HTTP_200_OK
    return "no user found", status.HTTP_204_NO_CONTENT


class ResetPasswordForm(FlaskForm):
    password = PasswordField(label='Nueva contraseña', validators=[
        DataRequired(),
        Length(min=8, message='LA contraseña debe tener al menos %(min)d caracteres')])
    confirm_password = PasswordField(label='Confirma la nueva contraseña', validators=[
        DataRequired(),
        EqualTo('password', message='Las contraseñas deben coincidir')])
    submit = SubmitField(label='Restablecer contraseña',
                         validators=[DataRequired()])


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
    return render_template('reset_request.html', title="Change password", legend="Reset password", form=form)


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

    '''if request.form['imageno'] == 'default':
        with open('./assets/default_profile.png', 'rb') as file:
            image = file.read()
    else:
        image = request.files['imagen'].read()'''

    new_neo = Neologismo(name=name, likes=likes,# image=image,
                         id_user=user, state=state, date_approved=date)
    db.session.add(new_neo)
    try:
        db.session.commit()
    except:
        db.session.rollback()

    db.session.refresh(new_neo)

    for i in range(len(sources)):
        new_source = Source(
            link=sources[i], id_neologisme=new_neo.id_neologisme)
        db.session.add(new_source)

    for i in range(len(descriptions)):
        new_description = Description(
            text=descriptions[i], id_neologisme=new_neo.id_neologisme)
        db.session.add(new_description)

    try:
        db.session.commit()
    except:
        db.session.rollback()

    return "Neologisme created", status.HTTP_201_CREATED


@main_bp.route('/user', methods=['GET'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def getuser():
    iduser = current_user.id
    nickname = current_user.nickname
    name = current_user.name
    surname = current_user.surname
    email = current_user.email
    date = current_user.birthdate.strftime("%d/%m/%y")
    mother_tongue = current_user.mother_tongue
    gender = current_user.gender
    school = current_user.school
    points = current_user.points
    query = db.session.query(Usuario, func.rank().over(
        order_by=Usuario.points.desc()).label('rankins')).filter_by(privileges=current_user.privileges).all()
    for (user, i) in query:
        if user == current_user:  # TODO: comporbar que esto funciona bien
            position = i
    fav_neo = [1, 2]
    # img
    privileges = current_user.privileges
    res = dict_of(iduser, nickname, name, surname, email, date, mother_tongue,
                  gender, school, points, position, fav_neo, privileges)
    return res, status.HTTP_200_OK


@main_bp.route('/users/<iduser>', methods=['PUT'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def putuser(iduser):
    user = Usuario.query.get(iduser)
    try:
        user.privileges = request.form['privileges']
    except:
        pass
    try:
        user.nickname = request.form['nickname']
    except:
        pass
    try:
        user.name = request.form['name']
    except:
        pass
    try:
        user.surname = request.form['surname']
    except:
        pass
    try:
        user.email = request.form['email']
    except:
        pass
    try:
        user.birthdate = request.form['date']
    except:
        pass
    try:
        user.gender = request.form['gender']
    except:
        pass
    try:
        user.password = request.form['password']
    except:
        pass
    try:
        user.school = request.form['school']
    except:
        pass
    try:
        user.mother_tongue = request.form['mother_tongue']
    except:
        pass
    try:
        user.points = request.form['points']
    except:
        pass
    try:
        db.session.commit()
    except:
        db.session.rollback()
        return "Something went wrong while committing", status.HTTP_500_INTERNAL_SERVER_ERROR
    return "modified", status.HTTP_201_CREATED


@main_bp.route('/user-neo', methods=['GET'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def getneosuser():
    query = Neologismo.query.filter_by(id_user=current_user.id).order_by(Neologismo.likes.desc())
    accepted = query.filter_by(state='aceptado').with_entities(
        Neologismo.name, Neologismo.likes, Neologismo.id_neologisme).all()
    proposed = query.filter((Neologismo.state == 'pendiente') | (Neologismo.state.contains('rechazado')))\
        .with_entities(Neologismo.name, Neologismo.state, Neologismo.id_neologisme).all()
    for i, neo in enumerate(accepted):
        accepted[i] = {'neologisme': neo[0], 'liked': neo[1], 'id': neo[2]}
    for i, neo in enumerate(proposed):
        proposed[i] = {'neologisme': neo[0], 'state': neo[1], 'id': neo[2]}
    res = {'accepted': accepted, 'proposed': proposed}
    return res, status.HTTP_200_OK


@main_bp.route('/users', methods=['GET'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def getusers():
    res = Usuario.query.order_by(Usuario.points.desc()).filter_by(
        privileges='user').limit(5).all()
    users = []
    images = []
    for i, user in enumerate(res):
        usuario = {}
        usuario['nickname'] = user.nickname
        usuario['position'] = i+1
        usuario['points'] = user.points
        users.append(usuario)
        images.append(user.image)
    return jsonify(users), status.HTTP_200_OK


@main_bp.route('/neologismes', methods=['GET'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def getneos():
    res = Neologismo.query.order_by(Neologismo.likes.desc())\
        .with_entities(Neologismo.id_user, Neologismo.name, Neologismo.likes, Neologismo.state, Neologismo.id_neologisme).all()
    neos = []
    images = []
    for i, neo in enumerate(res):
        neologismo = {}
        neologismo['user'] = Usuario.query.get(neo[0]).nickname
        neologismo['neologismo'] = neo[1]
        neologismo['position'] = i+1
        neologismo['liked'] = neo[2]
        neologismo['state'] = neo[3]
        neologismo['id'] = neo[4]
        neos.append(neologismo)
    return jsonify(neos), status.HTTP_200_OK


def getmonday():
    today = datetime.date.today().weekday()
    monday = {
        0: 1,
        1: 2,
        2: 3,
        3: 4,
        4: 5,
        5: 6,
        6: 0
    }
    return monday[today]


@main_bp.route('/week-neologismes', methods=['GET'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def getweekneos():
    res = Neologismo.query.order_by(Neologismo.likes.desc())\
        .filter((Neologismo.date_approved > (datetime.date.today()-datetime.timedelta(days=getmonday()))))\
        .with_entities(Neologismo.id_user, Neologismo.name, Neologismo.likes, Neologismo.date_approved, Neologismo.id_neologisme, Neologismo.state)\
        .all()
    neos = []
    images = []
    for i, neo in enumerate(res):
        neologismo = {}
        neologismo['descriptions'] = Description.query.filter_by(
            id_neologisme=neo[4]).with_entities(Description.text).all()
        neologismo['user'] = Usuario.query.get(neo[0]).nickname
        neologismo['neologismo'] = neo[1]
        neologismo['position'] = i+1
        neologismo['liked'] = neo[2]
        neologismo['date'] = neo[3]
        neologismo['id'] = neo[4]
        if neo[5] == 'aceptado':
            neos.append(neologismo)
        if len(neo) == 5:
            break

    return jsonify(neos), status.HTTP_200_OK


@main_bp.route('/neologismes/<neoid>', methods=['GET', 'PUT'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
def neo(neoid):
    if request.method == 'GET':
        neo = Neologismo.query.filter_by(id_neologisme=neoid)\
            .with_entities(Neologismo.id_user, Neologismo.name, Neologismo.likes, Neologismo.state, Neologismo.id_neologisme, Neologismo.date_approved)\
            .first()
        neologismo = {}
        neologismo['user'] = Usuario.query.get(neo[0]).nickname
        neologismo['descriptions'] = Description.query.filter_by(
            id_neologisme=neo[4]).with_entities(Description.text).all()
        neologismo['sources'] = Source.query.filter_by(
            id_neologisme=neo[4]).with_entities(Source.link).all()
        neologismo['neologisme'] = neo[1]
        neologismo['liked'] = neo[2]
        neologismo['state'] = neo[3]
        neologismo['date'] = neo[5].strftime("%d/%m/%y")
        return neologismo, status.HTTP_200_OK
    
    elif request.method == 'PUT':
        neo = Neologismo.query.get(neoid)
        try:
            method = request.form['do']
            if method == 'accept':
                neo.state = 'aceptado'
                neo.date_approved = datetime.date.today()
            elif method == 'reject':
                neo.state = 'rechazado: ' + request.form['message']
            elif method == 'modify':
                neo.name = request.form['name']
                neo.state = 'pendiente'

                descriptions = []
                for i in range(int(request.form['numDescr'])):
                    descriptions.append(request.form['description'+str(i)])

                sources = []
                for i in range(int(request.form['numSourc'])):
                    sources.append(request.form['source'+str(i)])

                Description.query.filter_by(id_neologisme=neoid).delete()
                Source.query.filter_by(id_neologisme=neoid).delete()
                print('Sources: ', sources, ' descrs: ', descriptions, ' name: ', request.form['name'])
                for i in range(len(sources)):
                    new_source = Source(
                        link=sources[i], id_neologisme=neoid)
                    db.session.add(new_source)

                for i in range(len(descriptions)):
                    new_description = Description(
                        text=descriptions[i], id_neologisme=neoid)
                    db.session.add(new_description)
            try:
                db.session.commit()
            except Exception as e:
                print('Committing: ', e)
                db.session.rollback()
                return "Something went wrong while commiting", status.HTTP_500_INTERNAL_SERVER_ERROR
        except Exception as e:
            print('Modifying: ', e)
            return "Something went wrong", status.HTTP_500_INTERNAL_SERVER_ERROR
        return "neologism succesfully modified", status.HTTP_201_CREATED


@main_bp.route('/allusers', methods=['GET'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def getallusers():
    if current_user.privileges == 'admin':
        res = Usuario.query.order_by(Usuario.points.desc()).all()
    elif current_user.privileges == 'linguist':
        res = Usuario.query.order_by(Usuario.points.desc()).filter(
            Usuario.privileges != 'admin').all()
    else:
        res = Usuario.query.order_by(
            Usuario.points.desc()).filter_by(privileges='user').all()
    users = []
    #images = []
    for i, user in enumerate(res):
        usuario = {}
        usuario['nickname'] = user.nickname
        usuario['position'] = i+1
        usuario['points'] = user.points
        usuario['id'] = user.id
        usuario['privileges'] = user.privileges
        users.append(usuario)
        # images.append(user.image)
    return jsonify(users), status.HTTP_200_OK


@main_bp.route('/neologismes/<neoid>/likes', methods=['GET', 'POST', 'DELETE'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def neolikes(neoid):
    if request.method == 'GET':
        users = UserlikesNeologisme.query.filter(
            UserlikesNeologisme.id_neologisme == neoid).all()
        res = []
        for i, user in enumerate(users):
            usuario = {}
            usuario['nickname'] = user.usuario.nickname
            res.append(usuario)
        return jsonify(res), status.HTTP_200_OK
    elif request.method == 'POST':
        like = UserlikesNeologisme(
            id_user=current_user.id, id_neologisme=neoid)
        db.session.add(like)
        neo = Neologismo.query.get(neoid)
        neo.likes += 1
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return "Something bad happened while commiting", status.HTTP_500_INTERNAL_SERVER_ERROR
        return {'id_neologisme': neo.id_neologisme, 'id_user': neo.id_user}, status.HTTP_201_CREATED
    else:  # DELETE
        UserlikesNeologisme.query.filter(
            (UserlikesNeologisme.id_neologisme == neoid) & (UserlikesNeologisme.id_user == current_user.id)).delete()
        neo = Neologismo.query.get(neoid)
        neo.likes -= 1
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return "Something bad happened while commiting", status.HTTP_500_INTERNAL_SERVER_ERROR
        return "Removed succesfully", status.HTTP_204_NO_CONTENT


@main_bp.route('/users/<userid>/favs', methods=['GET'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def userlikes(userid):
    neoids = UserlikesNeologisme.query.filter_by(id_user=userid).with_entities(UserlikesNeologisme.id_neologisme).all()
    for i, neo in enumerate(neoids):
        neoids[i] = neoids[i][0]
    neos = Neologismo.query.filter(Neologismo.id_neologisme.in_(neoids)).all()
    res = []
    for i, neo in enumerate(neos):
        neologismo = {}
        neologismo['id'] = neo.id_neologisme
        neologismo['likes'] = neo.likes
        neologismo['name'] = neo.name
        neologismo['state'] = neo.state
        neologismo['user'] = Usuario.query.get(neo.id_user).nickname
        res.append(neologismo)
    return jsonify(res), status.HTTP_200_OK
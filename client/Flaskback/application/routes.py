import datetime
import email
from posixpath import supports_unicode_filenames
from random import random
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
from .models import Description, Logro, Neologismo, Source, UserGetsAchievement, UserlikesNeologisme, Usuario
from sorcery import dict_of
from sqlalchemy import func
import uuid


# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route("/logout", methods=['GET', 'POST'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def logout():
    logout_user()
    return "logged out succesfully", 204


def send_mail(user):
    token = user.get_token()
    msg = Message('Password reset request', recipients=[
                  user.email], sender='pescaneoapp@gmail.com')
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

    new_neo = Neologismo(name=name, likes=likes,  # image=image,
                         id_user=user, state=state)
    db.session.add(new_neo)

    uga = UserGetsAchievement(
        id_user=user, id_achievement=2, date=datetime.date.today())
    db.session.add(uga)
    userp = Usuario.query.get(user)
    userp.points += 10

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

    # Logro de neologismos propuestos
    neoq = Neologismo.query.filter(Neologismo.id_user==current_user.id).all()
    if len(neoq)==5 or len(neoq)==20:
        ugaq = UserGetsAchievement.query.filter((UserGetsAchievement.id_user==current_user.id) &
                                                ((UserGetsAchievement.id_achievement==16) |
                                                (UserGetsAchievement.id_achievement==17))).all()
        ugaqs = {}
        for uga in ugaq:
            if uga.id_achievement == 16:
                ugaqs[16] = True
            if uga.id_achievement == 17:
                ugaqs[17] = True
        if len(neoq) == 5 and 16 not in ugaqs:
            uga = UserGetsAchievement(
                id_user=current_user.id, id_achievement=16, date=datetime.date.today())
            db.session.add(uga)
            userp.points += 50
        elif len(neoq) == 20 and 17 not in ugaqs:
            uga = UserGetsAchievement(
                id_user=current_user.id, id_achievement=17, date=datetime.date.today())
            db.session.add(uga)
            userp.points += 100

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


@main_bp.route('/users/<iduser>', methods=['PUT', 'DELETE'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def putuser(iduser):
    if request.method == 'PUT':
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
            user.set_password(request.form['password'])
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
    elif request.method == 'DELETE':
        user = Usuario.query.get(iduser)
        user.set_password(str(uuid.uuid4()))
        user.privileges = 'removed'
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return "Something went wrong while committing", status.HTTP_500_INTERNAL_SERVER_ERROR
        return "deleted", status.HTTP_204_NO_CONTENT


@main_bp.route('/user-neo', methods=['GET'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def getneosuser():
    query = Neologismo.query.filter_by(
        id_user=current_user.id).order_by(Neologismo.likes.desc())
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
        neouser = Usuario.query.get(neo[0])

        # Logro neo de la semana
        if i == 0 or i == 1 or i == 2 or i == 3 or i == 4:
            ugaq = UserGetsAchievement.query.filter((UserGetsAchievement.id_user==neouser.id) &
                                                    (UserGetsAchievement.id_achievement==20)).all()
            if len(ugaq) == 0:
                uga = UserGetsAchievement(
                    id_user=neouser.id, id_achievement=20, date=datetime.date.today())
                db.session.add(uga)
                neouser.points += 200
                try:
                    db.session.commit()
                except:
                    db.session.rollback()
                    return "Something went wrong while commiting", status.HTTP_500_INTERNAL_SERVER_ERROR


        neologismo = {}
        neologismo['user'] = neouser.nickname
        neologismo['neologismo'] = neo[1]
        neologismo['position'] = i+1
        neologismo['liked'] = neo[2]
        neologismo['state'] = neo[3]
        neologismo['id'] = neo[4]
        neologismo['descriptions'] = Description.query.filter_by(
            id_neologisme=neo[4]).with_entities(Description.text).all()
        neologismo['sources'] = Source.query.filter_by(
            id_neologisme=neo[4]).with_entities(Source.link).all()
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
        .filter((Neologismo.date_approved > (datetime.date.today()-datetime.timedelta(days=getmonday()))) & (Neologismo.state=='aceptado'))\
        .with_entities(Neologismo.id_user, Neologismo.name, Neologismo.likes, Neologismo.date_approved, Neologismo.id_neologisme, Neologismo.state)\
        .all()
    neos = []
    images = []
    for i, neo in enumerate(res):
        neouser = Usuario.query.get(neo[0])

        # Logro neo de la semana
        if i == 0 or i == 1 or i == 2:
            ugaq = UserGetsAchievement.query.filter((UserGetsAchievement.id_user==neouser.id) &
                                                    (UserGetsAchievement.id_achievement==3)).all()
            if len(ugaq) == 0:
                uga = UserGetsAchievement(
                    id_user=neouser.id, id_achievement=3, date=datetime.date.today())
                db.session.add(uga)
                neouser.points += 150
                try:
                    db.session.commit()
                except:
                    db.session.rollback()
                    return "Something went wrong while commiting", status.HTTP_500_INTERNAL_SERVER_ERROR

        neologismo = {}
        neologismo['descriptions'] = Description.query.filter_by(
            id_neologisme=neo[4]).with_entities(Description.text).all()
        neologismo['user'] = neouser.nickname
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


@main_bp.route('/neologismes/<neoid>', methods=['GET', 'PUT', 'DELETE'])
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
        if neo[5] is not None:
            neologismo['date'] = neo[5].strftime("%d/%m/%y")
        else:
            neologismo['date'] = 'None'
        return neologismo, status.HTTP_200_OK

    elif request.method == 'PUT':
        neo = Neologismo.query.get(neoid)
        try:
            method = request.form['do']
            if method == 'accept':
                neo.state = 'aceptado'
                neo.date_approved = datetime.date.today()
                uga = UserGetsAchievement(
                    id_user=neo.id_user, id_achievement=1, date=datetime.date.today())
                db.session.add(uga)
                user = Usuario.query.get(neo.id_user)
                user.points += 50
                try:
                    db.session.commit()
                except:
                    db.session.rollback()
                    return "Something went wrong while commiting", status.HTTP_500_INTERNAL_SERVER_ERROR
                
                ugaq = UserGetsAchievement.query.filter((UserGetsAchievement.id_user==neo.id_user) &
                                                        (UserGetsAchievement.id_achievement==1)).all()
                if len(ugaq) == 3:
                    uga = UserGetsAchievement(
                        id_user=neo.id_user, id_achievement=18, date=datetime.date.today())
                    db.session.add(uga)
                    user.points += 80
                elif len(ugaq) == 6:
                    uga = UserGetsAchievement(
                        id_user=neo.id_user, id_achievement=19, date=datetime.date.today())
                    db.session.add(uga)
                    user.points += 100
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
            except:
                db.session.rollback()
                return "Something went wrong while commiting", status.HTTP_500_INTERNAL_SERVER_ERROR
        except Exception as e:
            print('Modifying: ', e)
            return "Something went wrong", status.HTTP_500_INTERNAL_SERVER_ERROR
        return "neologism succesfully modified", status.HTTP_201_CREATED

    elif request.method == 'DELETE':
        neo = Neologismo.query.get(neoid)
        neo.state = 'rechazado: Este neologismo ha sido eliminado. Para recuperarlo como propuesta use el botón: Modificar'
        neo.likes = 0
        UserlikesNeologisme.query.filter_by(id_neologisme=neoid).delete()
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return "Something went wrong while commiting", status.HTTP_500_INTERNAL_SERVER_ERROR
        return "Neologisme deleted", status.HTTP_204_NO_CONTENT



@main_bp.route('/allusers', methods=['GET'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def getallusers():
    if current_user.privileges == 'admin':
        res = Usuario.query.order_by(Usuario.points.desc()).filter(
            Usuario.privileges != 'removed').all()
    elif current_user.privileges == 'linguist':
        res = Usuario.query.order_by(Usuario.points.desc()).filter(
            Usuario.privileges != 'admin' and Usuario.privileges != 'removed').all()
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

        # Añadimos el like a la base de datos y al neologismo
        like = UserlikesNeologisme(
            id_user=current_user.id, id_neologisme=neoid)
        db.session.add(like)
        neo = Neologismo.query.get(neoid)
        neo.likes += 1
        # Lo guardamos para hacer la siguiente consulta
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return "Something bad happened while commiting", status.HTTP_500_INTERNAL_SERVER_ERROR

        # Pedimos los logros sobre likes dados
        ugaquery0 = UserGetsAchievement.query.filter((UserGetsAchievement.id_user==neo.id_user) & (
                                                        (UserGetsAchievement.id_achievement==13) |
                                                        (UserGetsAchievement.id_achievement==14) |
                                                        (UserGetsAchievement.id_achievement==15))).all()
        # Apuntamos los que hay
        ugas0 = {}
        for uga in ugaquery0:
            if uga.id_achievement == 13:
                ugas0[13] = True
            elif uga.id_achievement == 14:
                ugas0[14] = True
            elif uga.id_achievement == 15:
                ugas0[15] = True

        # Damos el logro que corresponda de likes dados
        likesquery = UserlikesNeologisme.query.filter(UserlikesNeologisme.id_user == current_user.id).all()
        if len(likesquery) == 5 and not 13 in ugas0:
            uga = UserGetsAchievement(
                id_user=current_user.id, id_achievement=13, date=datetime.date.today())
            db.session.add(uga)
            userr = Usuario.query.get(current_user.id)
            userr.points += 10
        elif len(likesquery) == 20 and not 14 in ugas0:
            uga = UserGetsAchievement(
                id_user=current_user.id, id_achievement=14, date=datetime.date.today())
            db.session.add(uga)
            userr = Usuario.query.get(current_user.id)
            userr.points += 30
        elif len(likesquery) == 100 and not 15 in ugas0:
            uga = UserGetsAchievement(
                id_user=current_user.id, id_achievement=15, date=datetime.date.today())
            db.session.add(uga)
            userr = Usuario.query.get(current_user.id)
            userr.points += 70

        # Añadimos el logro de like recibido
        uga = UserGetsAchievement(
            id_user=neo.id_user, id_achievement=4, date=datetime.date.today())
        db.session.add(uga)
        user = Usuario.query.get(neo.id_user)
        user.points += 10

        # Pedimos los logros de likes recibidos
        ugaquery = UserGetsAchievement.query.filter((UserGetsAchievement.id_user==neo.id_user) & (
                                                        (UserGetsAchievement.id_achievement==10) |
                                                        (UserGetsAchievement.id_achievement==11) |
                                                        (UserGetsAchievement.id_achievement==12))).all()
        ugas = {}
        for uga in ugaquery:
            if uga.id_achievement == 10:
                ugas[10] = True
            elif uga.id_achievement == 11:
                ugas[11] = True
            elif uga.id_achievement == 12:
                ugas[12] = True
        # Damos el logro que corresponda de likes recibidos
        if neo.likes == 5 and not 10 in ugas:
            uga = UserGetsAchievement(
                id_user=neo.id_user, id_achievement=10, date=datetime.date.today())
            db.session.add(uga)
            user.points += 20
        elif neo.likes == 20 and not 11 in ugas:
            uga = UserGetsAchievement(
                id_user=neo.id_user, id_achievement=11, date=datetime.date.today())
            db.session.add(uga)
            user.points += 50
        elif neo.likes == 100 and not 12 in ugas:
            uga = UserGetsAchievement(
                id_user=neo.id_user, id_achievement=12, date=datetime.date.today())
            db.session.add(uga)
            user.points += 100

        # Hacemos commit y devolvemos
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
    neoids = UserlikesNeologisme.query.filter_by(
        id_user=userid).with_entities(UserlikesNeologisme.id_neologisme).all()
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


@main_bp.route('/badges', methods=['GET', 'POST'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def badges():
    if request.method == 'GET':
        uga = UserGetsAchievement.query.filter_by(
            id_user=current_user.id).all()
        ugas = []
        for ugach in uga:
            logro = Logro.query.get(ugach.id_achievement)
            achiev = {}
            achiev['Nombre'] = logro.description
            achiev['Acción'] = logro.action
            achiev['Puntos'] = logro.difficulty*10
            achiev['Fecha'] = ugach.date.strftime("%d/%m/%y")
            ugas.append(achiev)
        return jsonify(ugas), status.HTTP_200_OK
    elif request.method == 'POST':
        if request.form['achiev'] == '5':
            ugaquery = UserGetsAchievement.query.filter((UserGetsAchievement.id_achievement == 5) &
                                                        (UserGetsAchievement.id_user == current_user.id)).all()
            exists = False
            for ugaq in ugaquery:
                if ugaq.date.date() == datetime.date.today():
                    exists = True
                    break
            if not exists:
                uga = UserGetsAchievement(
                    id_user=current_user.id, id_achievement=5, date=datetime.date.today())
                db.session.add(uga)

                userp = Usuario.query.get(current_user.id)
                userp.points += 40
                try:
                    db.session.commit()
                except:
                    db.session.rollback()
                    return "Something went wrong while commiting", status.HTTP_500_INTERNAL_SERVER_ERROR
                return "Added succesfully", status.HTTP_201_CREATED
            else:
                return "Badge already given", status.HTTP_204_NO_CONTENT
        elif request.form['achiev'] == 'login':
            qtoday = UserGetsAchievement.query.filter((UserGetsAchievement.id_achievement == 6) &
                                                        (UserGetsAchievement.id_user == current_user.id)).all()
            days = {}
            for ugaq in qtoday:
                if ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day):
                    days[0] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=1):
                    days[1] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=2):
                    days[2] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=3):
                    days[3] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=4):
                    days[4] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=5):
                    days[5] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=6):
                    days[6] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=7):
                    days[7] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=8):
                    days[8] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=9):
                    days[9] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=10):
                    days[10] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=11):
                    days[11] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=12):
                    days[12] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=13):
                    days[13] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=14):
                    days[14] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=15):
                    days[15] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=16):
                    days[16] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=17):
                    days[17] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=18):
                    days[18] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=19):
                    days[19] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=20):
                    days[20] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=21):
                    days[21] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=22):
                    days[22] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=23):
                    days[23] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=24):
                    days[24] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=25):
                    days[25] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=26):
                    days[26] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=27):
                    days[27] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=28):
                    days[28] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=29):
                    days[29] = True
                elif ugaq.date == datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) - datetime.timedelta(days=30):
                    days[30] = True
                
            if 0 in days:
                return "No badge given", status.HTTP_204_NO_CONTENT
            
            uga = UserGetsAchievement(
                    id_user=current_user.id, id_achievement=6, date=datetime.date.today())
            db.session.add(uga)

            userp = Usuario.query.get(current_user.id)
            userp.points += 10
            if 1 not in days:
                try:
                    db.session.commit()
                except:
                    db.session.rollback()
                    return "Something went wrong while commiting one login badge", status.HTTP_500_INTERNAL_SERVER_ERROR
                return "One login badge given", status.HTTP_201_CREATED

            if 2 not in days:
                uga = UserGetsAchievement(
                    id_user=current_user.id, id_achievement=7, date=datetime.date.today())
                db.session.add(uga)
                userp.points += 20
                try:
                    db.session.commit()
                except:
                    db.session.rollback()
                    return "Something went wrong while commiting two login badge", status.HTTP_500_INTERNAL_SERVER_ERROR
                return "One and two logins badges given", status.HTTP_201_CREATED
            
            if 3 not in days or 4 not in days:
                try:
                    db.session.commit()
                except:
                    db.session.rollback()
                    return "Something went wrong while commiting two login badge", status.HTTP_500_INTERNAL_SERVER_ERROR
                return "One login badge given", status.HTTP_201_CREATED

            if 5 not in days:
                uga = UserGetsAchievement(
                    id_user=current_user.id, id_achievement=8, date=datetime.date.today())
                db.session.add(uga)
                userp.points += 50
                try:
                    db.session.commit()
                except:
                    db.session.rollback()
                    return "Something went wrong while commiting two login badge", status.HTTP_500_INTERNAL_SERVER_ERROR
                return "Five logins badge given", status.HTTP_201_CREATED
            
            if 6 not in days or 7 not in days or 8 not in days or 9 not in days or 10 not in days or \
                11 not in days or 12 not in days or 13 not in days or 14 not in days or 15 not in days or \
                16 not in days or 17 not in days or 18 not in days or 19 not in days or 20 not in days or \
                21 not in days or 22 not in days or 23 not in days or 24 not in days or 25 not in days or \
                26 not in days or 27 not in days or 28 not in days or 29 not in days:
                    try:
                        db.session.commit()
                    except:
                        db.session.rollback()
                        return "Something went wrong while commiting two login badge", status.HTTP_500_INTERNAL_SERVER_ERROR
                    return "One login badge given", status.HTTP_201_CREATED
            
            uga = UserGetsAchievement(
                id_user=current_user.id, id_achievement=9, date=datetime.date.today())
            db.session.add(uga)
            userp.points += 100
            try:
                db.session.commit()
            except:
                db.session.rollback()
                return "Something went wrong while commiting two login badge", status.HTTP_500_INTERNAL_SERVER_ERROR
            return "A month of logins badge given", status.HTTP_201_CREATED

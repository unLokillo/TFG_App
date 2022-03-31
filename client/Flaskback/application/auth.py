from flask import Blueprint, redirect, render_template, flash, request, session, url_for, make_response
from flask_login import login_required, logout_user, current_user, login_user
from .models import db, Usuario
from . import login_manager
from flask_api import status
from flask_cors import CORS, cross_origin
from datetime import datetime, timedelta
from os import path, pardir, getcwd


# Blueprint Configuration
auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route('/login', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
def login():
    if request.method == "POST":
        if current_user.is_authenticated:
            print('ya estabas logeado tontorron')
            return "Ok", 200
        usuario = Usuario.query.filter(((Usuario.email == request.json[
            'username']) | (Usuario.nickname == request.json['username']))).first()
        pwd = request.json['password']
        if usuario is None or not usuario.check_password(password=pwd):
            return "Usuario y/o contraseña incorrectos", 400
        else:
            login_user(usuario, remember=True, force=True,
                       duration=timedelta(days=365))
            return "Ok", 200
    elif request.method == "GET":
        res_fields = {
            'success': False,
            'username': "",
            'image': "",
            'user_id': 0
        }
        if current_user.is_authenticated:
            res_fields['success'] = True
            res_fields['username'] = current_user.nickname
            # res_fields['image'] = current_user.image # TODO insertar imagen
            res_fields['user_id'] = current_user.id
            return res_fields, status.HTTP_200_OK

        return res_fields, status.HTTP_401_UNAUTHORIZED


@auth_bp.route('/signup', methods=['POST'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
def signup():
    username = request.form['nickname']
    passw = request.form['password']
    email = request.form['email']
    name = request.form['name']
    surname = request.form['surname']
    birthdate = request.form['date']
    gender = request.form['gender']
    school = request.form['school']
    mother_tongue = request.form['mother_tongue']
    if request.form['imageno'] == 'default':
        with open('./assets/default_profile.png', 'rb') as file:
            image = file.read()
    else:
        image = request.files['imagen'].read()
    points = request.form['points']
    privileges = request.form['privileges']

    # Busqueda de usuario ya existente
    if Usuario.query.filter_by(nickname=username).count() > 0 \
            or Usuario.query.filter_by(email=username).count() > 0 \
            or Usuario.query.filter_by(email=email).count() > 0:
        return "Usuario ya existente", status.HTTP_400_BAD_REQUEST

    # Creacion y adicion del usuario
    new_user = Usuario(nickname=username,
                       email=email,
                       name=name,
                       surname=surname,
                       birthdate=datetime.strptime(birthdate, '%Y-%m-%d'),
                       gender=gender,
                       school=school,
                       mother_tongue=mother_tongue,
                       image=image,
                       points=points,
                       privileges=privileges)
    new_user.set_password(passw)
    db.session.add(new_user)
    try:
        db.session.commit()
    except:
        db.session.rollback()
    login_user(new_user)
    return "ok", status.HTTP_201_CREATED


@auth_bp.route('/users', methods=['GET'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
@login_required
def getusers():
    pass # TODO devolver usuarios
    return "ahora sí tss", status.HTTP_200_OK


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return Usuario.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    return "You need to be logged in to enter this place.", status.HTTP_401_UNAUTHORIZED

from enum import unique
from turtle import position
from flask import Flask, request, jsonify, json, session
from flask_api import status
from flask_cors import CORS, cross_origin
#import sqlite3

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}}, CORS_SUPPORTS_CREDENTIALS=True)
app.config['CORS_HEADERS'] = 'Content-Type'

app.secret_key = b'fmVb@st^jCP7f$uM'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Usuario(db.Model):
    __tablename__ = "usuarios"
    id_user = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    birthdate = db.Column(db.Date)
    gender = db.Column(db.String(20))
    password = db.Column(db.String(50), nullable=False)
    school = db.Column(db.String(15), nullable=False)
    mother_tongue = db.Column(db.String(20))
    image = db.Column(db.LargeBinary)
    points = db.Column(db.Integer, nullable=False)
    position = db.Column(db.Integer, unique=True, nullable=False)
    privileges = db.Column(db.String(15), nullable=False)

    def __init__(self, nickname, name, surname, email, birthdate,
                 gender, password, school, mother_tongue, image, points, privileges):
        # Add the data to the instance
        self.nickname = nickname
        self.name = name
        self.surname = surname
        self.email = email
        self.birthdate = birthdate
        self.gender = gender
        self.password = password
        self.school = school
        self.mother_tongue = mother_tongue
        self.image = image
        self.points = points
        self.privileges = privileges


class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('nickname', 'name', 'surname', 'email', 'birthdate',
                  'gender', 'password', 'school', 'mother_tongue', 'image', 'points', 'privileges')


class Neologismo(db.Model):
    __tablename__ = "neologismos"
    id_neologisme = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    likes = db.Column(db.Integer)
    image = db.Column(db.Binary)
    state = db.Column(db.String(20))
    position = db.Column(db.Integer, unique=True)
    id_user = db.Column(db.Integer, db.ForeignKey("usuarios.id_user"))
    user = db.relationship("Usuario", backref="neologismes")

    def __init__(self, id_neologisme, name, likes, image, state, position, id_user, user):
        self.id_neologisme = id_neologisme
        self.name = name
        self.likes = likes
        self.image = image
        self.state = state
        self.position = position
        self.id_user = id_user
        self.user = user


class NeologismoSchema(ma.Schema):
    class Meta:
        fields = ('id_neologisme', 'name', 'likes', 'image',
                  'state', 'position', 'id_user', 'user')


class Logro(db.Model):
    __tablename__ = "logros"
    id_achievement = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
    action = db.Column(db.String(100))
    difficulty = db.Column(db.Integer)
    name = db.Column(db.String(30))
    medal = db.Column(db.Binary)

    def __init__(self, id_achievement, description, action, difficulty, name, medal):
        self.id_achievement = id_achievement
        self.description = description
        self.action = action
        self.difficulty = difficulty
        self.name = name
        self.medal = medal


class LogroSchema(ma.Schema):
    class Meta:
        fields = ('id_achievement', 'description',
                  'action', 'difficulty', 'name', 'medal')


class Source(db.Model):
    __tablename__ = "sources"
    id_source = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(300))
    id_neologisme = db.Column(
        db.Integer, db.ForeignKey('neologismos.id_neologisme'))
    neologisme = db.relationship("Neologismo", backref='sources')

    def __init__(self, id_source, link, id_neologisme, neologisme):
        self.id_source = id_source
        self.link = link
        self.id_neologisme = id_neologisme
        self.neologisme = neologisme


class SourceSchema(ma.Schema):
    class Meta:
        fields = ('id_source', 'link', 'id_neologisme', 'neologisme')


class Description(db.Model):
    __tablename__ = "descriptions"
    id_description = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300))
    id_neologisme = db.Column(
        db.Integer, db.ForeignKey('neologismos.id_neologisme'))
    neologisme = db.relationship("Neologismo", backref='descriptions')

    def __init__(self, id_description, text, id_neologisme, neologisme):
        self.id_description = id_description
        self.text = text
        self.id_neologisme = id_neologisme
        self.neologisme = neologisme


class DescriptionSchema(ma.Schema):
    class Meta:
        fields = ('id_description', 'text', 'id_neologisme', 'neologisme')


class UserGetsAchievement(db.Model):
    id_uga = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey(
        'usuarios.id_user'))
    id_achievement = db.Column(
        db.Integer, db.ForeignKey('logros.id_achievement'))
    usuario = db.relationship("Usuario", backref='logros')
    logro = db.relationship("Logro", backref='usuarios')
    date = db.Column(db.Date)

    def __init__(self, id_uga, id_user, id_achievement, usuario, logro, date):
        self.id_uga = id_uga
        self.id_user = id_user
        self.id_achievement = id_achievement
        self.usuario = usuario
        self.logro = logro
        self.date = date


class UGASchema(ma.Schema):
    class Meta:
        fields = ('id_uga', 'id_user', 'id_achievement', 'usuario', 'logro', 'date')


class UserlikesNeologisme(db.Model):
    id_uln = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey(
        'usuarios.id_user'))
    id_neologisme = db.Column(
        db.Integer, db.ForeignKey('neologismos.id_neologisme'))
    usuario = db.relationship("Usuario", backref='likedneologismes')
    neologismo = db.relationship("Neologismo", backref='usuariosliked')

    def __init__(self, id_uln, id_user, id_neologisme, usuario, logro):
        self.id_uln = id_uln
        self.id_user = id_user
        self.id_neologisme = id_neologisme
        self.usuario = usuario
        self.logro = logro


class ULNSchema(ma.Schema):
    class Meta:
        fields = ('id_uln', 'id_user', 'id_neologisme', 'usuario', 'logro')


usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

neologismo_schema = NeologismoSchema()
neologismos_schema = NeologismoSchema(many=True)

logro_schema = LogroSchema()
logros_schema = LogroSchema(many=True)

source_schema = SourceSchema()
sources_schema = SourceSchema(many=True)

description_schema = DescriptionSchema()
descriptions_schema = DescriptionSchema(many=True)

uga_schema = UGASchema()
ugas_schema = UGASchema(many=True)

uln_schema = ULNSchema()
ulns_schema = ULNSchema(many=True)


@app.route("/users", methods=["POST"])
@cross_origin(origin='*', headers=['content-type'])
def create_user():

    username = request.json('username')
    passw = request.json('password')
    email = request.json('email')
    name = request.json('name')
    surname = request.json('surname')
    birthdate = request.json('birthdate')
    gender = request.json('gender')
    school = request.json('school')
    mother_tongue = request.json('mother_tongue')
    image = request.json('image')  # TODO cargar imagen
    points = request.json('points')
    privileges = request.json('privileges')

    # Busqueda de usuario ya existente
    if Usuario.query.filter_by(username=username).count() > 0 \
            or Usuario.query.filter_by(email=username).count() > 0:
        return "Usuario ya existente", status.HTTP_400_BAD_REQUEST
        pass  # TODO Devolver error de ya existente

        # Creacion y adicion del usuario
    new_user = Usuario(nickname=username,
                       password=passw,
                       email=email,
                       name=name,
                       surname=surname,
                       birthdate=birthdate,
                       gender=gender,
                       school=school,
                       mother_tongue=mother_tongue,
                       image=image,
                       points=points,
                       privileges=privileges)
    db.session.add(new_user)
    db.session.commit()
    return usuario_schema.jsonify(new_user)


@app.route("/users", methods=["GET"])
@cross_origin(origin='*', headers=['content-type'])
def get_all_users():
    all_users = Usuario.query.all()
    res = usuarios_schema.dump(all_users)
    return jsonify(res)


@app.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "POST":
        usuario = Usuario.query.filter(((Usuario.email == request.json[
            'username']) | (Usuario.nickname == request.json['username']))).first()
        pwd = request.json['password']
        print(usuario)
        if usuario is None or usuario.password != pwd:
            return "Usuario y/o contraseña incorrectos", 400
        else:
            session['username'] = request.json['nickname']
            return "Ok", 200
    elif request.method == "GET":
        if 'username' in session:
            return session['username'], 200


@app.route("/nothing", methods=["POST", "GET"])
def nothing():
    return "", 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

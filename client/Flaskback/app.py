from enum import unique
from turtle import position
from flask import Flask, request, jsonify, json, session
from flask_api import status
from flask_cors import CORS, cross_origin
import sqlite3

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
    id_user = db.Column(db.Integer, primary_key=True, nullable=False)
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


usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)


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

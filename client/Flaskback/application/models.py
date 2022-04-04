from . import db, ma
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(UserMixin, db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, db.Sequence('id_user'), primary_key=True)
    nickname = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    birthdate = db.Column(db.DateTime)
    gender = db.Column(db.String(20))
    password = db.Column(db.String(200), nullable=False)
    school = db.Column(db.String(15), nullable=False)
    mother_tongue = db.Column(db.String(20))
    image = db.Column(db.LargeBinary)
    points = db.Column(db.Integer, nullable=False)
    privileges = db.Column(db.String(15), nullable=False)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.nickname)


class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('nickname', 'name', 'surname', 'email', 'birthdate',
                  'gender', 'password', 'school', 'mother_tongue', 'image', 'points', 'privileges')


class Neologismo(db.Model):
    __tablename__ = "neologismos"
    id_neologisme = db.Column(db.Integer, db.Sequence(
        'id_neologismo'), primary_key=True)
    name = db.Column(db.String(100))
    likes = db.Column(db.Integer)
    image = db.Column(db.LargeBinary)
    date_approved = db.Column(db.DateTime)
    state = db.Column(db.String(20))
    position = db.Column(db.Integer, unique=True)
    id_user = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    user = db.relationship("Usuario", backref="neologismes")

    def __init__(self, id_neologisme, name, likes, image, date_approved, state, position, id_user, user):
        self.id_neologisme = id_neologisme
        self.name = name
        self.likes = likes
        self.image = image
        self.date_approved = date_approved
        self.state = state
        self.position = position
        self.id_user = id_user
        self.user = user


class NeologismoSchema(ma.Schema):
    class Meta:
        fields = ('id_neologisme', 'name', 'likes', 'image',
                  'date_approved','state', 'position', 'id_user', 'user')


class Logro(db.Model):
    __tablename__ = "logros"
    id_achievement = db.Column(
        db.Integer, db.Sequence('id_logro'), primary_key=True)
    description = db.Column(db.String(100))
    action = db.Column(db.String(100))
    difficulty = db.Column(db.Integer)
    name = db.Column(db.String(30))
    medal = db.Column(db.LargeBinary)

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
    id_source = db.Column(db.Integer, db.Sequence(
        'id_source'), primary_key=True)
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
    id_description = db.Column(db.Integer, db.Sequence(
        'id_description'), primary_key=True)
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
    __tablename__ = "users_get_achievements"
    id_uga = db.Column(db.Integer, db.Sequence('id_uga'), primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey(
        'usuarios.id'))
    id_achievement = db.Column(
        db.Integer, db.ForeignKey('logros.id_achievement'))
    usuario = db.relationship("Usuario", backref='logros')
    logro = db.relationship("Logro", backref='usuarios')
    date = db.Column(db.DateTime)

    def __init__(self, id_uga, id_user, id_achievement, usuario, logro, date):
        self.id_uga = id_uga
        self.id_user = id_user
        self.id_achievement = id_achievement
        self.usuario = usuario
        self.logro = logro
        self.date = date


class UGASchema(ma.Schema):
    class Meta:
        fields = ('id_uga', 'id_user', 'id_achievement',
                  'usuario', 'logro', 'date')


class UserlikesNeologisme(db.Model):
    __tablename__ = "users_like_neologismes"
    id_uln = db.Column(db.Integer, db.Sequence('id_uln'), primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey(
        'usuarios.id'))
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

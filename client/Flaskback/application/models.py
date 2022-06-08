from itsdangerous import TimestampSigner
from . import db, app
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

    def get_token(self):
        serial = TimestampSigner(app.config.get('SECRET_KEY'))
        return serial.sign(str(self.id)).decode('utf-8')

    @staticmethod
    def verify_token(token):
        serial = TimestampSigner(app.config.get('SECRET_KEY'))
        try:
            user_id = int(serial.unsign(token, max_age=600).decode('utf-8'))
        except:
            return None
        return Usuario.query.get(user_id)

    def __repr__(self):
        return '<User {}>'.format(self.nickname)


class Neologismo(db.Model):
    __tablename__ = "neologismos"
    id_neologisme = db.Column(db.Integer, db.Sequence(
        'id_neologismo'), primary_key=True)
    name = db.Column(db.String(100))
    name_eng = db.Column(db.String(100))
    likes = db.Column(db.Integer)
    image = db.Column(db.LargeBinary)
    date_approved = db.Column(db.DateTime)
    state = db.Column(db.String(20))
    id_user = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    user = db.relationship("Usuario", backref="neologismes")


class Logro(db.Model):
    __tablename__ = "logros"
    id_achievement = db.Column(
        db.Integer, db.Sequence('id_logro'), primary_key=True)
    description = db.Column(db.String(100))
    action = db.Column(db.String(100))
    difficulty = db.Column(db.Integer)
    name = db.Column(db.String(30))
    medal = db.Column(db.LargeBinary)


class Source(db.Model):
    __tablename__ = "sources"
    id_source = db.Column(db.Integer, db.Sequence(
        'id_source'), primary_key=True)
    link = db.Column(db.String(300))
    id_neologisme = db.Column(
        db.Integer, db.ForeignKey('neologismos.id_neologisme'))
    neologisme = db.relationship("Neologismo", backref='sources')


class Description(db.Model):
    __tablename__ = "descriptions"
    id_description = db.Column(db.Integer, db.Sequence(
        'id_description'), primary_key=True)
    text = db.Column(db.String(300))
    id_neologisme = db.Column(
        db.Integer, db.ForeignKey('neologismos.id_neologisme'))
    neologisme = db.relationship("Neologismo", backref='descriptions')


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


class UserlikesNeologisme(db.Model):
    __tablename__ = "users_like_neologismes"
    id_uln = db.Column(db.Integer, db.Sequence('id_uln'), primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey(
        'usuarios.id'))
    id_neologisme = db.Column(
        db.Integer, db.ForeignKey('neologismos.id_neologisme'))
    usuario = db.relationship("Usuario", backref='likedneologismes')
    neologismo = db.relationship("Neologismo", backref='usuariosliked')


class ErrorNotification(db.Model):
    __tablename__ = "error_notifications"
    id = db.Column(db.Integer, db.Sequence('id_uln'), primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey(
        'usuarios.id'))
    title = db.Column(db.String(90))
    description = db.Column(db.String(500))
    usuario = db.relationship("Usuario", backref='errores')

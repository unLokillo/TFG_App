import email
from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import current_user, login_required, logout_user
from flask_cors import cross_origin
from flask_api import status

from client.Flaskback.application.models import Usuario


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

def send_mail():
    pass

@main_bp.route("/resetPass", methods=['GET', 'POST'])
@cross_origin(origin='*', headers=['content-type'], supports_credentials=True)
def reset_password():
    user = Usuario.query.filter_by(email=request.json['email']).first()
    if user:
        send_mail()
        return status.HTTP_200_OK
    return status.HTTP_401_UNAUTHORIZED
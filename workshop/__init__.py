from flask import Blueprint

workshop_blue = Blueprint('workshop', __name__, url_prefix='/workshop')
from . import views

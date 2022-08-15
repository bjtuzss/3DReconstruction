from flask import Blueprint

square_blue = Blueprint('square', __name__, url_prefix='/square')
from . import views

from flask import Blueprint

forum_blue = Blueprint('forum', __name__, url_prefix='/forum')
from . import views

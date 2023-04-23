from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/')
def home():
    pass
@auth.route('/img2img')

def img2img():
    pass
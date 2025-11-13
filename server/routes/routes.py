# dataroutes.py
from flask import Blueprint, render_template


# Define seu blueprint corretamente
page_bp = Blueprint('page', __name__)

# Rotas para os arquivos index

@page_bp.route('/')
def index():
    return render_template('index.html')





